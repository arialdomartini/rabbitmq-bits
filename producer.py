import pika
import os

connectionString = os.environ['CLOUD_AMQP_CONNECTIONSTRING']
connection = pika.BlockingConnection(pika.URLParameters(connectionString))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello',  body='Hello World!')
print " [x] Sent 'Hello World!'"
