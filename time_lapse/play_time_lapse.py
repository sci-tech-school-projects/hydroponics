import cv2
from matplotlib import pyplot as plt
import os, sys, math, glob, re, shutil, datetime, time
import logging
from argparse import ArgumentParser

ap = ArgumentParser()
ap.add_argument("-s", '--play_speed', type=int, default=10, help='play speed rate')
args = ap.parse_args()

logger = logging.getLogger('LoggingTest')
logger.setLevel(20)
sh = logging.StreamHandler()
logger.addHandler(sh)


class Play_Time_Lapse():
    dir_to_save = 'images'
    image_paths = glob.glob(os.path.join(os.getcwd(), dir_to_save, '*.jpg'))
    play_speed = args.play_speed

    def __init__(self):
        print('***** init '.__class__.__name__)
        self.image_paths.sort()
        logger.log(20, self.image_paths)

    def Main(self):
        for idx, image_path in enumerate(self.image_paths):
            if idx % self.play_speed == 0:
                logger.log(20, image_path)
                image = cv2.imread(image_path)
                cv2.imshow("time_lapse ", image)

                # if cv2.waitKey(0) % 0xFF == ord('a'):
                #     pass
                if cv2.waitKey(1) % 0xFF == ord('q'):
                    break
        cv2.destroyAllWindows()

    def finalize(self):
        pass


if __name__ == '__main__':
    PTL = Play_Time_Lapse()
    PTL.Main()
