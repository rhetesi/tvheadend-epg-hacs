from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN


async def async_setup_entry(hass, entry, async_add_entities):
    """Set up TVHeadend EPG sensor from a config entry."""
    coordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities(
        [
            TVHeadendEPGSensor(coordinator),
        ]
    )


class TVHeadendEPGSensor(CoordinatorEntity, SensorEntity):
    _attr_name = "TVHeadend EPG"
    _attr_icon = "mdi:television-guide"

    def __init__(self, coordinator):
        super().__init__(coordinator)

    @property
    def native_value(self):
        """Return number of EPG events."""
        return len(self.coordinator.data)

    @property
    def extra_state_attributes(self):
        """Expose full EPG data for Lovelace card."""
        return {
            "epg": self.coordinator.data,
        }
