#!/usr/bin/env python
#coding:utf-8
import ConfigParser
import poplib
from email.header import decode_header
from email.parser import Parser
from email.utils import parseaddr

import time



def connect_pop3(host,username,password):
    t=time.clock()
    server = poplib.POP3(host,)
    connecttime=time.clock()-t
    server.user(username)
    server.pass_(password)
    logintime=time.clock()-connecttime-t
    return server,connecttime,logintime

def get_mail(host,username,password):
  conn, cTime, lTtime = connect_pop3(host, username, password)
  t0 = time.clock()
  count,size=conn.stat()
  getmailtime=time.clock()-t0
  resp, mails, octets = conn.list()
  conn.quit()
  logouttime=time.clock()-getmailtime-t0
  return mails,count,size,getmailtime,logouttime


def read_mail(host,username,password):
     conn,cTime,lTtime= connect_pop3(host,username,password)
     # 读取邮件列表中最新的邮件
     t1 = time.clock()
     mailInfo,mailCount,mailTotalsize,gTime,loTime=get_mail(host,username,password)
     resp, lines, octets = conn.retr(mailInfo[-1])
     readmailtime=time.clock()-t1
     msg_content = '\r\n'.join(lines)
     msg = Parser().parsestr(msg_content)
     return msg,readmailtime

def print_info(msg, indent=0):
         if indent == 0:
             for header in ['From', 'To', 'Subject']:
                 value = msg.get(header, '')
                 if value:
                     if header == 'Subject':
                         value = decode_str(value)
                     else:
                         hdr, addr = parseaddr(value)
                         name = decode_str(hdr)
                         value = u'%s <%s>' % (name, addr)
                 print('%s%s: %s' % ('  ' * indent, header, value))
         if (msg.is_multipart()):
             parts = msg.get_payload()
             for n, part in enumerate(parts):
                 print('%spart %s' % ('  ' * indent, n))
                 print('%s--------------------' % ('  ' * indent))
                 print_info(part, indent + 1)
         else:
             content_type = msg.get_content_type()
             if content_type == 'text/plain' or content_type == 'text/html':
                 content = msg.get_payload(decode=True)
                 charset = guess_charset(msg)
                 if charset:
                     content = content.decode(charset)
                 print('%sText: %s' % ('  ' * indent, content + '...'))
             else:
                 print('%sAttachment: %s' % ('  ' * indent, content_type))

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset
