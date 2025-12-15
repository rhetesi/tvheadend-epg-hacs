class TVHeadendEPGCard extends HTMLElement {
  setConfig(config) {
    if (!config.entity) {
      throw new Error("Entity megadása kötelező");
    }
    this.config = config;
  }

  set hass(hass) {
    const state = hass.states[this.config.entity];
    if (!state) return;

    const epg = state.attributes.epg || [];

    this.innerHTML = `
      <ha-card header="Műsorújság">
        <div style="padding: 12px">
          ${epg.map(e => `
            <div style="margin-bottom: 6px">
              <b>${e.channelName || "Ismeretlen csatorna"}</b><br>
              ${e.title}
              <small>
                (${new Date(e.start * 1000).toLocaleTimeString()} -
                 ${new Date(e.stop * 1000).toLocaleTimeString()})
              </small>
            </div>
          `).join("")}
        </div>
      </ha-card>
    `;
  }

  getCardSize() {
    return 6;
  }
}

customElements.define("tvheadend-epg-card", TVHeadendEPGCard);
