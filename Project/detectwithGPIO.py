import RPi.GPIO as GPIO
from RPi._GPIO import *
import time
import numpy as np
import cv2
import imutils
import argparse
LIGHT_PIN = 18
FAN_PIN = 23


def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LIGHT_PIN, GPIO.OUT)
    GPIO.setup(FAN_PIN, GPIO.OUT)


def turn_on_lights():
    GPIO.output(LIGHT_PIN, GPIO.HIGH)


def turn_off_lights():
    GPIO.output(LIGHT_PIN, GPIO.LOW)


def turn_on_fan():
    GPIO.output(FAN_PIN, GPIO.HIGH)


def turn_off_fan():
    GPIO.output(FAN_PIN, GPIO.LOW)


def display_detections(frame, detections):
    person = 1
    for (x, y, w, h) in detections:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, f'Person {person}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        person += 1
    cv2.putText(frame, 'Status : Detecting', (40, 40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    cv2.putText(frame, f'Total Persons : {person - 1}', (40, 70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    cv2.imshow('Output', frame)
    return frame


def detect_by_camera(output_path=None):
    video = cv2.VideoCapture(1)

    if not video.isOpened():
        print('Failed to open the camera.')
        return

    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(video.get(cv2.CAP_PROP_FPS))

    if output_path is not None:
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        output_video = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    else:
        output_video = None

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    motion_detected = False

    print('Detecting people...')
    while True:
        ret, frame = video.read()
        if not ret:
            break

        frame = imutils.resize(frame, width=min(800, frame.shape[1]))

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        detections, _ = hog.detectMultiScale(gray, winStride=(4, 4), padding=(8, 8), scale=1.03)

        display_detections(frame, detections)

        if len(detections) > 0:
            motion_detected = True
            turn_on_lights()
            turn_on_fan()
        else:
            if motion_detected:
                # Wait for 5 seconds before turning off lights and fan
                time.sleep(5)
                turn_off_lights()
                turn_off_fan()
                motion_detected = False

        if output_video is not None:
            output_video.write(frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    video.release()

    if output_video is not None:
        output_video.release()
        print('Video saved.')

    cv2.destroyAllWindows()


def main():
    parser = argparse.ArgumentParser(description="Human Detection")
    parser.add_argument('--output', help="Output Path (Video)")
    args = parser.parse_args()

    setup_gpio()
    detect_by_camera(args.output)


if __name__ == "__main__":
    main()
