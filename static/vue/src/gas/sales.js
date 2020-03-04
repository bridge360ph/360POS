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
      },
      newFuel: {
        'name': "",
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
    resetFuel: function () {
      Object.keys(this.newFuel).forEach(key => {
        this.newFuel[key] = ""
      })
    },
    isNumber($event) {
      // console.log($event.keyCode); //keyCodes value
      let keyCode = ($event.keyCode ? $event.keyCode : $event.which);

      // only allow number and one dot
      if ((keyCode < 48 || keyCode > 57) && (keyCode !== 46)) { // 46 is dot
        $event.preventDefault();
      }

      // restrict to 2 decimal places
      // if (this.newSales != null && this.newSales.indexOf(".") > -1 && (this.newSales.split('.')[1].length > 1)) {
      //   $event.preventDefault();
      // }
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
      if (this.newSales) {
        axios.post(`/api/v1/sales/`, this.newSales)
          .then(() => {
            this.saving = false;
            this.reset();
            this.fetchSales();

            $("#salesModal").modal("hide")
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
    addTypeOfFuel() {
      this.saving = true;
      this.adding = true;
      if (this.newFuel) {
        axios.post(`/api/v1/type-of-fuel/`, this.newFuel)
          .then(() => {
            this.resetFuel();
            this.saving = false;

            this.fetchTypeOfFuel();
            $("#fuelModal").modal("hide");
          })
          .catch((err) => {
            this.saving = false;
            console.log(err.response);
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