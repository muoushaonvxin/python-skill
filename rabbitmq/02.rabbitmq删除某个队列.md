
```python
import pika

credentials = pika.PlainCredentials("guest", "guest")
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.1', 5672, '/', credentials))
channel = connection.channel()
queue = channel.queue_delete(queue='test')
```
