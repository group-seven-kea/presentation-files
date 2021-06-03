import pika

def send_sms(number, message):
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='notifications')

    channel.basic_publish(exchange='', routing_key='notifications', body=f'{number};{message}')
    connection.close()