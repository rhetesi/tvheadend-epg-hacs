from .const import (
    DOMAIN,
    CONF_BASE_URL,
    CONF_UPDATE_INTERVAL,
    DEFAULT_UPDATE_INTERVAL,
    PLATFORMS,
)
from .coordinator import TVHeadendEPGCoordinator


async def async_setup_entry(hass, entry):
    hass.data.setdefault(DOMAIN, {})

    coordinator = TVHeadendEPGCoordinator(
        hass,
        entry.data[CONF_BASE_URL],
        entry.data.get(CONF_UPDATE_INTERVAL, DEFAULT_UPDATE_INTERVAL),
    )

    await coordinator.async_config_entry_first_refresh()

    hass.data[DOMAIN][entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(
        entry,
        PLATFORMS,
    )

    return True
