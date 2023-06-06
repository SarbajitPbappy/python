import cv2
import imutils
import numpy as np
import argparse

HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

def detect(frame, writer):
    bounding_box_cordinates, weights =  HOGCV.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.03)
    
    person = 1
    for x, y, w, h in bounding_box_cordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, f'person {person}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        person += 1
    
    cv2.putText(frame, 'Status : Detecting ', (40, 40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    cv2.putText(frame, f'Total Persons : {person-1}', (40, 70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    cv2.imshow('output', frame)

    return frame

def detectByCamera(writer):
    video = cv2.VideoCapture(1)
    print('Detecting people...')

    while True:
        check, frame = video.read()

        frame = detect(frame, writer)
        if writer is not None:
            writer.write(frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


def Human(*args):
    global writer
    writer = None
    if args[0]['output'] is not None:
        writer = cv2.VideoWriter(args[0]['output'], cv2.VideoWriter_fourcc(*'MJPG'), 10, (600, 600))

    if args[0]['camera']:
        detectByCamera(writer)
    else:
        print('Detecting people...')
        # image = cv2.imread(args[0]['image'])

        # image = imutils.resize(image, width=min(800, image.shape[1])) 

        # result_image = detect(image, writer)
        
        # if writer is not None:
            # writer.write(result_image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()



def argsParser():
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument("-c", "--camera", default=False, help="Set true if you want to use the camera.")
    arg_parse.add_argument("-o", "--output", type=str, help="path to optional output video file")
    args = vars(arg_parse.parse_args())
    Human(args)

if __name__ == "__main__":
    argsParser()
