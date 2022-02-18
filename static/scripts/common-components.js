Vue.component('current-user-info', {
    props: ['user'],
    template: '<div> Welcome {{ user.lastname }}!</div>'
});

