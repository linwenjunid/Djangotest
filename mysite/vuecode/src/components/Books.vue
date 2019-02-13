<template>
  <div id="Books">
    <h1>书单{{count}}</h1>
    <ol>
    <li v-for="book in books" >
      {{ book}}
    </li>
    <li>
    <button v-on:click="go(previous)">上一页</button>
    <button v-on:click="go(next)">下一页</button>
    </li>
    </ol>
  </div>
</template>

<script>
export default {
  name: 'Books',
  data () {
    return {
      books: null,
      count:0,
      next:0,
      previous:0,
    }
  },
  methods: {
    go:function(url) {
      this.axios
      .get(url)
      .then(response => (
        this.books = response.data.results,
        this.count = response.data.count,
        this.next = response.data.next,
        this.previous = response.data.previous
      ))
    }
  },
  mounted () {
    this.axios
      .get('http://127.0.0.1:8000/books/api/books/')
      .then(response => (
        this.books = response.data.results,
        this.count = response.data.count,
        this.next = response.data.next,
        this.previous = response.data.previous
      ))
  }
}
</script>

<style scoped>

</style>
