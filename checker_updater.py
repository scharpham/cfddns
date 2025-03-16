import time
from cloudflare import Cloudflare
import os, urllib
from dotenv import load_dotenv
import random
import datetime

load_dotenv()

remotes = {}

remotes['https://v4.ident.me/'] =  ""
remotes['https://checkip.amazonaws.com'] =  ""

def rand_remote():
    count_keys = len(remotes.keys())
    rand_idx = random.randint(0, count_keys-1)
    rand_url = list(remotes.keys())[rand_idx]
    return rand_url

def get_wan_ip():
    wan_v4 = urllib.request.urlopen(rand_remote()).read().decode('utf8')
    return wan_v4

def get_datetime():
    dt = datetime.datetime.now()
    str_dt = datetime.datetime.strftime(dt, "%Y-%m-%d")
    return str_dt

def init_client():
    client = Cloudflare(
        api_email=os.environ.get("CLOUDFLARE_EMAIL"),  # This is the default and can be omitted
        api_key=os.environ.get("CLOUDFLARE_API_KEY"),  # This is the default and can be omitted
    )
    return client

def get_current_dns_ip():
    page = init_client().dns.records.list(
        zone_id=os.environ.get("ZONE_ID"),
    )
    dns_ip = page.result[0].content
    return dns_ip


def update_record():
    record_response = init_client().dns.records.update(
        dns_record_id=os.environ.get("DNS_RECORD_ID"),
        zone_id=os.environ.get("ZONE_ID"),
        name= os.environ.get("NAME"),
        content = get_wan_ip(),
        proxied=False,
        type=os.environ.get("TYPE")
    )
    return record_response


def equality_check():
    #first check history for the last dns ip
    #if history is empty, set entry
    if get_wan_ip()!=last_dns_ip['ip']:
        #if last dns not equal to wan update record both on cloudflar and locally
        last_dns_ip['ip']=update_record().content
    else:
        #if wan ip = dns ip, then  no update is needed, do nothing
        pass

last_dns_ip = {}
last_dns_ip['ip']= get_current_dns_ip()


while True:
    try:
        equality_check()
    except:
        pass
    time.sleep(60*5)


