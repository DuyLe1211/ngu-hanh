import { createApp } from "vue";
import { createRouter, createWebHashHistory } from "vue-router";
import "./style.css";
import App from "./App.vue";
import Home from "./components/Home.vue";
import Product from "./components/Product.vue";

const app = createApp(App);

const routes = [
  { path: "/", component: Home },
  { path: "/app", component: Product },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

app.use(router);

app.mount("#app");
