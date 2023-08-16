import re

import pytest
import requests

from common.yaml_test import write_yaml, read_yaml


class TestOneMap:
    url = '1'
    link_pid = ''
    row_id = ''

    @pytest.mark.sm
    def test_run_rd_link(self, load_url_editor):
        # urll = 'http://fastmap.navinfo.com/omtest/oiie-feature-editor/editor/common/run'
        url = read_yaml('url')
        data = {
            'parameter': '{"userId":"chenyang","workOrderId":"8ea571a5-d63b-4e1c-a77f-dd7a66ea58c1",'
                         '"command":"CREATE","type":"RDLINK","data":[{"objName":"RDLINK","objData":{'
                         '"geometry":"LINESTRING Z (114.05276987 22.73184234 100, 114.05310307 22.73193659 100, '
                         '114.05326145 22.7318964 100, 114.05334811 22.73186729 100, 114.05341385 22.73182017 100, '
                         '114.05368728 22.73176057 100)","zSource":1,"zCollect":5,"dataClass":0,"linkSource":1,'
                         '"objStatus":"INSERT"}}],"opName":"","opConfig":{"catchLinks":[],"catchNodes":[],'
                         '"logId":"22cae10f-a3c0-46d5-9042-e77027d3db52"}}',
            'reqContext': '{"bizType": "omGdb", "uid": "chenyang", "catalog": "D"}',
            'reqId': 'chenyang_293d84a4 - 2bae - 49bd - b4e4 - a09e4ddd96d0',
            'token': '2daa0584 - 04a8 - 4582 - 96c5 - 39cfd78576e8'
        }
        res = requests.request(method='post', url=url, data=data)
        print(res.text)
        # link_pid = re.search("'errcode': 0, 'errmsg': '(.*?)'", res.text)错误示例：此处用的是json格式返回
        objpid = re.search('"mesh":"19927196"},"objId":"(.*?)","objName":"RDLINK"', res.text)
        # TestOneMap.link_pid = objpid.group(1)
        write_yaml({'link_pid': objpid.group(1)})

        rowid = re.search('"linkSource":1,"objStatus":"INSERT","rowId":"(.*?)","zCollect"', res.text)
        # TestOneMap.row_id = rowid.group(1)
        write_yaml({'row_id': rowid.group(1)})
        # print(TestOneMap.link_pid+' '+TestOneMap.row_id)
        # print(res.json()["data"]["result"]["opResult"][1]["objData"]["linkPid"])
        # print(res.json())
        print('=========================================================')

    def test_url_print(self):
        print(TestOneMap().url)
        print(TestOneMap().link_pid)
        print('=========================================================')

    @pytest.mark.sm
    def test_run_delete_rd_link(self, load_url_editor):
        url = read_yaml('url')
        row_id = read_yaml('row_id')
        link_pid = read_yaml('link_pid')
        data = {
            'parameter': '{"userId":"chenyang","workOrderId":"8ea571a5-d63b-4e1c-a77f-dd7a66ea58c1",'
                         '"command":"DELETE","type":"RDLINK","data":[{"objName":"RDLINK","objData":{'
                         '"rowId":"'+row_id+'","linkPid":"'+link_pid+'","objStatus":"DELETE"},'
                         '"objVersion":null}],"opConfig":{"logId":"04bd871b-d243-4598-8a1d-eeca888696b9"}} ',
            'reqContext': '{"bizType": "omGdb", "uid": "chenyang", "catalog": "D"}',
            'reqId': 'chenyang_293d84a4 - 2bae - 49bd - b4e4 - a09e4ddd96d0',
            'token': '2daa0584 - 04a8 - 4582 - 96c5 - 39cfd78576e8'
        }
        res = requests.request(method="post", url=url, data=data)
        print(res.text)

    @pytest.mark.sms
    def test_job_auto(self, load_url):
        # url = "http://fastmap.navinfo.com/omtest/oiie-feature-editor/robot/createJob"
        url = read_yaml('url')
        print(url)
        data = {
            'parameter': '{"meshIds":["19927196"],"taskId":"8ea571a5-d63b-4e1c-a77f-dd7a66ea58c1",'
                         '"userId":"chenyang","catalog":"D"}',
            'reqContext': '{"bizType": "omGdb", "uid": "chenyang", "catalog": "D"}',
            'reqId': 'chenyang_293d84a4 - 2bae - 49bd - b4e4 - a09e4ddd96d0',
            'token': '2daa0584 - 04a8 - 4582 - 96c5 - 39cfd78576e8'
        }
        res = requests.request(method="post", url=url, data=data)
        write_yaml({'link_pid': 12345678})
        redd = read_yaml('link_pid')
        print(res.text)
        print(redd)


if __name__ == '__main__':
    TestOneMap().test_run_rd_link()
    TestOneMap().test_run_delete_rd_link()
    obj = TestOneMap()
    obj.test_url_print()
    obj.test_job_auto()
