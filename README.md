# SMZDM_check_in

## 功能介绍
1、什么值得买每日自动签到  
2、签到成功后通过邮件进行提醒当前签到的天数

## chromedriver下载地址
https://chromedriver.storage.googleapis.com/index.html

## 安装
1、install python3 
2、install pip  
3、pip install selenium  
4、根据部署的环境不同，下载安装不同的chrome
5、安装Chromedriver驱动，同样参考安装的环境去下载

## 使用方法
在对应的操作系统上配置定时任务来运行 `python main.py`

by windows  
run.bat文件是为Windows的任务计划设置而准备的  
可以使用windows的任务计划来自动每天定时来完成签到

by linux
crontab -e 
30 0 *  *  * python ..../main.py

## 效果预览
![](https://ws2.sinaimg.cn/large/006tNc79gy1fop166qxxrj30yi1pc1l3.jpg)
