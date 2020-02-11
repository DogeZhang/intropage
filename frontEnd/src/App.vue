<template>
  <div id="app">
    <p class="title">{{msg}}</p>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      msg: 'Deep Learning-Based Ship Recognition System'
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #ddd;
  padding-top: 25px;
  height: 100%;
}
.title {
  text-align: center;
  font-size: 42px;
}
body {
  height: 100%;
  margin: 0;
  padding: 0;
  background: url('./assets/images/background2.jpg');
  /* background-color: rgb(86, 89, 94); */
  background-repeat:  no-repeat;
  background-size: 100% 120%;
}
</style>
