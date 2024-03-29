# -*- coding: utf-8 -*-
import json
import os
from multiprocessing import Pool
import time
from azure.iot.device import IoTHubDeviceClient


def send(data, connstr):
    print 'send', data
    try:
        device_client = IoTHubDeviceClient.create_from_connection_string(connstr)
        device_client.connect()
        json_data = json.dumps(data)
        device_client.send_message(json_data)
        device_client.disconnect()
        return 201
    except Exception:
        return False


class Sender(object):

    def __init__(self, batch_size=1):
        self.queue = []
        self.sending = []
        self.batch_size = batch_size
        self.connstr = os.environ.get('PYTILT_CONN_STR', None)

    def add_data(self, data):
        self.queue.append(data)
        if len(self.queue) >= self.batch_size:
            self.send()

    def send(self):
        pool = Pool(processes=1)
        self.sending = list(self.queue)
        self.queue = []
        result = pool.apply_async(send, args=[self.sending, self.connstr], callback=self.completed)
        pool.close()
        pool.join()

    def completed(self, was_sent):
        if was_sent:
            self.sending = []
        else:
            print 'send failed'
            if len(self.queue) > 100:
                self.queue = []
            self.queue += self.sending
