<template>
  <ion-page style="background-image: url('assets/wallpaper/electric.jpg'), url('assets/pokemon/151.png');">
    <ion-content>
      <ion-item>
        <ion-label>Select a Pokemon</ion-label>
        <ion-select v-model="pokemonSel">
          <ion-select-option
            v-for="(pk, idx) in pokemonData"
            :key="idx"
            :value="pk"
          >
            {{ pk.name }}
          </ion-select-option>
        </ion-select>
      </ion-item>
      <ion-grid class="ion-margin-top ion-margin-bottom">
        <ion-row class="ion-align-items-start">
            <ion-col size="4" class ="ion-text-center">
              <ion-img :src="pokemonPath()"></ion-img>
              <ion-text color="light" class="bg-dark title-box font-15">{{ pokemonSel.name }}</ion-text>
            </ion-col>
            <ion-col size="8">
              <ion-row>
                <ion-col
                v-for="(stat, i) in pokemonSel.stats"
                :key="i"
                >
                  <ion-row class="stat-box-header" :class="headerColorClass(statOrder[i])">
                    <ion-text color="light">{{ statOrder[i] }}</ion-text>
                  </ion-row>
                  <ion-row class="ion-text-center stat-box bg-medium">
                    <ion-text>{{ stat }}</ion-text>
                  </ion-row>
                </ion-col>
              </ion-row>
              <ion-row>
                <ion-col
                 v-for="type in pokemonSel.types"
                 :key="type"
                >
                  <ion-img
                   class="type-icon"
                   :src="pokemonTypePath(type)"
                   :title="type"></ion-img>
                  <ion-text class="type-word">{{ type }}</ion-text>
                </ion-col>
              </ion-row>
              <ion-row>
                <ion-col
                 v-for="move in pokemonSel.egg_moves"
                 :key="move">
                  <ion-text>{{ move }}</ion-text>
                </ion-col>
              </ion-row>
            </ion-col>
        </ion-row>
        <ion-row>
          <ion-grid>
            <ion-row>
              <ion-col>Hello</ion-col>
              <ion-col>World</ion-col>
            </ion-row>
            <ion-row>
              <ion-col>Yup</ion-col>
              <ion-col>Ok</ion-col>
            </ion-row>
          </ion-grid>
        </ion-row>
      </ion-grid>
    </ion-content>
  </ion-page>
</template>
<script>
import {
  IonCol,
  IonContent,
  IonGrid,
  IonImg,
  IonItem,
  IonLabel,
  IonPage,
  IonRow,
  IonSelect,
  IonSelectOption,
  IonText,
} from "@ionic/vue";
import { defineComponent, ref } from "vue";
import { pokemonData10 } from "@/data/gen1_0";
import { pokemonData11 } from "@/data/gen1_1";
import { pokemonData12 } from "@/data/gen1_2";
import { pokemonData20 } from "@/data/gen2_0";
import { pokemonData21 } from "@/data/gen2_1";
import { pokemonData30 } from "@/data/gen3_0";
import { pokemonData31 } from "@/data/gen3_1";
import { pokemonData32 } from "@/data/gen3_2";
import { pokemonData40 } from "@/data/gen4_0";
import { pokemonData41 } from "@/data/gen4_1";
import { pokemonData50 } from "@/data/gen5_0";
import { pokemonData51 } from "@/data/gen5_1";
import { pokemonData52 } from "@/data/gen5_2";
import { pokemonData60 } from "@/data/gen6_0";
import { pokemonData61 } from "@/data/gen6_1";
import { pokemonData70 } from "@/data/gen7_0";
import { pokemonData71 } from "@/data/gen7_1";
import { gamePoints, gameLocations, statOrder } from "@/data/reborn";
import { tmLocations, tutorLocations } from "@/data/tm_locations";

export default defineComponent({
  components: {
    IonCol,
    IonContent,
    IonGrid,
    IonImg,
    IonItem,
    IonLabel,
    IonPage,
    IonRow,
    IonSelect,
    IonSelectOption,
    IonText,
  },
  setup() {
    const pokemonData = pokemonData10.concat(
      pokemonData11,
      pokemonData12,
      pokemonData20,
      pokemonData21,
      pokemonData30,
      pokemonData31,
      pokemonData32,
      pokemonData40,
      pokemonData41,
      pokemonData50,
      pokemonData51,
      pokemonData52,
      pokemonData60,
      pokemonData61,
      pokemonData70,
      pokemonData71
    );
    let moveList = [];
    let ptLevel = ref(0);
    const pokemonSel = ref(pokemonData[0]);
    const pokemonPath = () => {
      return (
        process.env.BASE_URL + "assets/pokemon/" + pokemonSel.value.no + ".png"
      );
    };
    const pokemonTypePath = (typeStr) => {
      return process.env.BASE_URL + "assets/types/" + typeStr + ".png";
    };
    const headerColorClass = (statName) => {
      switch(statName) {
        case "HP":
          return "bg-red";
        case "Atk":
          return "bg-orange";
        case "Def":
          return "bg-green";
        case "Spe":
          return "bg-yellow";
        case "Sp.A":
          return "bg-blue";
        case "Sp.D":
          return "bg-purple";
      }
    };
    const movesAvailable = (event) => {
      ptLevel.value = event.target.value.level;

      // Clear the reactive array
      moveList.splice(0, moveList.length);

      // Get all points up to this point
      let pointNames = gamePoints.map((e) => e.name);
      let cumulativePoints = pointNames.slice(
        0,
        pointNames.indexOf(event.target.value.name) + 1
      );

      // Filter for moves and then add them to the reactive array
      tmLocations
        .filter((mv) => cumulativePoints.includes(mv.point))
        .forEach((mv) => moveList.push(mv.name));
      tutorLocations
        .filter((mv) => cumulativePoints.includes(mv.point))
        .forEach((mv) => moveList.push(mv.name));
    };
    return {
      moveList,
      ptLevel,
      pokemonSel,
      pokemonData,
      gamePoints,
      gameLocations,
      statOrder,
      pokemonPath,
      pokemonTypePath,
      headerColorClass,
      movesAvailable,
    };
  },
});
</script>
<style scoped>
ion-menu.md ion-item.selected {
  --background: rgba(var(--ion-color-success-rgb), 0.14);
}
ion-menu.md ion-item.selected ion-icon {
  background: var(--ion-color-success);
}
ion-menu.ios ion-item.selected ion-icon {
  background: var(--ion-color-success);
}
ion-item.selected {
  --background: var(--ion-color-success);
}

.bg-blue {
  background: blue;
}

.bg-red {
  background: red;
}

.bg-green {
  background: green;
}

.bg-yellow {
  background: yellow;
}

.bg-orange {
  background: orange;
}

.bg-purple {
  background: purple;
}

.bg-medium {
  background: var(--ion-color-medium, silver);
}

.bg-dark {
  background: var(--ion-color-dark, black);
}

@media (max-width: 576px) {
  .title-box {
    display: block;
    width: 100%;
    padding: 0.4em 0;
    font-size: 14px;
  }

  .stat-box-header {
    border: 1px;
    border-style: solid none none none;
    font-style: italic;
    font-size: 0.8em;
  }

  .stat-box-header > ion-text {
    mix-blend-mode: difference;
  }

  .stat-box {
    display: block;
    width: 100%;
    padding: 0.5em 1em;
    font-size: 14px;
    border: 1px;
    border-style: inset;
  }

  .type-icon {
    display: none;
  }
}

@media (min-width: 576px) {
  .title-box {
    display: block;
    width: 100%;
    padding: 0.7em 0;
    font-size: 24px;
  }

  .stat-box-header {
    border: 1px;
    border-style: solid none none none;
    font-style: italic;
    font-size: 1rem;
  }

  .stat-box-header > ion-text {
    mix-blend-mode: difference;
  }

  .stat-box {
    display: block;
    width: 100%;
    padding: 1em 0;
    font-size: 24px;
    border: 1px;
    border-style: inset;
  }

  .type-word {
    display: none;
  }

  .type-icon {
    width: 50%;
  }
}
body {
  background-color: #eeeeee;
}
</style>
<!-- https://css-tricks.com/rem-global-em-local/ -->