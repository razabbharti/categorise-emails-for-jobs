import imaplib
email_address=str(input("please enter your email address"))
password=str(input("please enter your"))
obj = imaplib.IMAP4_SSL('imap.gmail.com', 993)
obj.login(email_address, password)
obj.create('job')
obj.select('inbox')
result,data=obj.uid('search',None, r'(X-GM-RAW "subject:\"Thank you for applying\"")')
data1=data[0].split()
for i in data1:
    i=i.decode('utf-8')
    apply_lbl_msg = obj.uid('COPY', i, 'job')
    obj.expunge()
print('done')
