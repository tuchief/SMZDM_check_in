# -*- coding: utf-8 -*-
from email.header import Header
from email.utils import parseaddr, formataddr

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
import selenium.webdriver.support.ui as ui
if 'HTTP_PROXY'in os.environ: del os.environ['HTTP_PROXY']

# ===============================修改下面的内容===================================
# 发送邮箱地址
sendmailAddress = 'abc@163.com'
# 发送邮箱密码(如果邮箱提供授权码，那么密码就填写授权码即可,例如qq、163都提供授权码)
sendmailUserPasswd = '123456'
# smtp服务器地址和端口
smtpServer = 'smtp.163.com'
smtpPort = 25

# 接收邮箱地址
acceptmailAddress = 'abc@qq.com'

# smzdm用户名
smzdm_username = 'abc'
# smzdm密码
smzdm_userpasswd = '123456'

# chromedriver文件路径
CHROME_DRIVER_PATH="/Users/tuchief/smzdm/driver/chromedriver"

# ==============================================================================

chrome_opt = webdriver.ChromeOptions()
# prefs = {"profile.managed_default_content_settings.images": 2}
chrome_opt.add_argument('--headless')
chrome_opt.add_argument('--disable-gpu')
chrome_opt.add_argument("test-type")
chrome_opt.add_argument('--ignore-certificate-errors')
chrome_opt.add_argument('--dns-prefetch-disable')
# chrome_opt.add_experimental_option("prefs", prefs)
dr = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, chrome_options=chrome_opt)

# 签到地址
homePageUrl = 'https://www.smzdm.com/'
logoutUrl = 'https://zhiyou.smzdm.com/user/logout/'

dr.get(homePageUrl)
dr.implicitly_wait(30)

sleep(5)
# dr.find_element_by_class_name('J_login_trigger').click()
dr.execute_script("$('.J_login_trigger').click()")

sleep(5)
dr.switch_to_frame('J_login_iframe')

# smzdm的用户名密码
dr.find_element_by_id('username').send_keys("smzdm_username")
dr.find_element_by_id('password').send_keys("smzdm_userpasswd")

dr.find_element_by_class_name('login_submit').click()

sleep(5)
dr.find_element_by_xpath('//*[@id="index-head"]/div[3]/div[2]/a').click()

sleep(3)
# 获取签到天数
mailTxt =  dr.find_element_by_xpath('//*[@id="index-head"]/div[3]/div[2]/a').text
# 邮件标题（正文）
mailTxt = u"什么值得买——" + mailTxt

dr.get(logoutUrl)

dr.close()

from email.mime.text import MIMEText
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

msg = MIMEText(mailTxt, 'plain', 'utf-8')
# 邮箱的发送和接收地址
msg['From'] = _format_addr(mailTxt+u'<%s>' % sendmailAddress)
msg['To'] = _format_addr(u'管理员 <%s>' % acceptmailAddress)
msg['Subject'] = Header(mailTxt, 'utf-8').encode()

# 填写smtp服务器地址和端口
server = smtplib.SMTP(smtpServer, smtpPort) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(sendmailAddress, sendmailUserPasswd)
# 发送邮件, 发送邮件地址、接收邮件地址
server.sendmail(sendmailAddress, [acceptmailAddress], msg.as_string())
server.quit()
