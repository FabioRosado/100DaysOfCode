var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!',
    seen: true,
    todos: [
      { text: 'Learn Javascript' },
      { text: 'Learn Vue' },
      { text: 'Build something awesome' }
    ]
  },
  methods: {
    reverseMessage: function () {
      this.message = this.message.split('').reverse().join('');
    },
    show: function () {
      if (this.seen == false) {
        this.seen = true;
      } else {
        this.seen = false;
      }
    }
  }
});

app.message = 'I have changed the data!';
app.seen = false;
app.todos.push({ text: 'New item'});