from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity


class TVHeadendEPGSensor(CoordinatorEntity, SensorEntity):
    _attr_name = "TVHeadend EPG"
    _attr_icon = "mdi:television-guide"

    def __init__(self, coordinator):
        super().__init__(coordinator)

    @property
    def native_value(self):
        return len(self.coordinator.data)

    @property
    def extra_state_attributes(self):
        return {
            "epg": self.coordinator.data,
        }
