Vue.config.devtools = true;
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

new Vue({
  el: '#pos-gas',
  delimiters: ['[[', ']]'],
  data() {
    return {
      gasStations: [],
      loading: false,
      viewing: false,
      saving: false,
      currentGas: {}
    };
  },
  mounted() {
    this.fetchGasStation();
  },
  methods: {
    fetchGasStation() {
        this.loading = true;
        let endpoint = `/api/v1/gas-station/`;
        if (this.gasStations){
          axios.get(endpoint)
          .then((response) => {
            this.gasStations = response.data;
            console.log(this.gasStations);
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
        }
      },
  }
})