import pika, sys, os
from twilio.rest import Client
from os import environ as env

client = Client(env.get("TWILIO_PUBLIC_KEY"), env.get("TWILIO_PRIVATE_KEY"))

def main():
    """ Listens for messages that the main application will send to the queue. """
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='notifications')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        number, message = body.decode("utf-8").split(";")
        send_sms(number, message)

    channel.basic_consume(queue='notifications', on_message_callback=callback, auto_ack=True)
    print('Waiting for tasks. To exit press CTRL+C')
    channel.start_consuming()

def send_sms(number, message):
    """ Sends an SMS to the number provided (must be danish in this proof of concept)
        
        Args:
            number: Phone number retrieved from the user account.
            message: Text message that the user will receive.
    """
    client.messages.create(
            to=f"+45{number}",
            from_="+14845754058",
            body=str(message),
        )


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

