#!/usr/bin/env python

import os, sys

curr_dir = os.getcwd() 
print('Join video {dir}'.format(dir=curr_dir))

VIDEO_FILE = os.path.sep.join([curr_dir, 'movies.txt'])
lines = []

hours_dirs = os.listdir(curr_dir)
for hour_dir in hours_dirs:
    if hour_dir in ['.', '..']:
        continue
    hour_dir = os.path.sep.join([curr_dir, hour_dir])    
    if not os.path.isdir(hour_dir):
        continue
    min_dirs = os.listdir(hour_dir)
    min_dirs.sort()
    for min_dir in  min_dirs:
       if   min_dir in ['.', '..']:
           continue
       min_dir = os.path.sep.join([hour_dir, min_dir]) 
       if not os.path.isdir(min_dir):
           continue
       files = os.listdir(min_dir)
       movies = filter(lambda i: i.split('.').pop() == 'mp4', files)
       for move in movies:
           lines.append(os.path.sep.join([min_dir, move]))
           
#print(lines)
with open(VIDEO_FILE, 'w') as f:
    for i in range(0, len(lines)):
        f.write("file '{file}'".format(file=lines[i]))
        if i <  len(lines)-1:
            f.write("\n")

#command = 'ffmpeg -f concat -safe 0 -i movies.txt -c copy output.mkv'
command = 'ffmpeg -f concat -safe 0 -i movies.txt -c:v copy -c:a aac -strict experimental output.mp4'
content = os.popen(command).read()
#content = content.decode('utf-8')
print(content)
