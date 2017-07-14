#!/usr/bin/env python  
#coding:utf-8
import string,time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from src.sysinfo.loadavginfo import load_stat
from src.sysinfo.diskinfo import disk_stat
from src.sysinfo.meminfo import memory_stat
import datetime
from src.readmailinfo import *

def connect_smtp(host, port, username, password):
     t0 = time.clock()
     smtp = smtplib.SMTP()
     smtp.connect(host, port)
     connectTime = (time.clock() - t0)
     smtp.login(username, password)
     loginTime = (time.clock() - connectTime - t0)
     return smtp, connectTime,loginTime


def send_mail(host, port, username, receiver,password, Title, context):
    msg = MIMEText(context, 'plain', 'utf-8')
    msg['Subject'] = Header(Title, 'utf-8')
    con,cTime,lTime=connect_smtp(host,port,username,password)
    t0 = time.clock()
    con.sendmail(username,receiver, msg.as_string())
    sendmailTime = time.clock()-t0
    con.quit()
    logoutTime = (time.clock() - sendmailTime-t0)
    return sendmailTime,logoutTime







