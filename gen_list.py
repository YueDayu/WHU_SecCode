# import os

# root_dir = '/home/yuedy13/Desktop/result'
# subdir_list = [o for o in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir,o))]

# out_file = open('list.txt', 'w')

# for x in subdir_list:
# 	current_folder = os.path.join(root_dir, x)
# 	file_list = [os.path.join(x, f) for f in os.listdir(current_folder) if os.path.isfile(os.path.join(current_folder, f))]
# 	lable = 0
# 	if x >= 'a':
# 		lable = ord(x) - ord('a') + 10
# 	else:
# 		lable = int(x)
# 	for y in file_list:
# 		out_file.write(y + ' ' + str(lable) + '\n')

# out_file.close()

import random

radio = 0.07

infile = open('list.txt', 'r')
lines = infile.readlines()
infile.close()

random.shuffle(lines)
num = (int)(len(lines) * radio)

test_list = lines[0:num]
train_list = lines[num+1:]

test_file = open('test_list.txt', 'w')
for x in test_list:
	test_file.write(x)
test_file.close()

train_file = open('train_list.txt', 'w')
for x in train_list:
	train_file.write(x)
train_file.close()
