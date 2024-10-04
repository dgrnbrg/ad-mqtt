import logging
import sys
import os
import json
sys.path.insert( 0, "." )
import ad_mqtt as AD

with open('/data/options.json') as f:
    options = json.load(f)

cfg = AD.Config()

# Alarm Decoder ser2sock server location.
cfg.alarm.host = options['alarm']['host']
cfg.alarm.port = options['alarm'].get('port', 10000)
# To reset all zones to closed (not faulted) on startup, set this to True
cfg.alarm.restore_on_startup = options['alarm'].get('restore_on_startup', True)

# MQTT Broker connection
cfg.mqtt.broker = os.env['MQTT_HOST']
cfg.mqtt.port = os.env['MQTT_PORT']
cfg.mqtt.username = os.env['MQTT_USERNAME']
cfg.mqtt.password = os.env['MQTT_PASSWORD']
# Optional encryption settings for the broker.
cfg.mqtt.encryption.ca_cert = None
cfg.mqtt.encryption.certfile = None
cfg.mqtt.encryption.keyfile = None

# Debugging information
cfg.log.level = options['log_level']
cfg.log.screen = True
cfg.log.modules = ["ad_mqtt", "insteon_mqtt"]

# For possible device class values, see:
# https://www.home-assistant.io/integrations/binary_sensor/#device-class
alarm_code = options['alarm']['code']
devices = []
for d in options['devices']:
    devices.append(AD.Zone(
        zone = d['zone'],
        entity = d['entity'],
        label = d['label'],
        device_class = d.get('device_class'),
        is_virtual = d.get('is_virtual', False),
    ))

AD.run.run(cfg, alarm_code, devices)

