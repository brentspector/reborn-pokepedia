<template>
  <ion-page>
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
      <ion-item>
        <ion-label>Select a Point in Game</ion-label>
        <ion-select @ionChange="movesAvailable($event)">
          <ion-select-option
            v-for="(pnt, idx) in gamePoints"
            :key="idx"
            :value="pnt"
            >{{ pnt.name }}</ion-select-option
          >
        </ion-select>
      </ion-item>
      <ion-grid class="ion-margin-top ion-margin-bottom">
        <ion-row class="ion-align-items-start">
          <ion-col size="12" size-sm="4" class="ion-text-center">
            <ion-img :src="pokemonPath()"></ion-img>
            <ion-text color="light" class="bg-dark title-box">{{
              pokemonSel.name
            }}</ion-text>
          </ion-col>
          <ion-col size="12" size-sm>
            <ion-row>
              <ion-col
                size="6"
                size-sm
                v-for="(stat, i) in pokemonSel.stats"
                :key="i"
              >
                <ion-row
                  class="stat-box-header"
                  :class="headerColorClass(statOrder[i])"
                >
                  <ion-text>{{ statOrder[i] }}</ion-text>
                </ion-row>
                <ion-row class="ion-text-center stat-box bg-medium">
                  <ion-text>{{ stat }}</ion-text>
                </ion-row>
              </ion-col>
            </ion-row>
            <ion-row>
              <ion-col
                size-sm="3"
                class="ion-justify-content-center"
                style="display: flex"
                v-for="type in pokemonSel.types"
                :key="type"
              >
                <ion-img
                  class="type-icon"
                  :src="pokemonTypePath(type)"
                  :title="type"
                ></ion-img>
              </ion-col>
            </ion-row>
            <ion-row>
              <ion-col
                size="1"
                class="ion-text-center ion-align-items-center"
                style="display: flex"
              >
                <ion-text>Egg Moves</ion-text>
              </ion-col>
              <ion-col>
                <ion-row>
                  <ion-col
                    class="ion-margin ion-text-center egg-move"
                    style="flex-grow: 0"
                    v-for="move in pokemonSel.egg_moves"
                    :key="move"
                  >
                    <ion-label>{{ move }}</ion-label>
                  </ion-col>
                </ion-row>
              </ion-col>
            </ion-row>
            <ion-row>
              <ion-col
                size="2"
                size-xl="1"
                class="ion-text-center ion-align-items-center"
                style="display: flex"
              >
                <ion-text>Locations</ion-text>
              </ion-col>
              <ion-col>
                <ion-row
                  class="ion-margin ion-padding location-row"
                  v-for="(loc, idx) in pokemonSel.locations"
                  :key="idx"
                >
                  <ion-text
                    >{{ loc["location"] }} ({{ loc["point"] }} -
                    {{ loc["method"] }})</ion-text
                  >
                </ion-row>
              </ion-col>
            </ion-row>
          </ion-col>
        </ion-row>
        <ion-row>
          <ion-grid>
            <ion-row class="bg-dark">
              <ion-col size="2">Level</ion-col>
              <ion-col>Move</ion-col>
            </ion-row>
            <ion-row
              v-for="(moves, level) in pokemonSel.level_up_moves"
              :key="level"
              :class="{ selected: parseInt(level) &lt;= parseInt(ptLevel) }"
            >
              <ion-col size="2">
                <ion-text>{{ level }}</ion-text>
              </ion-col>
              <ion-col>
                <ion-row
                  v-for="(move, idx) in String(moves).split(',')"
                  :key="idx"
                >
                  <ion-text>{{ move }}</ion-text>
                </ion-row>
              </ion-col>
            </ion-row>
            <ion-row
              v-for="(move, idx) in pokemonSel.tm_tutor_moves"
              :key="idx"
              :class="{ selected: moveList.includes(move) }"
            >
              <ion-col size="2"><!-- Intentionally empty --></ion-col>
              <ion-col>
                <ion-text>{{ move }}</ion-text>
              </ion-col>
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
      switch (statName) {
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
  --background: rgba(var(--ion-color-primary-rgb), 0.14);
}
ion-menu.md ion-item.selected ion-icon {
  background: var(--ion-color-primary);
}
ion-menu.ios ion-item.selected ion-icon {
  background: var(--ion-color-primary);
}
ion-item.selected {
  background: var(--ion-color-primary);
}
ion-row.selected:nth-of-type(even) {
  background: var(--ion-color-success-shade);
}
ion-row.selected:nth-of-type(odd) {
  background: var(--ion-color-success-tint);
}
.bg-blue {
  background: var(--ion-color-secondary, blue);
  color: var(--ion-color-secondary-contrast, --ion-color-light);
}

.bg-red {
  background: var(--ion-color-danger, red);
  color: var(--ion-color-danger-contrast, --ion-color-light);
}

.bg-green {
  background: var(--ion-color-success, green);
  color: var(--ion-color-success-contrast, --ion-color-light);
}

.bg-yellow {
  background: var(--ion-color-warning, yellow);
  color: var(--ion-color-warning-contrast, --ion-color-light);
}

.bg-orange {
  background: var(--ion-color-fire, orange);
  color: var(--ion-color-fire-contrast, --ion-color-light);
}

.bg-purple {
  background: var(--ion-color-tertiary, purple);
  color: var(--ion-color-tertiary-contrast, --ion-color-light);
}

.bg-medium {
  background: var(--ion-color-medium, silver);
  color: var(--ion-color-medium-contrast, --ion-color-light);
}

.bg-dark {
  background: var(--ion-color-dark-shade, black);
  color: var(--ion-color-dark-contrast, --ion-color-light);
}

.title-box {
  display: block;
  width: 100%;
  padding: 0.7em 0;
  font-size: 24px;
}

.stat-box-header {
  border: 2px var(--ion-color-dark);
  border-style: solid none none none;
  border-radius: 0.5em 0.5em 0 0;
  font-style: italic;
  font-size: 1rem;
}

.stat-box {
  display: block;
  width: 100%;
  padding: 1em 0;
  font-size: 24px;
  border: ridge var(--ion-color-dark);
  border-width: 0 1px 1px 1px;
  border-radius: 0 0 0.5em 0.5em;
}

.type-icon {
  max-width: 10rem;
}

.egg-move {
  background: var(--ion-color-secondary-shade);
  border-radius: 0.5em;
  color: var(--ion-color-secondary-contrast);
}

.location-row {
  background: var(--ion-color-tertiary-shade);
  border-radius: 0.5em;
  color: var(--ion-color-tertiary-contrast);
}

body {
  background-color: #eeeeee;
}
</style>
