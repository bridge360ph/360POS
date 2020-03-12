Vue.config.devtools = true;
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

new Vue({
  el: '#pos-price',
  delimiters: ['[[', ']]'],
  data() {
    return {
      prices: [],
      gasolineStations: [],
      loading: false,
      viewing: false,
      saving: false,
      adding: false,
      paging: false,
      currentPrice: {},
      next: null,
      previous: null,
      newPrice: {
        'name': null,
        'price': 0.00,
        'gas_station_assigned': null,
      },
    };
  },
  mounted() {
    this.fetchPrices();
    this.fetchGasolineStations();
    this.nextPage();
  },
  methods: {
    reset: function () {
      Object.keys(this.newPrice).forEach(key => {
        this.newPrice[key] = ""
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
      // if (this.newPrice != null && this.newPrice.indexOf(".") > -1 && (this.newPrice.split('.')[1].length > 1)) {
      //   $event.preventDefault();
      // }
    },
    updatePrice() {
      this.saving = true;
      let endpoint = `/api/v1/fuel-prices/${this.currentPrice.id}/`;
      if (this.currentPrice) {
        axios.put(endpoint, this.currentPrice)
          .then((response) => {
            this.saving = false;
            this.currentPrice = response.data;

            this.fetchPrices();
            $("#editPriceModal").modal("hide")
          })
          .catch((err) => {
            this.saving = false;
            console.log(err);
          })
      }
    },
    addPrice() {
      this.saving = true;
      this.adding = true;
      if (this.newPrice) {
        axios.post(`/api/v1/fuel-prices/`, this.newPrice)
          .then(() => {
            this.saving = false;
            this.reset();
            this.fetchPrices();
            $("#pricesModal").modal("hide")

          })
          .catch((err) => {
            this.saving = false;
            console.log(err.response);
          })
      }
    },
    fetchGasolineStations() {
      this.loading = true;
      let endpoint = `/api/v1/gasoline-stations/`;
      if (this.gasolineStations) {
        axios.get(endpoint)
          .then((response) => {
            this.gasolineStations = response.data;
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
      }
    },
    fetchPrices() {
      this.loading = true;
      let endpoint = `/api/v1/fuel-prices/`;
      if (this.prices) {
        axios.get(endpoint)
          .then((response) => {
            this.prices = response.data;
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
      }
    },
    fetchPrice(id) {
      this.viewing = true;
      let endpoint = `/api/v1/fuel-prices/${id}/`;
      if (this.currentPrice) {
        axios.get(endpoint)
          .then((response) => {
            this.currentPrice = response.data;
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
      let endpoint = `/api/v1/fuel-prices/`;

      if(this.next) {
        endpoint = this.next;
      } else if (this.previous) {
        endpoint = this.previous;
      }

      if (this.prices) {
        axios.get(endpoint)
          .then((response) => {
            this.prices = response.data;
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
      let endpoint = `/api/v1/fuel-prices/`;

      if(this.previous) {
        endpoint = this.previous;
      } else if (this.next) {
        endpoint = this.next;
      }

      if (this.prices) {
        axios.get(endpoint)
          .then((response) => {
            this.prices = response.data;
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