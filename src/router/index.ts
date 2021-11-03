import { createRouter, createWebHistory } from "@ionic/vue-router";
import { RouteRecordRaw } from "vue-router";

const routes: Array<RouteRecordRaw> = [
  {
    path: "",
    redirect: "/locations",
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
  {
    path: "/details2",
    component: () => import("../views/Details2.vue")
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
