Vue.config.devtools = true;
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

new Vue({
  el: '#pos-gas',
  delimiters: ['[[', ']]'],
  data() {
    return {
      gasStations: [],
      managers: [],
      staffs: [],
      loading: false,
      viewing: false,
      saving: false,
      currentGas: {}
    };
  },
  mounted() {
    this.fetchGasStations();
    this.fetchManagers();
    this.fetchStaffs();
  },
  methods: {
    fetchGasStations() {
      this.loading = true;
      let endpoint = `/api/v1/gas-station/`;
      if (this.gasStations) {
        axios.get(endpoint)
          .then((response) => {
            this.gasStations = response.data;
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
      }
    },
    fetchGasStation(id) {
      this.loading = true;
      let endpoint = `/api/v1/gas-station/${id}/`;
      if (this.currentGas) {
        axios.get(endpoint)
          .then((response) => {
            this.currentGas = response.data;
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
      }
    },
    fetchManagers() {
      this.loading = true;
      let endpoint = `/api/v1/manager/`;
      if (this.managers) {
        axios.get(endpoint)
          .then((response) => {
            this.managers = response.data;
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
      }
    },
    fetchStaffs() {
      this.loading = true;
      let endpoint = `/api/v1/staff/`;
      if (this.staffs) {
        axios.get(endpoint)
          .then((response) => {
            this.staffs = response.data;
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
      }
    },
    updateGas() {
      this.saving = true;
      let endpoint = `/api/v1/gas-station/${this.currentGas.id}/`;
      if (this.currentGas) {
        axios.put(endpoint, this.currentGas)
          .then((response) => {
            this.saving = false;
            this.currentGas = response.data;
            this.fetchGasStations();

            $("#gasStationModal").modal("hide")
          })
          .catch((err) => {
            this.saving = false;
            console.log(err);
          })
      }
    },
  }
})