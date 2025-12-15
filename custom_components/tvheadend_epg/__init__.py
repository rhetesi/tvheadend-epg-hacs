from .const import DOMAIN
from .coordinator import TVHeadendEPGCoordinator

async def async_setup_entry(hass, entry):
    hass.data.setdefault(DOMAIN, {})

    coordinator = TVHeadendEPGCoordinator(
        hass,
        entry.data["url"],
        entry.data.get("update_interval", 300)
    )

    await coordinator.async_config_entry_first_refresh()
    hass.data[DOMAIN][entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])
    return True
