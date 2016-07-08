#/home/ubuntu/python-dev/bin
import sys
sys.path.append('./gen-py')
#che dan
from helloworld import HelloWorld
from helloworld.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
 
import socket,time

class HelloWorldHandler:
  def __init__(self):
    self.log = {}

  def ping(self):
    print "ping()"

  def sayHello(self):
    print "sayHello()"
    return str(time.time()) + "say hello from " + socket.gethostbyname(socket.gethostname())

  def sayMsg(self, msg):
    print "sayMsg(" + msg + ")"
    return "say " + msg + " from " + socket.gethostbyname(socket.gethostname())

handler = HelloWorldHandler()
processor = HelloWorld.Processor(handler)
transport = TSocket.TServerSocket('localhost',30303)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print "Starting python server..."
server.serve()
print "done!"

