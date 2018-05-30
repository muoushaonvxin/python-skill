在web应用中常用JSON格式传输数据例如我们利用Baidu语音识别服务做语音识别将本地音频数据post到Baidu语音识别服务器, 服务器响应结果为json字符串

```python
var01 = {
    "corpus_no": "123098049218041",
    "err_msg": "success",
    "err_no": 0,
    "result": ["你好", ],
    "sn": "123098120948021984",
}
```

在python中如何读写json数据？

```python
import requests
import json

l = [1, 2, 'abc', {'name': 'Bob', 'age': 13}]
json.dumps(l)
'[1, 2, "abc", {"age": 13, "name": "Bob"}]'

d = {'b': None, 'a': 5, 'c': 'abc'}
json.dumps(d)
'{"a": 5, "c": "abc", "b": null}'

json.dumps(l, separators=[',', ':'])
'[1, 2, 'abc', {"age": 13, "name": "Bob"}]'

d = {"a": 5, "c": None, "b": 456} 
json.dumps(d, sort_keys=True)
'{"a": 5, "b": 456}, "c": null}'
```

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
