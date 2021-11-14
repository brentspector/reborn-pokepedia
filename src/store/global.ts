import { reactive } from "vue";

export const globalStore = {
  debug: process.env.NODE_ENV === "production" ? false : true,

  state: reactive({
    cardFormat: true,
    darkMode: true,
  }),

  setCardFormatAction(newValue: boolean): void {
    if (this.debug) {
      console.log("setCardFormatAction triggered with", newValue);
    }

    this.state.cardFormat = newValue;
  },

  setDarkModeAction(newValue: boolean): void {
    if (this.debug) {
      console.log("setDarkModeAction triggered with", newValue);
    }

    this.state.darkMode = newValue;
  },
};
