import sys
sys.path.append('./gen-py')


from whatTime import TimeService
from whatTime.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:
  # Make socket
  transport = TSocket.TSocket('localhost', 233333)

  # Buffering is critical. Raw sockets are very slow
  transport = TTransport.TBufferedTransport(transport)

  # Wrap in a protocol
  protocol = TBinaryProtocol.TBinaryProtocol(transport)

  # Create a client to use the protocol encoder
  client = TimeService.Client(protocol)

  # Connect!
  transport.open()


  msg = client.TellMeTime()
  print msg

  transport.close()

except Thrift.TException, tx:
  print 'error'
  print "%s" % (tx.message)
