import aiohttp
import async_timeout
from datetime import timedelta
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

class TVHeadendEPGCoordinator(DataUpdateCoordinator):

    def __init__(self, hass, url, interval):
        self.url = url
        super().__init__(
            hass,
            name="TVHeadend EPG",
            update_interval=timedelta(seconds=interval)
        )

    async def _async_update_data(self):
        try:
            async with aiohttp.ClientSession() as session:
                async with async_timeout.timeout(15):
                    async with session.get(self.url) as resp:
                        resp.raise_for_status()
                        json_data = await resp.json()
                        return json_data.get("entries", [])
        except Exception as err:
            raise UpdateFailed(f"TVHeadend EPG error: {err}")
