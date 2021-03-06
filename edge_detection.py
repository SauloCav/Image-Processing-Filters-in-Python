#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import skimage
import skimage.feature
import skimage.viewer
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("your_image.jpg", 0)

edges2 = skimage.feature.canny(
    image=img,
    sigma=2,
    low_threshold=2,
    high_threshold=10,
)

plt.imshow(edges2)
plt.show()
