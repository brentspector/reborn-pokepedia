<template>
  <ion-page>
    <ion-content>
      <ion-item
        v-if="!isModal"
        @click="setSearchListOpen('pokemon')"
        lines="none"
        detail="true"
        class="hydrated dropdown"
      >
        <ion-icon
          slot="start"
          :ios="searchOutline"
          :md="searchSharp"
        ></ion-icon>
        <ion-label>{{ pokemonSel.name }}</ion-label>
      </ion-item>
      <ion-item
        v-if="!isModal"
        @click="setSearchListOpen('point')"
        lines="none"
        detail="true"
        class="hydrated dropdown"
      >
        <ion-icon
          slot="start"
          :ios="searchOutline"
          :md="searchSharp"
        ></ion-icon>
        <ion-label>{{ pointDropdownLabel() }}</ion-label>
      </ion-item>
      <ion-grid class="ion-margin-top ion-margin-bottom">
        <ion-row class="ion-align-items-start">
          <ion-col
            size-xs="12"
            :size-sm="isModal ? 12 : 4"
            size-lg="4"
            class="ion-text-center"
          >
            <ion-img :src="pokemonPath()"></ion-img>
            <ion-text color="light" class="bg-dark title-box">{{
              pokemonSel.name
            }}</ion-text>
          </ion-col>
          <ion-col size-xs="12" size-sm>
            <ion-row>
              <ion-col
                size-xs="6"
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
                :size-xl="isModal ? 2 : 1"
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
                    v-for="move in pokemonSel.eggMoves"
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
                :size-xl="isModal ? 2 : 1"
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
        <ion-item
          v-if="isModal"
          @click="setSearchListOpen('point')"
          lines="none"
          detail="true"
          class="hydrated dropdown"
        >
          <ion-icon
            slot="start"
            :ios="searchOutline"
            :md="searchSharp"
          ></ion-icon>
          <ion-label>{{ pointDropdownLabel() }}</ion-label>
        </ion-item>
        <ion-row>
          <ion-grid>
            <ion-row class="bg-dark">
              <ion-col size="2">Level</ion-col>
              <ion-col>Move</ion-col>
            </ion-row>
            <ion-row
              v-for="(moves, level) in pokemonSel.levelUpMoves"
              :key="level"
              :class="isMoveSelected(level)"
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
              v-for="(move, idx) in pokemonSel.tmTutorMoves"
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
      <ion-fab v-if="isModal" vertical="bottom" horizontal="end" slot="fixed">
        <ion-fab-button
          activated="true"
          @click="modalCallbackWrapper"
        ></ion-fab-button>
      </ion-fab>
    </ion-content>
  </ion-page>
</template>
<script lang="ts">
import { searchOutline, searchSharp } from "ionicons/icons";
import {
  IonCol,
  IonContent,
  IonFab,
  IonFabButton,
  IonGrid,
  IonIcon,
  IonImg,
  IonItem,
  IonLabel,
  IonPage,
  IonRow,
  IonText,
  modalController,
  ModalOptions,
} from "@ionic/vue";
import { defineComponent, onMounted, ref } from "vue";
import { useRoute } from "vue-router";
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
import { gamePoints, statOrder } from "@/data/reborn";
import { tmLocations, tutorLocations } from "@/data/tm_locations";
import { Pokemon } from "@/interfaces/pokemon_interfaces";
import SearchList from "@/views/SearchList.vue";

export default defineComponent({
  components: {
    IonCol,
    IonContent,
    IonFab,
    IonFabButton,
    IonGrid,
    IonIcon,
    IonImg,
    IonItem,
    IonLabel,
    IonPage,
    IonRow,
    IonText,
  },
  props: {
    pk: {
      type: Object as () => Pokemon,
      required: false,
    },
    point: {
      type: Object as () => typeof gamePoints[0],
      required: false,
    },
    modalCallback: {
      type: Function as () => void,
      required: false,
    },
  },
  setup(props) {
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
    const route = useRoute();
    const moveList: string[] = [];
    const pointInGame = ref({ name: "Select A Point In Game", level: "0" });
    const isModal = ref(false);
    const pokemonSel = ref(pokemonData[0]);
    let modal: HTMLIonModalElement;
    // Typescript doesn't like that modalCallback is possibly undefined
    // thus we can't directly call it via @click nor invoke it as a lambda
    // so we do this little song and dance to let typescript know that
    // yes, it is in fact callable, please stop failing
    const modalCallbackWrapper = () => {
      if (typeof props.modalCallback == "function") {
        const mcb = props.modalCallback as Function;
        mcb();
      }
    };
    const pokemonPath = () => {
      return (
        process.env.BASE_URL + "assets/pokemon/" + pokemonSel.value.no + ".png"
      );
    };
    const pokemonTypePath = (typeStr: string) => {
      return process.env.BASE_URL + "assets/types/" + typeStr + ".png";
    };
    const headerColorClass = (statName: string) => {
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
    const isMoveSelected = (level: number) => {
      // Using the unary operator (+) to guarantee string is a number
      // Otherwise ends up using string comparision such that 11 < 4
      return +level < +pointInGame.value.level ? "selected" : "";
    };
    const movesAvailable = (point: typeof gamePoints[0] | undefined) => {
      if (point) {
        pointInGame.value = point;

        // Clear the reactive array
        moveList.splice(0, moveList.length);

        // Get all points up to this point
        const pointNames = gamePoints.map((e) => e.name);
        const cumulativePoints = pointNames.slice(
          0,
          pointNames.indexOf(point.name) + 1
        );

        // Filter for moves and then add them to the reactive array
        tmLocations
          .filter((mv) => cumulativePoints.includes(mv.point))
          .forEach((mv) => moveList.push(mv.name));
        tutorLocations
          .filter((mv) => cumulativePoints.includes(mv.point))
          .forEach((mv) => moveList.push(mv.name));
      }
      if (modal) {
        modal.dismiss();
      }
    };
    const pokemonSearchListHandler = (pk: Pokemon) => {
      if (pk) {
        pokemonSel.value = pk;
      }
      modal.dismiss();
    };
    const setSearchListOpen = async (mode: string) => {
      let settings: ModalOptions;
      if (mode === "pokemon") {
        settings = {
          component: SearchList,
          componentProps: {
            content: pokemonData,
            contentKey: "name",
            label: "Select A Pokemon",
            modalCallback: pokemonSearchListHandler,
          },
        };
      } else if (mode === "point") {
        settings = {
          component: SearchList,
          componentProps: {
            content: gamePoints,
            contentKey: "name",
            label: "Select A Point In Game",
            modalCallback: movesAvailable,
          },
        };
      } else {
        throw mode + " is not a supported search list!";
      }
      modal = await modalController.create(settings);
      return modal.present();
    };

    const getIdNumberFromRoute = (id: string | string[]): number => {
      let numId = 0;
      if (!id) {
        return numId;
      }
      if (typeof id === "string") {
        numId = parseInt(id);
      } else if (id.length > 0) {
        numId = parseInt(id[0]);
      }
      if (numId > 1) {
        return numId;
      } else {
        return 1;
      }
    };

    const determinePokemonSel = (
      id: string | string[],
      pk: Pokemon | undefined
    ): void => {
      if (pk) {
        isModal.value = true;
        pokemonSel.value = pk;
      } else {
        isModal.value = false;
        pokemonSel.value = pokemonData.filter(
          (pk) => pk.no == getIdNumberFromRoute(id)
        )[0];
        if (!pokemonSel.value) {
          pokemonSel.value = pokemonData[0];
        }
      }

      // Update moves available based on point provided
      movesAvailable(props.point);
    };

    const pointDropdownLabel = () => {
      return pointInGame.value.name;
    };

    onMounted(() => determinePokemonSel(route.params.id, props.pk));

    return {
      searchOutline,
      searchSharp,
      isModal,
      moveList,
      pointInGame,
      pokemonSel,
      pokemonData,
      gamePoints,
      statOrder,
      modalCallbackWrapper,
      pokemonPath,
      pokemonTypePath,
      headerColorClass,
      isMoveSelected,
      pointDropdownLabel,
      movesAvailable,
      setSearchListOpen,
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
.dropdown:hover {
  --background: rgba(var(--ion-color-primary-rgb), 0.14);
}
</style>

<!-- GLOBAL STYLES
    AVOID USING THIS -->
<style>
@media screen and (min-width: 768px) {
  .details-modal {
    --width: 80%;
    --height: 80%;
  }
}
</style>