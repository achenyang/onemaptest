import json
import re
import pytest
import requests
from common.yaml_test import write_yaml, read_yaml, read_testcase


class TestOneMap:
    num = 1
    num_d = 1

    @pytest.mark.sm
    @pytest.mark.parametrize('args_name', read_testcase('testonemap.yaml'))
    def test_run_rd_link(self, load_url_editor, args_name):
        # urll = 'http://fastmap.navinfo.com/omtest/oiie-feature-editor/editor/common/run'
        # print(args_name)
        # url = read_yaml('url')
        # data = {
        #     'parameter': '{"userId":"chenyang","workOrderId":"8ea571a5-d63b-4e1c-a77f-dd7a66ea58c1",'
        #                  '"command":"CREATE","type":"RDLINK","data":[{"objName":"RDLINK","objData":{'
        #                  '"geometry":"LINESTRING Z (114.05276987 22.73184234 100, 114.05310307 22.73193659 100, '
        #                  '114.05326145 22.7318964 100, 114.05334811 22.73186729 100, 114.05341385 22.73182017 100, '
        #                  '114.05368728 22.73176057 100)","zSource":1,"zCollect":5,"dataClass":0,"linkSource":1,'
        #                  '"objStatus":"INSERT"}}],"opName":"","opConfig":{"catchLinks":[],"catchNodes":[],'
        #                  '"logId":"22cae10f-a3c0-46d5-9042-e77027d3db52"}}',
        #     'reqContext': '{"bizType": "omGdb", "uid": "chenyang", "catalog": "D"}',
        #     'reqId': 'chenyang_293d84a4 - 2bae - 49bd - b4e4 - a09e4ddd96d0',
        #     'token': '2daa0584 - 04a8 - 4582 - 96c5 - 39cfd78576e8'
        # }
        url = args_name['requests']['url']
        data = args_name['requests']['data']
        me = args_name['requests']['method']
        res = requests.request(method=me, url=url, data=data)
        # print(res.text)
        # link_pid = re.search("'errcode': 0, 'errmsg': '(.*?)'", res.text)错误示例：此处用的是json格式返回
        objpid = re.search('"mesh":"19927196"},"objId":"(.*?)","objName":"RDLINK"', res.text)
        # TestOneMap.link_pid = objpid.group(1)
        link_pid = "link_pid" + str(TestOneMap.num)
        write_yaml({link_pid: objpid.group(1)})
        rowid = re.search('"linkSource":1,"objStatus":"INSERT","rowId":"(.*?)","zCollect"', res.text)
        # TestOneMap.row_id = rowid.group(1)
        row_id = "row_id"+str(TestOneMap.num)
        write_yaml({row_id: rowid.group(1)})
        TestOneMap.num += 1
        # print(TestOneMap.link_pid+' '+TestOneMap.row_id)
        # print(res.json()["data"]["result"]["opResult"][1]["objData"]["linkPid"])
        # print(res.json())
        status = res.status_code
        assert status == int(args_name['validate'])
        print('=========================================================')

    @pytest.mark.sm
    @pytest.mark.parametrize('args_n', read_testcase('testonemap.yaml'))
    def test_run_delete_rd_link(self, args_n):
        url = args_n['requests']['url']
        row_id = "row_id"+str(TestOneMap.num_d)
        rowid = read_yaml(row_id)
        link_pid = "link_pid"+str(TestOneMap.num_d)
        linkpid = read_yaml(link_pid)
        data = {
            'parameter': '{"userId":"chenyang","workOrderId":"8ea571a5-d63b-4e1c-a77f-dd7a66ea58c1",'
                         '"command":"DELETE","type":"RDLINK","data":[{"objName":"RDLINK","objData":{'
                         '"rowId":"'+rowid+'","linkPid":"'+linkpid+'","objStatus":"DELETE"},'
                         '"objVersion":null}],"opConfig":{"logId":"04bd871b-d243-4598-8a1d-eeca888696b9"}} ',
            'reqContext': '{"bizType": "omGdb", "uid": "chenyang", "catalog": "D"}',
            'reqId': 'chenyang_293d84a4 - 2bae - 49bd - b4e4 - a09e4ddd96d0',
            'token': '2daa0584 - 04a8 - 4582 - 96c5 - 39cfd78576e8'
        }
        res = requests.request(method="post", url=url, data=data)
        print(res.text)
        status = res.status_code
        assert status == int(args_n['validate'])
        TestOneMap.num_d += 1


if __name__ == '__main__':
    TestOneMap().test_run_rd_link()
    TestOneMap().test_run_delete_rd_link()

