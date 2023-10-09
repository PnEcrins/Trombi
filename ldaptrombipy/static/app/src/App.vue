<template>
  <TrombiCal msg="Welcome to Your Vue.js App"/>

</template>

<script>
import TrombiCal from './components/TrombiCal.vue'

export default {
  name: 'App',
  components: {
    TrombiCal
  }
}
</script>

<style>
@import'~bootstrap/dist/css/bootstrap.css';
@import'../public/custom.css';
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  height: 100%;
}
body {
  background-color: #f1f0f0;

}

</style>
