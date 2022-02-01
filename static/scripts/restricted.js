Vue.component('current-user-info', {
    props: ['user'],
    template: '<div> Welcome {{ user.lastname }}!</div>'
});

var restricted_app = new Vue({
      el: '#restricted-app',
      data: {
        user: {},
        logged_in: false
      },
      mounted () {
        axios.get('/user/current')
            .then(response => {
                console.log(response)
                this.user = response.data
                this.logged_in = true;
            })
            .catch(error => {
                console.log(error);
            });
        }
      });