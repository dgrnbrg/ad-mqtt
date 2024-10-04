

Version: 0.2.3

```
git clone https://github.com/TD22057/ad-mqtt.git
cd ad-mqtt
python3 -m venv venv
./venv/bin/pip install -r requirements.txt

[edit run.py to add ser2sock, zone info]

./run.py
```

Designed to work with Home Assistant.  Uses MQTT discovery to create sensors
for all zones and the alarm panel automatically.  Times are passed in the
MQTT messages and retained so they can be used to create real "last changed"
time sensors if desired in HASS.

If you use virtual zones, you need to enable the corresponding zone expander
emulation in the Alarm Decoder setup. Then, you can include `is_virtual=True`
in a Zone configuration, and it will get a switch that can be used to trigger
the emulated zone fault.

## Using as a HomeAssistant addon

You can add this repo as a homeassistant addon repository, and then install the ad-mqtt addon.

Here's an example alarm configuration (make sure to put your code in quotes, or it will fail to validate):

```
host: alarmdecoder.local
port: 10000
restore_on_startup: true
code: "1234"
```

Here's an example devices configuration:

```
- zone: 1
  entity: motion_basement
  label: Motion Basement
- zone: 2
  entity: heat_basement
  label: Heat Sensor Basement
  device_class: heat
- zone: 9
  entity: motion_east
  label: Virtual Motion East
  device_class: motion
  is_virtual: true
```
