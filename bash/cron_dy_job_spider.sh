#! /bin/bash

# 职位抓取器

dir=$(pwd)
cd ${dir}/../
export PYTHONPATH=${dir}/..:$PYTHONPATH

# 判断进程是否存在，如果存在则
dy_count=`ps -ef|grep dy_spider.py|grep -v grep | wc -l`
if [ 0 == dy_count ];then
  /usr/local/bin/python3 电鸭/dy_spider.py $* >> /tmp/remote_job_spider.log 2>&1 &
fi

sx_count=`ps -ef|grep shixian_spider.py|grep -v grep | wc -l`
if [ 0 == sx_count ];then
  /usr/local/bin/python3 实现网/shixian_spider.py $* >> /tmp/remote_job_spider.log 2>&1 &
fi