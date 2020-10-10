#!/bin/bash
cd $(dirname $0)
for id in `ps -ef|grep "car_main" | grep -v "grep" |awk '{print $2}'`
do
kill -9 $id
echo "kill $id"
done
source ~/anaconda3/etc/profile.d/conda.sh
conda activate garage_manager
nohup python car_main.py > recogizeLog.out 2>&1 &
nohup python car_yolov4_test_html.py 2>&1 &
