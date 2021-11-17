import {
  gridOutline,
  gridSharp,
  moonOutline,
  moonSharp,
  navigateOutline,
  navigateSharp,
  pieChartOutline,
  pieChartSharp,
  ribbonOutline,
  ribbonSharp,
} from "ionicons/icons";
import { globalStore } from "@/store/global";

export const appPages = [
  {
    title: "Game Points",
    url: "/points",
    iosIcon: ribbonOutline,
    mdIcon: ribbonSharp,
  },
  {
    title: "Game Locations",
    url: "/locations",
    iosIcon: navigateOutline,
    mdIcon: navigateSharp,
  },
  {
    title: "Pokemon Details",
    url: "/details",
    iosIcon: pieChartOutline,
    mdIcon: pieChartSharp,
  },
];

export const customizationButtons = [
  {
    title: "Card View",
    iosIcon: gridOutline,
    mdIcon: gridSharp,
    method: (event: Event): void =>
      globalStore.setCardFormatAction(
        (event.target as HTMLIonToggleElement).checked
      ),
    stateValue: (): boolean => globalStore.state.cardFormat,
  },
  {
    title: "Dark Mode",
    iosIcon: moonOutline,
    mdIcon: moonSharp,
    method: (event: Event): void =>
      globalStore.setDarkModeAction(
        (event.target as HTMLIonToggleElement).checked
      ),
    stateValue: (): boolean => globalStore.state.darkMode,
  },
];
