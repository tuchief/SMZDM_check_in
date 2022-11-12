# SMZDM_check_in

## 功能介绍
1、什么值得买每日自动签到  
2、签到成功后通过邮件进行提醒当前签到的天数

## chromedriver下载地址
https://chromedriver.storage.googleapis.com/index.html  
https://npm.taobao.org/mirrors/chromedriver

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

## 免责说明
- 本项目仅供个人学习RPA技术参考使用。用户明确同意其使用本开源项目所存在的风险将完全由其自己承担；因其使用本项目而产生的一切后果也由其自己承担，开源作者对用户不承担任何责任。  
- 任何由于使用本开源项目而造成的个人资料泄露、丢失、被盗用或被窜改及由此而导致的任何法律争议和后果等，本开源均得免责。  
- 开源使用者因使用本项目而触犯中华人民共和国法律的，一切后果自己负责，开源作者不承担任何责任。
- 凡以任何方式获取本开源项目代码或直接、间接使用本开源资料者，视为自愿接受本开源声明的约束。
- 声明未涉及的问题参见国家有关法律法规，当本声明与国家法律法规冲突时，以国家法律法规为准。
