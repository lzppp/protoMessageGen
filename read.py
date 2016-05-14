import testgen_pb2
#import models
def RequestCommonParser(RequestCommon):
	# newRequest = models.RequestCommon()
	# newRequest.userid = RequestCommon.userid
	# newRequest.userkey = RequestCommon.userkey
	# newRequest.cmdid = RequestCommon.cmdid
	# newRequest.timestamp = RequestCommon.timestamp
	# newRequest.version = RequestCommon.version
	# newRequest.platform = RequestCommon.platform
	# # ##print output
	print(RequestCommon.userid)
	print(RequestCommon.userkey)
	print(RequestCommon.cmdid)
	print(RequestCommon.timestamp)
	print(RequestCommon.version)
	print(RequestCommon.platform)


requset = testgen_pb2.RequestCommon()
requset.ParseFromString(b'\x08\x98\xacK\x12\x0cyuxiangxiang\x18\xb5\xc4\x07 \xee\xe0\xdb\xb9\x05*\x051.0.00\x01')
RequestCommonParser(requset)