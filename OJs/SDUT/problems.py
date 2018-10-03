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
    cur = 0
    cli = 0
    while cur < cnt and cli < 100:  # 最多请求 100 次（10000 个题目），防止无限重定向等
        cli += 1
        url = 'https://acm.sdut.edu.cn/onlinejudge2/index.php/API/Problem?pid={}&cmp=g&order=ASC&limit=100'.format(
            cur)
        req = requests.get(url)
        data = json.loads(req.text)
        for p in data:
            return_data.append({
                'pid': str(p['pid']),
                'title': p['title'],
                'url': 'https://acm.sdut.edu.cn/onlinejudge2/index.php/Home/Index/problemdetail/pid/{}.html'.format(p['pid'])
            })
            cur = p['pid']
    return return_data


if __name__ == '__main__':
    with open('problems.json', 'w') as fw:
        fw.write(json.dumps(main(), indent=4, ensure_ascii=False))
