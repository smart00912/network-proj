# -*- coding:utf-8 -*-  
__author__ = 'sean.li'

import SocketServer

class MyTCPHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		while 1:
			# self.request is the TCP socket connected to client
			self.data = self.request.recv(1024).strip()
			if not self.data:
				print "client %s disconnected..." % self.client_address[0]
				break
			if self.data.split()[0] == 'put':
				print "Going to receive file %s" % self.data.split()[1]
				f= open('recv/%s' %self.data.split()[1],'wb')
				self.request.send("ReadyToReceiveFile")
				# 此处不可用 if not data判断
				while 1:
					data = self.request.recv(4096)
					if data == 'done':
						print "Transfer is done..."
						break
					f.write(data)
				f.close()
			# client_address是一个元组，包括一个ip和端口
			print self.client_address[0],'-------',self.client_address[1]
			print self.data
			# send back the data,but upper-cased
			self.request.sendall(self.data.upper())
if  __name__ == "__main__":
	# 每个连接上的客户端都运行着一个和服务器的实例链接，断开的话也是实例不影响其他客户端的链接
	HOST,PORT="10.0.2.15",9999
	# create socket server and binding localhost om port 9999
	server =SocketServer.ThreadingTCPServer((HOST,PORT),MyTCPHandler)
	server.serve_forever()
