new Vue({
    el: '#app',
    data () {
      return {
        dialog: false,
        nav: [
          {
            icon: 'home',
            text: 'Home',
            title: 'Back to Home page',
            active: true
          },
          {
            icon: 'info',
            text: 'About',
            title: 'About this demo',
            active: false
          },
          {
            icon: 'assignment_turned_in',
            text: 'Todos',
            title: 'Some stuff that needs doing',
            active: false
          },
          {
            icon: 'email',
            text: 'Contact',
            title: 'Our Contact info',
            active: false
          }
        ]
      }
    }
  })