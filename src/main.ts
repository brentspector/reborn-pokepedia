import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

import { IonicVue } from "@ionic/vue";
import { globalStore } from "./store/global";

/* Core CSS required for Ionic components to work properly */
import "@ionic/vue/css/core.css";

/* Basic CSS for apps built with Ionic */
import "@ionic/vue/css/normalize.css";
import "@ionic/vue/css/structure.css";
import "@ionic/vue/css/typography.css";

/* Optional CSS utils that can be commented out */
import "@ionic/vue/css/padding.css";
import "@ionic/vue/css/float-elements.css";
import "@ionic/vue/css/text-alignment.css";
import "@ionic/vue/css/text-transformation.css";
import "@ionic/vue/css/flex-utils.css";
import "@ionic/vue/css/display.css";

/* Theme variables */
import "./theme/variables.css";

const app = createApp(App)
  .use(IonicVue)
  .use(router);

router.isReady().then(() => {
  app.mount("#app");

  // Toggle dark mode
  const prefersLight = window.matchMedia("(prefers-color-scheme: light)");
  globalStore.setDarkModeAction(!prefersLight.matches);
  prefersLight.addEventListener("change", (mediaQuery) => {
    globalStore.setDarkModeAction(!mediaQuery.matches);
  });

  // Need to get path after app is mounted
  // Then redirect based on whatever path is
  // https://github.com/geeksilva97/geeksilva97.github.io
  const path = localStorage.getItem("path");
  if (path) {
    localStorage.removeItem("path");
    router.push(path);
  }
});
