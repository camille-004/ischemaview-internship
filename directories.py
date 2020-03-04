import json
import os
import shutil
import itertools
from os.path import isfile, join
from collections import OrderedDict

file_path = 'patient_data_no_pid_dec_01_2018_to_dec_15_2018/patient_data_with_qa_wo_pid.json'

# Keys from JSON file with eight slices and a pass probability less than 40
items = []

with open(file_path) as f:
	data = OrderedDict(json.load(f))
	for (k, v) in data.items():
		if v['slices'] == 8 and float(v['pass_prob']) < 40:
			items.append(json.dumps(k))

single_images_path = "/Users/camilledunning/Desktop/Code/iSchemaView/patient_data_no_pid_dec_01_2018_to_dec_15_2018/single_images"
mtt_files_path = "/Users/camilledunning/Desktop/Code/iSchemaView/mtt_files"
tmax_files_path = "/Users/camilledunning/Desktop/Code/iSchemaView/tmax_files"

# Get files from the single_images directory
image_files = [f for f in os.listdir(single_images_path) if isfile(join(single_images_path, f))]

mtt_files = []
tmax_files = []

# MTT and TMAX images that correspond to JSON keys in items list
mtt_files_items = []
tmax_files_items = []

for image in image_files:
	if "mtt" in image:
		mtt_files.append(image)
	if "tmax" in image:
		tmax_files.append(image)

for item in items:
	for mtt, tmax in itertools.zip_longest(mtt_files, tmax_files, fillvalue=('','')):
		if item[1:-1] in mtt:
			mtt_files_items.append(mtt)
		elif item[1:-1] in tmax:
			tmax_files_items.append(tmax)

# Lists of actual files
mtt_file_list = []
tmax_file_list = []

mtt_file_list = [os.path.join(single_images_path, m) for m in mtt_files_items]
tmax_file_list = [os.path.join(single_images_path, t) for t in tmax_files_items]

for mttfile in mtt_file_list:
	shutil.copy(mttfile, mtt_files_path)

for tmaxfile in tmax_file_list:
	shutil.copy(tmaxfile, tmax_files_path)