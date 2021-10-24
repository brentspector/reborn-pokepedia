import {
  navigateOutline,
  navigateSharp,
  pieChartOutline,
  pieChartSharp,
  ribbonOutline,
  ribbonSharp,
} from "ionicons/icons";

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
