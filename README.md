# Scrapy Deamon Web Service
An Approach to use a scrapy spiders as an independent web service with django and rabbitmq as a message broker

- **Django** as a independent application which consumes the items scraped.
- **Scrapy** python based framework for scraping smart phones listed in daraz.
- **Splash** as a javascript rendering enginee.
- **Scrapyd** to deamonize our scrapy spiders which exposes the rest endpoint for managing our spiders. 
- **Rabbitmq** as a message broker to communicate (pass scraped items independently) to our django server.

# Installation
- **Install python packages:** ``pip install -r requirements.txt``
- **Install Rabbitmq** ``sudo apt-get install rabbitmq-server``
- **Install Splash:** ``sudo docker run -it -p 8050:8050 --rm scrapinghub/splash``

# Runing spider
- **Install python packages:** ``pip install -r requirements.txt``
- **Migrate Databse:** ``python itemsbackend/manage.py migrate``
- **Start Django Consumer[-]** ``python itemsbackend/manage.py consumer.py``
- **Start scrapy deamon[-]** ``cd darazcrawler && scrapyd``
- **Deploy the default spider to deamon:** ``cd darazcrawler && scrapyd-deploy default``
- **Runing spider:** ``curl http://localhost:6800/schedule.json -d project=default -d spider=smart_phones``


> [-] => These needs to run in background / separate terminal. Or they can be daemonized to run in background
 as a separate system service.