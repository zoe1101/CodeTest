import json


def har_json_parse(har_path=''):
    with open(har_path, 'rb') as load_har_json:
        har_json = json.load(load_har_json)
    return har_json


class har_parse:
    pass


if __name__ == '__main__':
    api_list = [{'method': '',
                 'url': '',
                 'params': '',
                 'body': '',
                 'headers': '',
                 'cookies': '',
                 'response': '',
                 }
                ]
    har_json_file = har_json_parse(har_path=r'../../data/test.har')
    print(har_json_file)
    url_list = har_json_file['log']['entries']
    # 解析
    if len(url_list) > 0:
        for item in url_list:
            print(item['request']['url'])
            # 请求返回的内容
            # print(item['response']['content'])
