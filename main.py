import json

import smtp_client
import pika

# Establish a connection to RabbitMQ
credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
channel = connection.channel()

# Create the queue
channel.queue_declare(queue='email_queue')


# Define a callback function to process incoming messages
def send_email(ch, method, properties, body):
    body = json.loads(body)
    rec_email = body["email"]
    email_type = body["type"]
    template_data = body["template_data"]
    smtp_client.send_email(rec_email, email_type, template_data)
    print("Received:", body)


# Set up the consumer and start listening for messages
channel.basic_consume(queue='email_queue', on_message_callback=send_email, auto_ack=True)
print("Waiting for messages")
channel.start_consuming()
