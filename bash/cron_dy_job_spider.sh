#! /bin/bash

# 电鸭职位抓取器

dir=$(pwd)
cd ${dir}/../电鸭/
export PYTHONPATH=${dir}/..:$PYTHONPATH

/usr/local/bin/python3 dy_spider.py $* > /tmp/remote_job_spider.log 2>&1
