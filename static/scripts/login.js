const Login = { template: '<div>Login</div>' }
const Register = { template: '<div>Register</div>' }

const routes = [
  { path: '/login-form', component: Login },
  { path: '/registration-form', component: Register },
];

const router = VueRouter.createRouter({
  history: VueRouter.createWebHashHistory(),
  routes,
});


var login_app = Vue.createApp({
      data(){
        return {
            message: '',
            username: '',
            password: '',
            hasError: false,
            isSuccess: false,
            isFailed: false
        }
      },
      methods: {
        postLogin: function(event) {
            axios.post('/login', {
                username: this.username,
                password: this.password
            })
            .then(response => {
                if (response.data.login_success) {
                    this.isSuccess = true;
                    this.isFailed = false;
                    this.hasError = false;
                    this.username = '*******'
                    this.password = '***********'
                    this.message = 'Login success! Please proceed to the <a href="/restricted">RESTRICTED AREA</a> or <a href="/admin">ADMIN AREA</a>.'
                } else {
                    this.isFailed = true;
                    this.isSuccess = false;
                    this.hasError = false;
                    this.username = ''
                    this.password = ''
                    this.message = 'Login failed! Access denied.'
                }
            })
            .catch(error => {
                this.message = error;
                this.hasError = true;
                this.isFailed = false;
                this.isSuccess = false;
                console.log(error);
            });
        }
      },
      computed: {
          messageClass: function () {
            return {
              'alert-success': this.isSuccess,
              'alert-warning': this.hasError,
              'alert-danger': this.isFailed
            }
          }
      }
    });

login_app.use(router)
login_app.mount('#login-app')
