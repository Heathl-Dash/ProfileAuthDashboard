import pika
import json
import os

RABBITMQ_DEFAULT_HOST = os.getenv("RABBITMQ_DEFAULT_HOST")
RABBITMQ_DEFAULT_USER = os.getenv("RABBITMQ_DEFAULT_USER")
RABBITMQ_DEFAULT_PASS = os.getenv("RABBITMQ_DEFAULT_PASS")
RABBITMQ_DEFAULT_VHOST = os.getenv("RABBITMQ_DEFAULT_VHOST")
RABBITMQ_DEFAULT_PORT = os.getenv("RABBITMQ_DEFAULT_PORT")

print(RABBITMQ_DEFAULT_PORT)
def __get_connection_and_channel():
    """devolve a conexão com o rabbitMQ e o canal de comunicação, a conexão
    sempre deve ser fechada no final do seu uso"""
    credentials = pika.PlainCredentials(RABBITMQ_DEFAULT_USER, RABBITMQ_DEFAULT_PASS)
    parameters = pika.ConnectionParameters(
        host=RABBITMQ_DEFAULT_HOST,
        port=int(RABBITMQ_DEFAULT_PORT),
        virtual_host=RABBITMQ_DEFAULT_VHOST,
        credentials=credentials,
    )
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    return connection, channel


def __add_to_exchange(
    exchange: str, body: str, exchange_type: str = "fanout", routing_key: str = ""
):
    """cria uma exchange a partir dos parametros passados"""
    conn, chan = __get_connection_and_channel()
    chan.exchange_declare(exchange=exchange, exchange_type=exchange_type)
    chan.basic_publish(
        exchange=exchange, routing_key=routing_key, body=json.dumps(body)
    )

    conn.close()


def __add_to_queue(
    queue_name: str,
    delivery_mode: int,
    message_dict: dict = {},
    durable: bool = True,
    exchange: str = "",
):
    """cria uma fila a partir dos parametros passados"""
    conn, chan = __get_connection_and_channel()
    chan.queue_declare(queue=queue_name, durable=durable)
    message = json.dumps(message_dict)
    chan.basic_publish(
        exchange=exchange,
        routing_key=queue_name,
        body=message,
        properties=pika.BasicProperties(delivery_mode=delivery_mode),
    )

    # sempre fechar conexão
    conn.close()


def delete_user_publish_event(user_id):
    message_dict = {"user_id": user_id}
    queue_name = "user.deleted"
    delivery_mode = 2
    __add_to_queue(queue_name, delivery_mode, message_dict)


def delete_user_publish_exchange(user_id):
    message_dict = {"user_id": user_id,'event':'delete'}
    exchange_name = "user.events"
    __add_to_exchange(exchange_name, message_dict)

def create_user_publish_exchange(user_id,weight=None):
    message_dict = {"user_id": user_id,'event':'create',"weight":weight}
    exchange_name = "user.events"
    __add_to_exchange(exchange_name, message_dict)