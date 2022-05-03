import time
import random
from os import path
import yaml
from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily
from prometheus_client import start_http_server

class RandomNumberCollector(object):
    def __init__(self):
        pass
    def collect(self):
        gauge = GaugeMetricFamily("random_number", "A random number generator", labels=["randomNum"])
        gauge.add_metric(['random_num'], random.randint(1, 20))
        yield gauge

if __name__ == "__main__":
    start_http_server(9000)
    REGISTRY.register(RandomNumberCollector())
    while True: 
        # period between collection
        time.sleep(1)