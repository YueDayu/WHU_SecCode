import cv2
import numpy as np
import os
from os import listdir
from os.path import isfile, join, exists

input_path = './imgs'
output_path = './result'

def process_single_img(image_path):
	img = cv2.imread(image_path)
	cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	h,s,v = cv2.split(img)
	img = 255 - h / 2 - s / 3 + v / 2
	ret, res = cv2.threshold(img,120,255,cv2.THRESH_BINARY)
	return res

def crop_image(image_path):
	img = process_single_img(image_path)
	new_img = img[:, 28:108]
	res = []
	for i in range(0, 5):
		crop_img = new_img[6:, i * 13: i * 13 + 24]
		res.append(crop_img)
	return res

if __name__ == '__main__':
	filelist = [f for f in listdir(input_path) if isfile(join(input_path, f))]
	for x in filelist:
		old_file = join(input_path, x)
		img_list = crop_image(old_file)
		print x + ' processing...'
		for i, img in enumerate(img_list):
			new_path = join(output_path, x[i])
			if not exists(new_path):
				os.makedirs(new_path)
			new_file = join(new_path, x.split('_')[1])
			cv2.imwrite(new_file, img)

# list = crop_image('./imgs/w9y5q_2015122016094058570.jpg')
# for x in list:
# 	cv2.imshow("img", x)
# 	cv2.waitKey(0)
# 	cv2.destroyAllWindows()