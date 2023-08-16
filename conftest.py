import pytest

from common.yaml_test import write_yaml, clear_yaml


@pytest.fixture(scope='function')
def exe_first():
    print("this is first exe")


@pytest.fixture(scope="function")
def load_url_auto():
    clear_yaml()
    print('前置调用')
    url = "http://fastmap.navinfo.com/omtest/oiie-feature-editor/robot/createJob"
    write_yaml({'url': url})
    # 实现后置调用
    # yield
    # print('后置调用')
    # clear_yaml()


@pytest.fixture(scope="function")
def load_url_editor():
    #clear_yaml()
    print('前置调用')
    url = "http://fastmap.navinfo.com/omtest/oiie-feature-editor/editor/common/run"
    write_yaml({'url': url})

