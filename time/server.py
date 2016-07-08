import sys
sys.path.append('./gen-py')
 
from whatTime import TimeService
from whatTime.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
import time
import socket

class TimeServiceHandler:
    def __init__(self):
        pass

    def TellMeTime():
        return 'you got me' 



handler = TimeServiceHandler()
processor = TimeService.Processor(handler)
transport = TSocket.TServerSocket('localhost',233333)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print "Starting python server..."
server.serve()
print "done!"
