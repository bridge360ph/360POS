Vue.config.devtools = true;
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

new Vue({
  el: '#pos-transactions',
  delimiters: ['[[', ']]'],
  data() {
    return {
      transactions: [],
      gasStations: [],
      apiEndpoint: `/api/v1/transactions/`,
      fuelPrices: [],
      loading: false,
      viewing: false,
      saving: false,
      adding: false,
      paging: false,
      currentTransactions: {},
      next: null,
      previous: null,
      count: null,
      newTransactions: {
        'fuel': null,
        'sales': 0.00,
        'gas_station_assigned': null,
        'dispensed_liter': 0.00,
      },
    };
  },
  mounted() {
    this.fetchTransactions();
    this.fetchGasStations();
    this.fetchFuelPrices();
    this.nextPage();
  },
  methods: {
    reset: function () {
      this.newTransactions.fuel = null;
      this.newTransactions.sales = 0.00;
      this.newTransactions.gas_station_assigned = null;
      // Object.keys(this.newTransactions).forEach(key => {
      //   this.newTransactions[key] = null
      // })
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
    updateTransaction() {
      this.saving = true;
      let endpoint = `/api/v1/transactions/${this.currentTransactions.id}/`;
      if (this.currentTransactions) {
        axios.put(endpoint, this.currentTransactions)
          .then((response) => {
            this.saving = false;
            this.currentTransactions = response.data;
            this.fetchTransactions();

            $("#editSalesModal").modal("hide")
          })
          .catch((err) => {
            this.saving = false;
            console.log(err);
          })
      }
    },
    addTransactions() {
      this.saving = true;
      this.adding = true;
      if (this.newTransactions) {
        axios.post(`/api/v1/transactions/`, this.newTransactions)
          .then(() => {
            this.saving = false;
            this.reset();
            
            $("#salesModal").modal("hide")
            this.fetchTransactions();
          })
          .catch((err) => {
            this.saving = false;
            console.log(err.response);
          })
      }
    },
    fetchFuelPrices() {
      this.loading = true;
      let endpoint = `/api/v1/fuel-prices/`;
      
      if (this.fuelPrices) {
        axios.get(endpoint)
          .then((response) => {
            this.fuelPrices = response.data;
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
      }
    },
    fetchGasStations() {
      this.loading = true;
      let endpoint = `/api/v1/gasoline-stations/`;
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
    addfuelPrices() {
      this.saving = true;
      this.adding = true;
      if (this.newFuel) {
        axios.post(`/api/v1/fuel-prices/`, this.newFuel)
          .then(() => {
            this.resetFuel();
            this.saving = false;

            this.fetchfuelPrices();
            $("#fuelModal").modal("hide");
          })
          .catch((err) => {
            this.saving = false;
            console.log(err.response);
          })
      }
    },
    fetchTransactions() {
      this.loading = true;
      let endpoint = this.apiEndpoint;

      if (this.transactions) {
        axios.get(endpoint)
          .then((response) => {
            this.transactions = response.data;
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
      }
    },
    fetchTransaction(id) {
      this.viewing = true;
      let endpoint = `/api/v1/transactions/${id}/`;
      if (this.currentTransactions) {
        axios.get(endpoint)
          .then((response) => {
            this.currentTransactions = response.data;
            this.viewing = false;
          })
          .catch((err) => {
            this.viewing = false;
            console.log(err);
          })
      }
    },
    nextPage() {
      this.paging = true;
      let endpoint = `/api/v1/transactions/`;

      if(this.next) {
        endpoint = this.next;
      } else if (this.previous) {
        endpoint = this.previous;
      }

      if (this.transactions) {
        axios.get(endpoint)
          .then((response) => {
            this.transactions = response.data;
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
      let endpoint = `/api/v1/transactions/`;

      if(this.previous) {
        endpoint = this.previous;
      } else if (this.next) {
        endpoint = this.next;
      }

      if (this.transactions) {
        axios.get(endpoint)
          .then((response) => {
            this.transactions = response.data;
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
  }
})