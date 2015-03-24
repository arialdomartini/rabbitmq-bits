import pika
import os

connectionString = os.environ['CLOUD_AMQP_CONNECTIONSTRING']
connection = pika.BlockingConnection(pika.URLParameters(connectionString))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(channel, method, properties, body):
    print "[x] Received %r" % (body, )

channel.basic_consume(callback, queue='hello', no_ack = True )
