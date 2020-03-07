Vue.config.devtools = true;
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

new Vue({
  el: '#pos-gas',
  delimiters: ['[[', ']]'],
  data() {
    return {
      gasStations: [],
      fuels: [],
      managers: [],
      staffs: [],
      loading: false,
      viewing: false,
      saving: false,
      adding: false,
      next: null,
      previous: null,
      currentGas: {},
      newGas: {
        'name': "",
        'site_location': "",
        'site_manager': null,
        'site_staff': [],
        'fuels': [],
        'price_management_flexibility': 0.00
      }
    };
  },
  mounted() {
    this.fetchGasStations();
    this.fetchManagers();
    this.fetchStaffs();
    this.fetchFuels();
    this.nextPage();
  },
  methods: {
    reset: function () {
      this.newGas.name = "";
      this.newGas.site_location = "";
      this.newGas.site_manager = null;
      this.newGas.site_staff = [];
      this.newGas.fuels = [];
      this.newGas.sales = "";
      this.newGas.gasStations = null;
      this.newGas.volume_of_gasoline = "";
      this.newGas.price_management_flexibility = null;
      this.newGas.pricing_for_specific_type_of_fuel = null;
      // Object.keys(this.newGas).forEach(key => {
      //   this.newGas[key] = ""
      // })
    },
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
      this.viewing = true;
      let endpoint = `/api/v1/gas-station/${id}/`;
      if (this.currentGas) {
        axios.get(endpoint)
          .then((response) => {
            this.currentGas = response.data;
            this.viewing = false;
          })
          .catch((err) => {
            this.viewing = false;
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
    fetchFuels() {
      this.loading = true;
      let endpoint = `/api/v1/type-of-fuel/`;
      
      if (this.fuels) {
        axios.get(endpoint)
          .then((response) => {
            this.fuels = response.data;
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
    addGas() {
      this.saving = true;
      this.adding = true;
      if (this.newGas) {
        axios.post(`/api/v1/gas-station/`, this.newGas)
          .then(() => {
            this.reset();
            this.saving = false;
            this.fetchGasStations();
          })
          .catch((err) => {
            this.saving = false;
            console.log(err.response);
          })
      }
    },
    nextPage() {
      this.paging = true;
      let endpoint = `/api/v1/gas-station/`;

      if(this.next) {
        endpoint = this.next;
      } else if (this.previous) {
        endpoint = this.previous;
      }

      if (this.gasStations) {
        axios.get(endpoint)
          .then((response) => {
            this.gasStations = response.data;
            this.paging = false;

            if(response.data.next) {
              this.next = response.data.next;
            } else {
              this.next = null;
            }
            
            if (response.data.previous) {
              this.previous = response.data.previous;
            }

          })
          .catch((err) => {
            this.paging = false;
            console.log(err);
          })
      }
    },
    previousPage() {
      this.paging = true;
      let endpoint = `/api/v1/gas-station/`;

      if(this.previous) {
        endpoint = this.previous;
      } else if (this.next) {
        endpoint = this.next;
      }

      if (this.gasStations) {
        axios.get(endpoint)
          .then((response) => {
            this.gasStations = response.data;
            this.paging = false;

            if(response.data.next) {
              this.next = response.data.next;
            }
            
            if (response.data.previous) {
              this.previous = response.data.previous;
            } else {
              this.previous = null;
            }

          })
          .catch((err) => {
            this.paging = false;
            console.log(err);
          })
      }
    },
  },
  watch: {
    adding(val) {
      if (val) {
        setTimeout(() => {
          this.adding = false;
        }, 2000);
      }
    }
  }
})