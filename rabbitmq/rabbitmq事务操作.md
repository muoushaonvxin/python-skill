
```python
import pika

credentials = pika.PlainCredentials("guest", "guest")
connection = pika.BlockingConnection(pika.ConnectionParameters("192.168.1.1", 5672, '/', credentials))
channel = connection.channel()

try:
    channel.tx_select()
    channel.exchange_declare(exchange="250test", exchange_type="direct", durable=True)
    serverity = "info"
    channel.basic_publish(exchange="250test", routing_key=serverity, body="hello world")
    channel.tx_commit()
except Exception as e:
    print("rabbitmq connection has error")
    channel.rollback()
connection.close()
```
