import testgen_pb2
import sys

# This function fills in a Person message based on user input.
def Prompt(RequestCommon):
  RequestCommon.userid = 1234456
  RequestCommon.userkey = 'yuxiangxiang'
  RequestCommon.cmdid = 123445
  RequestCommon.timestamp = 1463218286
  RequestCommon.version = '1.0.0'
  RequestCommon.platform = 1

# Main procedure:  Reads the entire address book from a file,
#   adds one person based on user input, then writes it back out to the same
#   file.
aRequestCommon = testgen_pb2.RequestCommon()
Prompt(aRequestCommon)
print(aRequestCommon.SerializeToString())

# Add an address.
# Prompt()
# print(RequestCommon.SerializeToString())