Vue.config.devtools = true;
import { apiService } from "../common/api.service.js";

new Vue({
  el: '#pos-profile',
  delimiters: ['[[', ']]'],
  data: {
    profiles: [],
    gasStations: {},
    loading: false,

  },
  mounted() {
    this.fetchLoginCredentials();
    this.fetchGasStation();
  },
  methods: {
    fetchLoginCredentials() {
      this.loading = true;
      let endpoint = "/api/v1/user/";
      apiService(endpoint)
        .then((response) => {
          this.profiles = response.data;
          this.loading = false;
        })
        .catch(err => {
          this.loading = false;
        })
    },
    fetchGasStation() {
      this.loading = true;
      let endpoint = "/api/v1/gas-station/";
      apiService(endpoint)
        .then((response) => {
          this.gasStation = response.data;
          this.loading = false;
        })
        .catch(err => {
          this.loading = false;
        })
    }
  }
})