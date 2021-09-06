# 运行环境

|system |python | 
|:------|:------|      
|cross platform |3.9.16|

# 组件安装

```shell
pip install -U django-service-kombu
```

# 入门案例

```yaml
├── manage.py
└── project
    ├── __init__.py
    ├── asgi.py
    ├── urls.py
    ├── wsgi.py
    └── settings.py
```

> settings.py

```python
INSTALLED_APPS = [
    # 主要用于配置检查,可不配置
    'django_service_kombu',
]

KOMBU = {
    'connect_options': {
        'hostname': 'pyamqp://admin:nimda@127.0.0.1:5672//'
    },
    'consume_options': {
        
    },
    'publish_options': {
        
    }
}
```
