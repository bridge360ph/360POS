Vue.config.devtools = true;
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

new Vue({
  el: '#pos-fuel',
  delimiters: ['[[', ']]'],
  data() {
    return {
      fuels: [],
      gasStations: [],
      apiEndpoint: `/api/v1/sales`,
      loading: false,
      viewing: false,
      saving: false,
      adding: false,
      paging: false,
      currentFuels: {},
      next: null,
      previous: null,
      count: null,
      newFuel: {
        'name': "",
      }
    };
  },
  mounted() {
    this.fetchFuels();
    this.nextPage();
  },
  methods: {
    reset: function () {
      Object.keys(this.newSales).forEach(key => {
        this.newSales[key] = null
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
    updateFuel() {
      this.saving = true;
      let endpoint = `/api/v1/type-of-fuel/${this.currentFuels.id}/`;
      if (this.currentFuels) {
        axios.put(endpoint, this.currentFuels)
          .then((response) => {
            this.saving = false;
            this.currentFuels = response.data;
            this.fetchFuels();

            $("#editFuelModal").modal("hide")
          })
          .catch((err) => {
            this.saving = false;
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
    addFuel() {
      this.saving = true;
      this.adding = true;
      if (this.newFuel) {
        axios.post(`/api/v1/type-of-fuel/`, this.newFuel)
          .then(() => {
            this.resetFuel();
            this.saving = false;

            this.fetchFuels();
            $("#fuelModal").modal("hide");
          })
          .catch((err) => {
            this.saving = false;
            console.log(err.response);
          })
      }
    },
    fetchFuel(id) {
      this.viewing = true;
      let endpoint = `/api/v1/type-of-fuel/${id}/`;
      if (this.currentFuels) {
        axios.get(endpoint)
          .then((response) => {
            this.currentFuels = response.data;
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
      let endpoint = `/api/v1/type-of-fuel/`;

      if(this.next) {
        endpoint = this.next;
      } else if (this.previous) {
        endpoint = this.previous;
      }

      if (this.fuels) {
        axios.get(endpoint)
          .then((response) => {
            this.fuels = response.data;
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
      let endpoint = `/api/v1/type-of-fuel/`;

      if(this.previous) {
        endpoint = this.previous;
      } else if (this.next) {
        endpoint = this.next;
      }

      if (this.fuels) {
        axios.get(endpoint)
          .then((response) => {
            this.fuels = response.data;
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