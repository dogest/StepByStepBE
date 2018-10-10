from datetime import datetime

import django_env
from Account.models import UserOJBind
from OJs.config import OJs
from Solution.models import Solution


def spider(source, username, last):
    imp = __import__('OJs.{}.solutions'.format(source))
    data = getattr(imp, source).solutions.main(username)
    return data


def main():
    for oj in OJs:
        user_oj_bind_set = UserOJBind.objects.filter(source=oj)
        for i in user_oj_bind_set:
            data = spider(oj, i.username, i.last)
            last = ''
            for j in data:
                solution = Solution(
                    user=i.user,
                    pid=str(j['pid']),
                    runid=str(j['runid']),
                    source=oj,
                    result=str(j['result']),
                    time=int(j.get('time', '0')),
                    memory=int(j.get('memory', '0')),
                    language=str(j.get('language', '')),
                    code_len=int(j.get('code_len', '0')),
                    submission_time=datetime.strptime(str(j['submission_time']),
                                                      '%Y-%m-%d %H:%M:%S'))
                solution.save()
                last = str(j['runid'])
            i.last = last
            i.save()


if __name__ == '__main__':
    main()
