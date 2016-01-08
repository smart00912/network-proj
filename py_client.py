#coding:  utf8
__author__ = 'sean.li'
import socket
import time

HOST='192.168.1.51'
PORT= 9999
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
'''
if not s.connect_ex((HOST,PORT)):
	str='hello world'
	s.sendall(str)
	data=s.recv(1024)
	s.close()
	print 'Received',repr(data)
else:                                                                                  
	print 'connection failed'
'''
while 1:
	user_input= raw_input("Your msg:").strip()
	if len(user_input) == 0:continue
	s.sendall(user_input)
	data = s.recv(1024)
	if data == 'ReadyToReceiveFile':
		with open(user_input.split()[1]) as f:
			s.sendall(f.read())
			time.sleep(0.5)
			s.send('done')
	print 'file send done'
#如果close放在while内则每次客户端发送数据后都要close造成服务端也停掉
s.close()

