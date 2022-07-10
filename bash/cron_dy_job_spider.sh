#! /bin/bash

# 职位抓取器

dir=$(pwd)
cd ${dir}/../
export PYTHONPATH=${dir}/..:$PYTHONPATH

/usr/local/bin/python3 电鸭/dy_spider.py $* >> /tmp/remote_job_spider.log 2>&1 &
/usr/local/bin/python3 实现网/shixian_spider.py $* >> /tmp/remote_job_spider.log 2>&1 &
