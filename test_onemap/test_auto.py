import pytest
import requests

from common.yaml_test import read_yaml, write_yaml


class TestAuto:

    @pytest.mark.sms
    def test_job_auto(self, load_url_auto):
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
        print(res.text)