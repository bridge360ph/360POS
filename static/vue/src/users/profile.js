Vue.config.devtools = true;
// Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
// import { apiService } from "../common/api.service.js";

new Vue({
  el: '#pos-profile',
  delimiters: ['[[', ']]'],
  data() {
    return {
      profiles: [],
      gasStations: [],
      loading: false,
    };
  },
  mounted() {
    this.fetchLoginCredentials();
  },
  methods: {
    fetchLoginCredentials() {
      this.loading = true;
      let endpoint = "/api/v1/user/";
      axios.get(endpoint)
        .then((response) => {
          this.profiles = response.data;
          this.loading = false;
        })
        .catch(err => {
          this.loading = false;
          console.log(err);
        })
    }
  }
})