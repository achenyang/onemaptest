import os

import yaml


def read_yaml(key):
    with open(os.getcwd()+'/onemap.yaml', mode='r', encoding='utf-8') as r:
        va = yaml.load(stream=r, Loader=yaml.FullLoader)
        return va[key]


def write_yaml(data):
    with open(os.getcwd()+'/onemap.yaml', mode='a', encoding='utf-8') as w:
        yaml.dump(data, stream=w, allow_unicode=True)


def clear_yaml():
    with open(os.getcwd()+'/onemap.yaml', mode='w', encoding='utf-8') as c:
        c.truncate()


def read_testcase(yaml_name):
    with open(os.getcwd()+'/test_onemap/'+yaml_name, mode='r', encoding='utf-8') as f:
        re = yaml.load(stream=f, Loader=yaml.FullLoader)
        return re
