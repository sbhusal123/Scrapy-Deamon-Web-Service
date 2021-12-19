# Scrapy Deamon Web Service
An Approach to use a scrapy spiders as an independent web services with django and rabbitmq as a message broker

- **Django** as a independent application which consumes the items scraped.
- **Scrapy** python based framework for scraping smart phones listed in daraz.
- **Splash** as a javascript rendering enginee.
- **Scrapyd** to deamonize our scrapy spiders which exposes the rest endpoint for managing our spiders. 
- **Rabbitmq** as a message broker to communicate (pass scraped items independently) to our django server.