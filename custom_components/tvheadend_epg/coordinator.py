import logging
from datetime import timedelta
from urllib.parse import urljoin

import aiohttp
import async_timeout

from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
)

from .const import EPG_ENDPOINT, DEFAULT_EPG_LIMIT

_LOGGER = logging.getLogger(__name__)


class TVHeadendEPGCoordinator(DataUpdateCoordinator):

    def __init__(self, hass, base_url: str, interval: int):
        self.base_url = base_url.rstrip("/")
        self.epg_url = urljoin(
            self.base_url + "/",
            f"{EPG_ENDPOINT}?limit={DEFAULT_EPG_LIMIT}",
        )

        super().__init__(
            hass,
            _LOGGER,
            name="TVHeadend EPG",
            update_interval=timedelta(seconds=interval),
        )

    async def _async_update_data(self):
        try:
            async with aiohttp.ClientSession() as session:
                async with async_timeout.timeout(15):
                    async with session.get(self.epg_url) as response:
                        response.raise_for_status()
                        json_data = await response.json()
                        return json_data.get("entries", [])
        except Exception as err:
            raise UpdateFailed(
                f"TVHeadend EPG fetch failed: {err}"
            ) from err
