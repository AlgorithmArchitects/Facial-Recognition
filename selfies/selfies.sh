#!/bin/sh

for var in `seq 1 10`;
do
    fswebcam -d /dev/video0 -r 640x480 --jpeg 85 -F 5 subject16_$var.jpg
done
