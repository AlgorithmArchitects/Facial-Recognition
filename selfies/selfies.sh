#!/bin/sh

echo "Please enter Student ID"
read id
if [ ! -d "$id" ]; then
    mkdir $id
fi
for var in `seq 1 10`;
do
    fswebcam -d /dev/video0 -r 640x480 --jpeg 85 -F 5 $id/$var.jpg
done
