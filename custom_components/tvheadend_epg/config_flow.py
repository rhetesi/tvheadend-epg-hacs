from homeassistant import config_entries
import voluptuous as vol
from .const import DOMAIN, CONF_URL, CONF_UPDATE_INTERVAL, DEFAULT_UPDATE_INTERVAL

class TVHeadendEPGConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            return self.async_create_entry(
                title="TVHeadend EPG",
                data=user_input
            )

        schema = vol.Schema({
            vol.Required(CONF_URL): str,
            vol.Optional(CONF_UPDATE_INTERVAL, default=DEFAULT_UPDATE_INTERVAL): int
        })

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
            errors=errors
        )
