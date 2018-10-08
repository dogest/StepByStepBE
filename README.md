# StepByStep

## Usage

```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

在实际部署项目之前，需要将项目由 DEBUG 模式调整至发布模式：

1. 修改 `settings.py` 中的 `SECRET_KEY`
2. `DEBUG` 改为 `False`
3. `ALLOWED_HOSTS` 设置为发布网站
4. `CORS_ORIGIN_ALLOW_ALL` 改为 `False`
5. 将前端的网址加到 `CORS_ORIGIN_WHITELIST` 中
