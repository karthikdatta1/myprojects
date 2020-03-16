import os
import cv2
import matplotlib
import numpy as np

from .detectorr import detection
# %matplotlib inline
import matplotlib.pyplot as plt
import math

# path = "/home/userd618/Documents/opencv/test"
# dirs = os.listdir(path)
# print(len(dirs))

# count = 0
from matplotlib.pyplot import figure

detector = detection()


# directory = "/home/userd618/Documents/opencv/updated_result"
# for file in dirs:
#     path1 = path + "/" + file

def blob(path):

    # path1 = os.path.join('/home/userd618/PycharmProjects/blackspot/', 'images')
    print(path)
# import pdb;pdb.set_trace()
# print(os.listdir(path1))
    count = 0
    im = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    keypoints = detector.detect(im)
    print(len(keypoints))
    if len(keypoints) == 0:
        return False
    #         plt.imshow(im)

    if len(keypoints) >= 1:
        count += 1
        im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0, 0, 255),
                                              cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        #         img = cv2.resize(im_with_keypoints, None, fx=5,fy=5,interpolation=cv2.INTER_CUBIC)
        for keyPoint in keypoints:
            x = keyPoint.pt[0]
            y = keyPoint.pt[1]
            x = math.floor(x)
            y = math.floor(y)

        image = cv2.circle(im_with_keypoints, (x, y), 60, (0, 0, 255), 5)
        return True
    # figure(num=None, figsize=(10, 10), dpi=100, facecolor='w', edgecolor='k')
    # #         os.chdir(directory)
    # plt.imshow(image)
    # #         cv2.imwrite(file,image)
    #
    # plt.show()

#         print(file)
# print(count)

# cv2.imshow("Keypoints", im_with_keypoints)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# print(len(keypoints))
