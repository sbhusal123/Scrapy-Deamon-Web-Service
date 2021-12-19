# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import pika
import json


class DarazcrawlerPipeline:
    """Rabbitmq Pipeline to publish the item"""

    def __init__(self) -> None:
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host="localhost", 
                port=5672
            )
        )

        self.channel = self.connection.channel()

    def publish(self, method, body):
        properties = pika.BasicProperties(method)
        self.channel.basic_publish(
            exchange='',
            routing_key='backend',
            body=body,
            properties=properties
        )
    

    def process_item(self, item, spider):
        self.publish('smart_phones', json.dumps(item))
        return item
