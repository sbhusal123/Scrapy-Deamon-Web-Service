# Setting up scrapyd Daemon

## 1. [scrapyd](https://scrapyd.readthedocs.io/en/stable/)

> Scrapyd is an application for deploying and running Scrapy spiders. It enables you to deploy (upload) your projects and control their spiders using a JSON API.

- **Installation:** ``pip install scrapyd``
- **Launch Scrapy Daemon Server:** ``scrapyd`` by default runs on ``127.0.0.1:6800``

## 2. [scrapyd-client](https://pypi.org/project/scrapyd-client/1.0.1/)

Scrapyd-client is a client for Scrapyd. It provides:
- ``scrapyd-deploy``, to deploy your project to a Scrapyd server
- ``scrapyd-client``, to interact with your project once deployed

## 3. Configuring the deployment:

>scrapy.cfg

```cfg
# Automatically created by: scrapy startproject
#
# For more information about the [deploy] section see:
# https://scrapyd.readthedocs.io/en/latest/deploy.html

[settings]
default = darazcrawler.settings

[deploy:default]
url = http://localhost:6800/
project = darazcrawler
```
****



[Deployment Docs](https://github.com/scrapy/scrapyd-client#scrapyd-deploy)

## 4. Deploy:
-  ``scrapyd-deploy default``

- Note that ``default`` corresponds to ``[deploy:default]`` section of config file which contains information about the url address of scrapyd server and the project we want to deploy

- This eggifys the project and uploads the egg to scrapyd server using a rest api. All the available endpoints are listed [here](https://scrapyd.readthedocs.io/en/latest/api.html).

Response:
```json
Packing version 1639903841
Deploying to project "darazcrawler" in http://localhost:6800/addversion.json
Server response (200):
{"node_name": "surya-Vostro-3459", "status": "ok", "project": "darazcrawler", "version": "1639903841", "spiders": 1}
```

## 5. Runing our spider:
```curl
curl http://localhost:6800/schedule.json -d project=<project_name> -d spider=<spider_name>
```

```curl
curl http://localhost:6800/schedule.json -d project=default -d spider=smart_phones
```

