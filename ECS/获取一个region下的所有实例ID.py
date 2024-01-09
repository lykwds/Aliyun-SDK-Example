from aliyunsdkcore.client import AcsClient
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
import json

def get_instances(client, page_number):
    request = DescribeInstancesRequest.DescribeInstancesRequest()
    request.set_accept_format('json')
    request.set_PageSize(50)  # 每页实例数量
    request.set_PageNumber(page_number)  # 第几页


    response = client.do_action_with_exception(request)
    json_response = json.loads(str(response, encoding='utf-8'))

    instanceIDs = [instance["InstanceId"] for instance in json_response["Instances"]["Instance"]]
    return json_response["TotalCount"], instanceIDs


client = AcsClient('<your-access-key-id>', '<your-access-key-secret>', 'cn-hangzhou')

all_instanceIDs = []
page_number = 1
while True:
    total_count, instanceIDs = get_instances(client, page_number)
    all_instanceIDs += instanceIDs
    # 如果已经获取了所有实例，则退出循环
    if len(all_instanceIDs) >= total_count:
        break
    # 否则，获取下一页的数据
    else:
        page_number += 1

print(all_instanceIDs)
