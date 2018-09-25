#
from riaps.run.comp import Component
import logging

import pprint
from time import time

from influxdb import InfluxDBClient
from influxdb.client import InfluxDBClientError

import json
import datetime
import random
import time

USER = 'riapsdev'
PASSWORD = 'riaps'
DBNAME = 'traffic'

class Logger(Component):
    def __init__(self):
        super(Logger, self).__init__()
        #self.host = '192.168.0.111'
        self.host = '192.168.0.108'
        self.port = '8086'
        self.series = []
        
        self.client = InfluxDBClient(self.host, self.port, USER, PASSWORD, DBNAME)
        
        print("Running")
        #self.retention_policy = 'awesome_policy'
        #self.client.create_retention_policy(self.retention_policy, '3d', 3, default=True)
        
                
    def on_subICPort(self):
        msg = self.subICPort.recv_pyobj()
        record =[]
        self.logger.info("subICLog: \n %s", pprint.pformat(msg))
        now = datetime.datetime.now()
        current_time = now.strftime('%Y-%m-%dT%H:%M:%SZ')
        metric = "density"
       
         
        
        pointValues = {
                "time": current_time,
                "measurement": metric,
                'fields':  {
                    'segment0': msg['Densities']['segment0'],
                    'segment1': msg['Densities']['segment1'],
                    'segment2': msg['Densities']['segment2'],
                    'segment3': msg['Densities']['segment3'],
                },
                'tags': {
                    "Actor" : msg['IC']
                },
            }
        record.append(pointValues)
        
        before_timeStamp = datetime.datetime.now()
        self.client.write_points(record),#, retention_policy=self.retention_policy)
        after_timeStamp = datetime.datetime.now()
        time_past = (after_timeStamp - before_timeStamp)
        print(time_past)
        
    def on_subLightLog(self):
        msg = self.subLightLog.recv_pyobj()
        self.logger.info("subLightLog: \n %s", pprint.pformat(msg))
        record =[]
        
        now = datetime.datetime.now()
        current_time = now.strftime('%Y-%m-%dT%H:%M:%SZ')
        metric = "lightState"
        
        pointValues = {
                "time": current_time,
                "measurement": metric,
                'fields':  {
                    #'LightState0': 1,
                    'LightState0': msg['GameLightState']['segment0']['vehicle'],
                    'LightState1': msg['GameLightState']['segment1']['vehicle'],
                    'LightState2': msg['GameLightState']['segment2']['vehicle'],
                    'LightState3': msg['GameLightState']['segment3']['vehicle'],
                },
                'tags': {
                    "Actor" : msg['IC']
                },
            }
        record.append(pointValues)
        self.client.write_points(record),#, retention_policy=self.retention_policy)
        
    def on_clock(self):
        msg = self.clock.recv_pyobj()
       
        