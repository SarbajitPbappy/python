import numpy as np
import cv2
import imutils
import argparse


def DisplayDetect(frame):
    bounding_box_cordinates, weights = HOGCV.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.03)
    person = 1
    for x, y, w, h in bounding_box_cordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, f'person {person}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        person += 1
    cv2.putText(frame, 'Status : Detecting ', (40, 40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    cv2.putText(frame, f'Total Persons : {person - 1}', (40, 70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    cv2.imshow('output', frame)
    return frame


def DetectByPath(road, people):
    video = cv2.VideoCapture(road)
    check, frame = video.read()
    if not check:
        print('Video Not Found. Please Enter a Valid Path (Full path of Video Should be Provided).')
        return
    print('Detecting people...')
    while video.isOpened():
        # check is True if reading was successful
        check, frame = video.read()
        if check:
            frame = imutils.resize(frame, width=min(800, frame.shape[1]))
            frame = DisplayDetect(frame)
            if people is not None:
                people.write(frame)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break
        else:
            break
    video.release()
    cv2.destroyAllWindows()
    if people is not None:
        people.release()
        people = None
        print('Video Saved.')


def DetectByCamera(people):
    video = cv2.VideoCapture(0)
    print('Detecting people...')
    while True:
        check, frame = video.read()
        frame = DisplayDetect(frame)
        if people is not None:
            people.write(frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()


def DetectByImage(path, output_path):
    image = cv2.imread(path)
    image = imutils.resize(image, width=min(800, image.shape[1]))
    result_image = DisplayDetect(image)
    if output_path is not None:
        cv2.imwrite(output_path, result_image)
        print('Image Saved.')
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def HUMAN(args):
    image_path = args.image
    video_path = args.video
    camera = args.camera
    output_path = args.output

    if str(camera).lower() == 'true':
        print('Detecting people...')
        DetectByCamera(cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'MJPG'), 10, (600, 600)))
    elif video_path is not None:
        DetectByPath(video_path, cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'MJPG'), 10, (600, 600)))
    elif image_path is not None:
        DetectByImage(image_path, output_path)
    else:
        print('Detecting people...')
        DetectByCamera(cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'MJPG'), 10, (600, 600)))


def main():
    parser = argparse.ArgumentParser(description="Human Detection")
    parser.add_argument('--image', help="Image Path")
    parser.add_argument('--video', help="Video Path")
    parser.add_argument('--camera', help="Use Camera", action='store_true')
    parser.add_argument('--output', help="Output Path (Image/Video)")
    args = parser.parse_args()
    HUMAN(args)


if __name__ == "__main__":
    HOGCV = cv2.HOGDescriptor()
    HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    main()
