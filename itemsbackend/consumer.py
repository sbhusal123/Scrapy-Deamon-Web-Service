import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "itemsbackend.settings")
django.setup()

from items.models import Item

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost", port=5672))
channel = connection.channel()

channel.queue_declare(queue='backend')


def callback(ch, method, properties, body):
    print("--"*100)
    item = json.loads(body)
    if properties.content_type == 'smart_phones':
        print(item)
        try:
            i_obj = Item.objects.create(
                title=item['title'],
                price=item['discounted_price']
            )
            i_obj.save()
        except Exception as e:
            print(f"Excaption occured: {e}")
    print("--"*100)


channel.basic_consume(queue='backend', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()