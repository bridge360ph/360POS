Vue.config.devtools = true;
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
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
      viewing: false,
      saving: false,
      currentProfile: {}
    };
  },
  mounted() {
    this.fetchLoginCredentials();
  },
  methods: {
    fetchLoginCredentials() {
      this.loading = true;
      let endpoint = "/api/v1/user/";
      if (this.profiles){
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
    },
    updateLogin() {
      this.saving = true;
      let endpoint = `/api/v1/user/${this.currentProfile.id}/`;
      if (this.profiles) {
        axios.put(endpoint, this.currentProfile)
          .then((response) => {
            this.saving = false;
            this.currentProfile = response.data;
            this.fetchLoginCredentials();

            $("#profileModal").modal("hide")
          })
          .catch((err) => {
            this.saving = false;
            console.log(err);
          })
      }
    },
    fetchLoginCredential(id) {
      this.viewing = true;
      let endpoint = `/api/v1/user/${id}/`;
      if (this.profiles){
        axios.get(endpoint)
        .then((response) => {
          this.currentProfile = response.data;
          this.viewing = false;
        })
        .catch(err => {
          this.viewing = false;
          console.log(err);
        })
      }
    },
  }
})