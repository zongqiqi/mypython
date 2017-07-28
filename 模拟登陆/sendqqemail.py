# -*- coding: utf-8 -*-


def sendmail(toaddress,subject,message):
    import smtplib
    from email.mime.text import MIMEText
    # _user = "544136329@qq.com"
    _user = "zongqiqi0522@foxmail.com"
    _pwd  = "amrnypvaabhvbejd"
    _to   = toaddress

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"]    = _user
    msg["To"]      = _to

    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(_user, _pwd)
        s.sendmail(_user, _to, msg.as_string())
        s.quit()
        print "Success!"
    except smtplib.SMTPException,e:
        print "Falied,%s"%e

# sendmail('544136329@qq.com','first text','宗七七，Hello world')


# ###=====================imaplib接收邮件===============================================
# import imaplib
# import email
#
# def extract_body(payload):
#     if isinstance(payload,str):
#         return payload
#     else:
#         return '\n'.join([extract_body(part.get_payload()) for part in payload])
#
# conn = imaplib.IMAP4_SSL("imap.foxmail.com",993)
# conn.login("zongqiqi0522@foxmail.com", "amrnypvaabhvbejd")
# conn.select()
# typ, data = conn.search(None, 'ALL')
# try:
#     for num in data[0].split():
#         typ, msg_data = conn.fetch(num, '(RFC822)')
#         for response_part in msg_data:
#             if isinstance(response_part, tuple):
#                 msg = email.message_from_string(response_part[1])
#                 subject=msg['subject']
#                 print(subject)
#                 payload=msg.get_payload()
#                 body=extract_body(payload)
#                 print (body)
#         typ, response = conn.store(num, '+FLAGS', r'(\Seen)')
# finally:
#     try:
#         conn.close()
#     except:
#         pass
#     conn.logout()
# ###=======================================================================================

#
# import imaplib
# mailserver = imaplib.IMAP4_SSL('imap.foxmail.com', 993)
# username = 'zongqiqi0522@foxmail.com'
# password = 'amrnypvaabhvbejd'
# mailserver.login(username, password)
# status, count = mailserver.select('Inbox')
# status, data = mailserver.fetch(count[0], '(UID BODY[TEXT])')
# print data[0][1]
# mailserver.close()
# mailserver.logout()




###=================================================成功！！取回邮件===========================================
import imaplib
import email
mail = imaplib.IMAP4_SSL('imap.foxmail.com', 993)
mail.login('zongqiqi0522@foxmail.com', 'amrnypvaabhvbejd')
mail.list()
mail.select("inbox")  # connect to inbox.

result, data = mail.search(None, "ALL")

ids = data[0]  # data is a list.
id_list = ids.split()  # ids is a space separated string
latest_email_id = id_list[-5]  # get the latest

result, data = mail.fetch(latest_email_id, "(RFC822)")  # fetch the email body (RFC822) for the given ID

raw_email = data[0][1]
mailpar = email.message_from_string('\r\n'.join(raw_email))
# mailpar = email.message_from_string(raw_email)
# print raw_email
f = open('qqmail.eml','wb')
f.write(raw_email)
f.close()
# subject=email.Header.decode_header(mailpar['subject'])[0][0]
# subcode=email.Header.decode_header(mailpar['subject'])[0][1]
# print subject.decode('gb2312')

fp = open("qqmail.eml", "r")
msg = email.message_from_file(fp)
for par in msg.walk():
    if not par.is_multipart():  # 这里要判断是否是multipart，是的话，里面的数据是无用的，至于为什么可以了解mime相关知识。
        name = par.get_param("name")  # 如果是附件，这里就会取出附件的文件名
        if name:
            # 有附件
            # 下面的三行代码只是为了解码象=?gbk?Q?=CF=E0=C6=AC.rar?=这样的文件名
            h = email.Header.Header(name)
            dh = email.Header.decode_header(h)
            fname = dh[0][0]
            print '附件名:', fname
            data = par.get_payload(decode=True)  # 解码出附件数据，然后存储到文件中

            try:
                f = open(fname, 'wb')  # 注意一定要用wb来打开文件，因为附件一般都是二进制文件
            except:
                print '附件名有非法字符，自动换一个'
                f = open('aaaa', 'wb')
            f.write(data)
            f.close()
        else:
            # 不是附件，是文本内容
            print par.get_payload(decode=True)  # 解码出文本内容，直接输出来就可以了。

        print '+' * 60  # 用来区别各个部分的输出

mail.close()
mail.logout()
###============================================================================================================



