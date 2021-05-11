import cv2
import os, sys, math, glob, re, shutil, datetime, time


class Camera_Test():

    def Main(self):
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            cv2.imshow('camera', frame)
            if cv2.waitKey(1) % 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    CT = Camera_Test()
    CT.Main()
