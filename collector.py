import os
import time
from prometheus_client.core import GaugeMetricFamily, REGISTRY
from prometheus_client import start_http_server

metric = GaugeMetricFamily("disk_encryption", "all system metrics", labels=["encrypted", "disk_name"])

class CustomCollector(object):

    def collect(self):
        def is_encrypted(diskname):
            # Placeholder logic
            if diskname.startswith('/'):
                return 'true'
            else:
                return 'false'

        du = os.popen("df -h | awk '{print $1}' | grep -Eiv 'Filesystem|map'")
        for line in du:
            if line: # To avoid empty lines
                encrypted = is_encrypted(line)
            else:
                continue
            metric.add_metric([encrypted, line.strip()], 1)

        yield metric

if __name__ == "__main__":
    start_http_server(9000)
    REGISTRY.register(CustomCollector())
    while True: 
        # period between collection
        time.sleep(5)