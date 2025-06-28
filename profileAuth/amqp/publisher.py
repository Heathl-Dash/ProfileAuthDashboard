import pika
import json
import os

RABBITMQ_DEFAULT_HOST = os.getenv("RABBITMQ_DEFAULT_HOST")
RABBITMQ_DEFAULT_USER=os.getenv('RABBITMQ_DEFAULT_USER')
RABBITMQ_DEFAULT_PASS=os.getenv('RABBITMQ_DEFAULT_PASS')
RABBITMQ_DEFAULT_VHOST=os.getenv('RABBITMQ_DEFAULT_VHOST')


'''devolve a conexão com a fila, a conexão
sempre deve ser fechada no final do seu uso '''
def __get_connection_and_channel():
    credentials=pika.PlainCredentials(RABBITMQ_DEFAULT_USER,RABBITMQ_DEFAULT_PASS)
    parameters=pika.ConnectionParameters(
        host=RABBITMQ_DEFAULT_HOST,
        virtual_host=RABBITMQ_DEFAULT_VHOST,
        credentials=credentials
    )
    connection=pika.BlockingConnection(parameters)
    channel=connection.channel()

    return connection,channel


def delete_user_publish_event(user_id):
    conn,chan=__get_connection_and_channel()
    queue_name='user.deleted'

    chan.queue_declare(queue=queue_name,durable=True)
    message=json.dumps({'user_id':user_id})
    chan.basic_publish(
        exchange='',
        routing_key=queue_name,
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2
        )
    )

    #sempre fechar conexão
    conn.close()
    
