import json

import requests


def get_cnt():
    url = 'https://acm.sdut.edu.cn/onlinejudge2/index.php/API/Problem?limit=1'
    req = requests.get(url)
    data = json.loads(req.text)
    return data[0]['pid']


def main():
    cnt = get_cnt()
    return_data = []
    for i in range(1000, cnt + 1):
        url = 'https://acm.sdut.edu.cn/onlinejudge2/index.php/API/Problem?pid={}'.format(
            i)
        req = requests.get(url)
        data = json.loads(req.text)
        if not data:
            print('题目 {} 无法获取'.format(i))
            continue
        data = data[0]
        return_data.append({
            'pid': data['pid'],
            'title': data['title'],
        })
        print('获取题目 {} 成功'.format(i))
    return return_data


if __name__ == '__main__':
    with open('problems.json', 'w') as fw:
        fw.write(json.dumps(main(), indent=4, ensure_ascii=False))
