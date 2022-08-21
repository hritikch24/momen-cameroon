import requests
import schedule
import time
request_Latency_list=[]
cache_Latency_list=[]
db_Latency_list=[]
request_Latency_dict={}
cache_Latency_dict={}
db_Latency_dict={}
def curl():
    x = requests.get('http://localhost/health')
    if x.status_code!=200:
        exit(1)
def update_list():
    x = requests.get('http://localhost/health')
    request_Latency=x.json()["metrics"]["requestLatency"]
    db_Latency=x.json()["metrics"]["dbLatency"]
    cache_Latency=x.json()["metrics"]["cacheLatency"]
    request_Latency_list.append(request_Latency)
    cache_Latency_list.append(cache_Latency)
    db_Latency_list.append(db_Latency)
def stdout():
    request_Latency_dict["maximum"]=max(request_Latency_list)
    request_Latency_dict["minimum"]=min(request_Latency_list)
    request_Latency_dict["Average"]=sum(request_Latency_list)/len(request_Latency_list)
    db_Latency_dict["maximum"]=max(db_Latency_list)
    db_Latency_dict["minimum"]=min(db_Latency_list)
    db_Latency_dict["Average"]=sum(db_Latency_list)/len(db_Latency_list)
    cache_Latency_dict["maximum"]=max(cache_Latency_list)
    cache_Latency_dict["minimum"]=min(cache_Latency_list)
    cache_Latency_dict["Average"]=sum(cache_Latency_list)/len(cache_Latency_list)
    print("Request latency :{}".format(request_Latency_dict))
    print("Db_latency: {}".format(db_Latency_dict))
    print("cache_latency: {}".format(cache_Latency_dict))
def make_list_empty():
    request_Latency_list=[]
    cache_Latency_list=[]
    db_Latency_list=[]

schedule.every(10).seconds.do(curl)
schedule.every(1).seconds.do(update_list)
schedule.every(6.001).seconds.do(stdout)
schedule.every(6.002).seconds.do(make_list_empty)
while True:
   schedule.run_pending()
   time.sleep(0)
