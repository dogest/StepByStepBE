# StepByStep 爬虫拓展

StepByStep 可以通过自行编写爬虫来支持更多的 OJ，需要的爬虫如下：

- `problems.py`
- `solutions.py`
- `user_check.py`

在此目录下新建一个文件夹，文件夹名即为要支持的 OJ，然后在 `config.py` 的 `OJs` 列表中添加此 OJ，重启项目即可。

## 爬虫规范

每个爬虫文件都要实现名为 `main` 的函数，这个函数需要将所需的数据直接返回。每个文件的 `main` 函数的参数与返回格式各不相同。

爬虫函数会作为模块被导入，因此 `if __name__ == '__main__'` 的代码块不会被执行，可以在此处执行测试等操作。

## problems.py

爬取对应 OJ 所有题目的爬虫

参数：

无

返回值：

```json
[
    {
        "pid": 1000,
        "title": "A + B Problem"
    },
    {
        "pid": 1001,
        "title": "487-3279"
    },
    {
        "pid": 1002,
        "title": "Biorhythms"
    },
    {
        "pid": 1003,
        "title": "ID Codes"
    },
    {
        "pid": 1004,
        "title": "Packets"
    },
    {
        "pid": 1005,
        "title": "Farmland"
    }
]
```

## solutions.py

获取某用户的所有提交

参数：

- username：用户名
- last：上次爬取到的地方

返回值：

```json
[
    {
        "pid": 1000,
        "source": "SDUT",
        "result": "Wrong Answer",
        "time": 30,
        "memory": 8168,
        "submission_time": "2016-01-27 19:29:49",
        "language": "Python",
        "uid": 21060,
        "code_length": 43
    },
    {
        "pid": 3406,
        "source": "SDUT",
        "result": "Wrong Answer",
        "time": 40,
        "memory": 8168,
        "submission_time": "2016-01-27 21:10:08",
        "language": "Python",
        "uid": 21060,
        "code_length": 32
    },
    {
        "pid": 3406,
        "source": "SDUT",
        "result": "Wrong Answer",
        "time": 30,
        "memory": 8156,
        "submission_time": "2016-01-27 21:10:58",
        "language": "Python",
        "uid": 21060,
        "code_length": 33
    },
]
```

其中 pid、source、result、submission_time 是必须要有的。

### source

就是对应 OJ，与文件夹名相同

### result

必须是下列选项之一：

- Waiting
- Accepted
- Time Limit Exceeded
- Memory Limit Exceeded
- Wrong Answer
- Runtime Error
- Output Limit Exceeded
- Compile Error
- Presentation Error
- System Error
- Judging
- Other

大小写必须严格相同，且字符串前后没有多余空格。

### language

必须是下列选项之一：

- C
- C++
- Java
- Python
- C#
- PHP
- Ruby
- JavaScript
- Go
- Scala
- Kotlin
- Swift
- Pascal
- Fortran
- Lua
- Haskell
- Perl
- Other

大小写必须严格相同，字符串前后没有空格。

Python 不区分 2 与 3，没有记录的语言全部归于 Other。

### time

程序运行耗时，不提供此数据不会影响功能使用，但会导致统计数据出错。

单位为毫秒（ms）

### memory

程序运行占用内存，同样不影响使用，仅影响统计数据。

单位为 KB

### submission_time

提交时间，格式为 `yyyy-MM-dd HH:mm:ss`，仅影响统计数据。

### code_length

代码长度，仅影响统计数据。

## user_check.py

用于在绑定账号时确认账号所有权，不能以任何形式保存用户提交的密码。

参数：

- username：用户名
- password：密码

返回值：

- True if 验证通过 else False