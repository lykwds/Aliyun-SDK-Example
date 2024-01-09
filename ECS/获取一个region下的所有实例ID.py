from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest

# 创建一个AcsClient实例
client = AcsClient(
   "<your-access-key-id>", 
   "<your-access-key-secret>",
   "cn-hangzhou")

# 创建一个DescribeInstancesRequest实例
request = DescribeInstancesRequest.DescribeInstancesRequest()

# 发送请求并获取response
response = client.do_action_with_exception(request)

# 从response中抽取实例ID
instanceIds = [instance["InstanceId"] for instance in response["Instances"]["Instance"]]
