import requests


def main(username, password):
    url = 'https://acm.sdut.edu.cn/onlinejudge2/index.php/Home/Login/login'
    data = {
        'user_name': username,
        'password': password
    }
    req = requests.post(url, data=data, allow_redirects=False)
    req.encoding = 'utf-8'
    if req.status_code == 302 and req.headers.get('Location') == 'Index/index':
        return True
    return False


if __name__ == '__main__':
    username = input('username: ')
    password = input('password: ')
    print(main(username, password))
