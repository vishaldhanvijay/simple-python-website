var login_app = new Vue({
      el: '#login-app',
      data: {
        message: 'Hello Login!',
        username: '',
        password: ''
      },
      methods: {
        postLogin: function(event) {
            axios.post('/xhr-login', {
                username: this.username,
                password: this.password
            })
            .then(function (response) {
                console.log(response);
            })
            .catch(function (error) {
                console.log(error);
            });
        }
      }
    });

