Vue.config.devtools = true;
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

new Vue({
  el: '#pos-sales',
  delimiters: ['[[', ']]'],
  data() {
    return {
      sales: [],
      gasStations: [],
      typeOfFuel: [],
      loading: false,
      viewing: false,
      saving: false,
      adding: false,
      currentSales: {},
      newSales: {
        'type_of_fuel': null,
        'sales': 0.00,
        'price': 0.00,
        'gas_station_assigned': null,
        'dispensed_liter': 0.00,
      }
    };
  },
  mounted() {
    this.fetchTypeOfFuel();
    this.fetchSales();
  },
  methods: {
    reset: function () {
      Object.keys(this.newSales).forEach(key => {
        this.newSales[key] = ""
      })
    },
    updateSales() {
      this.saving = true;
      let endpoint = `/api/v1/sales/${this.currentSales.id}/`;
      if (this.currentSales) {
        axios.put(endpoint, this.currentSales)
          .then((response) => {
            this.saving = false;
            this.currentSales = response.data;

            $("#salesModal").modal("hide")
          })
          .catch((err) => {
            this.saving = false;
            console.log(err);
          })
      }
    },
    addSales() {
      this.saving = true;
      this.adding = true;
      if (this.newGas) {
        axios.post(`/api/v1/sales/`, this.newSales)
          .then(() => {
            this.reset();
            this.saving = false;
          })
          .catch((err) => {
            this.saving = false;
            console.log(err.response);
          })
      }
    },
    fetchTypeOfFuel() {
      this.loading = true;
      let endpoint = `/api/v1/type-of-fuel/`;
      if (this.typeOfFuel) {
        axios.get(endpoint)
          .then((response) => {
            this.typeOfFuel = response.data;
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
      }
    },
    fetchSales() {
      this.loading = true;
      let endpoint = `/api/v1/sales/`;
      if (this.sales) {
        axios.get(endpoint)
          .then((response) => {
            this.sales = response.data;
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
      }
    },
    fetchSale(id) {
      this.viewing = true;
      let endpoint = `/api/v1/sales/${id}/`;
      if (this.currentSales) {
        axios.get(endpoint)
          .then((response) => {
            this.currentSales = response.data;
            this.viewing = false;
          })
          .catch((err) => {
            this.viewing = false;
            console.log(err);
          })
      }
    },
  }
})