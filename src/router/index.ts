import { createRouter, createWebHistory } from "@ionic/vue-router";
import { RouteRecordRaw } from "vue-router";

const routes: Array<RouteRecordRaw> = [
  {
    path: "",
    component: () => import("../views/Welcome.vue"),
  },
  {
    path: "/points",
    component: () => import("../views/Points.vue"),
  },
  {
    path: "/locations",
    component: () => import("../views/Locations.vue"),
  },
  {
    path: "/details",
    component: () => import("../views/Details.vue"),
  },
  {
    path: "/details/:id",
    component: () => import("../views/Details.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
