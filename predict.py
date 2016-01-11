import numpy as np
import sys
import caffe
import matplotlib.pyplot as plt
import os
import show_image
import cv2
from os import listdir
from os.path import isfile, join, exists

# caffe_root = '../caffe-master/'
MODEL_FILE = 'lenet.prototxt'
PRETRAINED = 'code.caffemodel'

class_list = '0123456789abcdefghijklmnopqrstuvwxyz'

# input_image = caffe.io.load_image(IMAGE_FILE, color=False)

net = caffe.Classifier(MODEL_FILE, PRETRAINED, image_dims=(24, 24))

def predict(filename):
    img_list = show_image.crop_image(filename)
    for i, x in enumerate(img_list):
        cv2.imwrite('temp/' + str(i) + '.jpg', x)
    res = ""
    real = os.path.basename(filename).split('_')
    for i in range(0, 5):
        input_image = caffe.io.load_image('temp/' + str(i) + '.jpg', color=False)
        out = net.predict([input_image])
        # print class_list[int(out[0].argmax())]
        res += class_list[int(out[0].argmax())]
    return res, res == real[0]

test_path = '/home/yuedy13/Downloads/testdata'

filelist = [join(test_path, f) for f in listdir(test_path) if isfile(join(test_path, f))]
all_num = len(filelist)
num = 0
i = 0
char_num = 5000
char_error = 0
for x in filelist:
    res, judge = predict(x)
    i += 1
    if judge == False:
        real = os.path.basename(x).split('_')[0]
        for index in range(0, 5):
            if real[index] != res[index]:
                char_error += 1
        num += 1
        print x + ' ' + res + ' ' + str(i) + ' ' + str(num)
print float(num) / all_num
print 'char error: ' + str(float(char_error) / char_num)
# print predict('lea3r_2015123019521195222.jpg')