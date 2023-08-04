<template>
  <Navbar />
  <router-view></router-view>
</template>

<style scoped></style>

<script>
import Navbar from "./components/Navbar.vue";
import Home from "./components/Home.vue";
import Product from "./components/Product.vue";
export default {
  components: {
    Navbar,
    Home,
    Product,
  },
};
</script>
