
```python
import pika

credentials = pika.PlainCredentials("hitrader", "hitrader123")
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.99.234', 5672, '/', credentials))
channel = connection.channel()
queue = channel.queue_declare(queue="test", durable=True, exclusive=False, auto_delete=False)
print("the queue %s message count is: %d." % (queue.method.queue, queue.method.message_count))
```
