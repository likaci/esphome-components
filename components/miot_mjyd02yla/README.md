# Xiaomi Mijia Night Light 2 (MJYD02YL)

<img src="miot_mjyd02yla.png" alt="MJYD02YL" width="200"/>

> This componint at beta state, please leave feedback.

> You colud automaticaly get bindkey from Xiaomi Cloud by configuring `xiaomi_account` property in [MIOT](../miot/) platform.

Sample configuration:
```yaml
external_components:
  - source: github://dentra/esphome-components

binary_sensor:
  - platform: miot_mjyd02yla
    # String (Required), device MAC-address.
    mac_address: "device-mac-address"
    # String, (Optional), device bind key. Will use [xiaomi_account](../miot/) if absent.
    bindkey: "device-bin-key"
    # String, (Optional), the name of binary sensor
    name: "MJYD02YL Motion"
    # BinarySensor (Optional), Light intensivity: on - strong light, off - weak light
    light:
      name: "MJYD02YL Light"
    # Sensor (Optional), Time in seconds of inactivity
    idle_time:
      name: "MJYD02YL Idle Time"
    # Sensor (Optional), Battey Level, %
    battery_level:
      name: "MJYD02YL Battery Level"
```