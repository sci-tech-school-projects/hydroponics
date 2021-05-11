#!/usr/bin/python3
## -*- coding: UTF-8 -*-
import cv2
import os, sys, math, glob, re, shutil, datetime, time


class Time_Lapse_Camera():
    """
    :param dir_to_save = '/home/pi/time_lapse'
    """
    try:
        base_dir = sys.argv[1]
    except IndexError:
        print('sys.argv[1] needs absolute path of project directory')
        sys.exit()

    dir_to_save = os.path.join(base_dir, 'images')

    def __init__(self):
        self.create_dir()

    def create_dir(self):
        if not os.path.exists(self.dir_to_save):
            os.mkdir(self.dir_to_save)

    def create_name(self):
        now = datetime.datetime.now()
        name = now.strftime("%Y_%m%d_%H%M%S") + ".jpg"
        print(name)
        return name

    def log(self):
        file = os.path.join(self.base_dir, "camera_log")
        if not os.path.exists(file):
            with open(file, "w") as l:
                l.write("")
        with open(file, "a") as l:
            l.write(self.create_name() + "\n")

    def Main(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if ret:
                path_file_name = os.path.join(self.dir_to_save, self.create_name())
                self.log()
                cv2.imwrite(path_file_name, frame)
                time.sleep(10)

    def finalize(self):
        pass


if __name__ == '__main__':
    TLC = Time_Lapse_Camera()
    TLC.Main()
