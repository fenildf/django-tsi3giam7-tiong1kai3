# 試驗中介django套件

[![Build Status](https://travis-ci.org/sih4sing5hong5/django-tsi3giam7-tiong1kai3.svg?branch=master)](https://travis-ci.org/sih4sing5hong5/django-tsi3giam7-tiong1kai3)
[![Coverage Status](https://coveralls.io/repos/sih4sing5hong5/django-tsi3giam7-tiong1kai3/badge.svg?branch=master&service=github)](https://coveralls.io/github/sih4sing5hong5/django-tsi3giam7-tiong1kai3?branch=master)

用來處理echo server佮實際django程式的套件

## 使用
### 設定
佇`settings.py`
```python
MIDDLEWARE_CLASSES += (
    '試驗中介.轉址佮設定資料.轉址佮設定資料',
)
```

### 連線
任何`POST`連線，參數有
```python
{
    '模式': '轉址',
    '網域': 'http://意傳.台灣',
}
```


## 授權
本軟體採用MIT授權