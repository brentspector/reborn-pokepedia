<template>
  <ion-page>
    <ion-content fullscreen>
      <ion-item
        @click="setSearchListOpen()"
        lines="none"
        detail="true"
        class="hydrated dropdown"
      >
        <ion-icon
          slot="start"
          :ios="searchOutline"
          :md="searchSharp"
        ></ion-icon>
        <ion-label>{{ dropdownLabel() }}</ion-label>
      </ion-item>
      <ion-list v-if="!globalStore.state.cardFormat">
        <ion-item
          v-for="pk in pokemonAtPoint"
          :key="pk.no"
          @click="setDetailsOpen(pk)"
        >
          <ion-thumbnail slot="start">
            <img :src="pokemonPath(pk.no)" />
          </ion-thumbnail>
          <ion-label class="title">
            <ion-text>{{ pk.name }}</ion-text>
            <ion-thumbnail class="ion-margin-start ion-margin-top">
              <img
                v-for="type in pk.types"
                :key="type"
                :src="pokemonTypePath(type)"
                :title="type"
              />
            </ion-thumbnail>
          </ion-label>
          <ion-col size-lg="9">
            <ion-row class="method">
              <ion-text>
                {{ pokemonPoint(pk).location }}
              </ion-text>
            </ion-row>
            <ion-row class="point">
              <ion-text>
                {{ pokemonPoint(pk).method }}
              </ion-text>
            </ion-row>
          </ion-col>
        </ion-item>
      </ion-list>
      <ion-grid v-if="globalStore.state.cardFormat">
        <ion-row>
          <ion-col
            size="6"
            size-md="4"
            size-lg="3"
            size-xl="2.4"
            v-for="pk in pokemonAtPoint"
            :key="pk.no"
            @click="setDetailsOpen(pk)"
          >
            <ion-card>
              <img :src="pokemonPath(pk.no)" />
              <ion-card-header>
                <ion-card-subtitle>
                  <ion-row class="ion-justify-content-around">
                    <ion-thumbnail
                      class="ion-margin-start ion-margin-top"
                      v-for="type in pk.types"
                      :key="type"
                    >
                      <img :src="pokemonTypePath(type)" :title="type" />
                    </ion-thumbnail>
                  </ion-row>
                </ion-card-subtitle>
                <ion-card-title class="ion-text-center">{{
                  pk.name
                }}</ion-card-title>
              </ion-card-header>
              <ion-card-content class="ion-text-center">
                {{ pokemonPoint(pk).location }} - {{ pokemonPoint(pk).method }}
              </ion-card-content>
            </ion-card>
          </ion-col>
        </ion-row>
      </ion-grid>
    </ion-content>
  </ion-page>
</template>

<script lang="ts">
import { searchOutline, searchSharp } from "ionicons/icons";
import {
  IonCard,
  IonCardContent,
  IonCardHeader,
  IonCardSubtitle,
  IonCardTitle,
  IonCol,
  IonContent,
  IonGrid,
  IonIcon,
  IonItem,
  IonLabel,
  IonList,
  IonPage,
  IonRow,
  IonText,
  IonThumbnail,
  modalController,
} from "@ionic/vue";
import { defineComponent, ref, reactive } from "vue";
import { globalStore } from "@/store/global";
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
import { gamePoints } from "@/data/reborn";
import { Pokemon } from "@/interfaces/pokemon_interfaces";
import Details from "@/views/Details.vue";
import SearchList from "@/views/SearchList.vue";

export default defineComponent({
  components: {
    IonCard,
    IonCardContent,
    IonCardHeader,
    IonCardSubtitle,
    IonCardTitle,
    IonCol,
    IonContent,
    IonGrid,
    IonIcon,
    IonItem,
    IonLabel,
    IonList,
    IonPage,
    IonRow,
    IonText,
    IonThumbnail,
  },
  setup() {
    const pokemonAtPoint: Pokemon[] = reactive([]);
    const pointInGame = ref(gamePoints[0]);
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
    const pokemonAvailable = (point: typeof pointInGame.value) => {
      if (point) {
        // Clear the reactive array
        pokemonAtPoint.splice(0, pokemonAtPoint.length);

        //Apply point in game
        pointInGame.value = point;

        // Filter for pokemon and then add them to the reactive array
        pokemonData
          // eslint-disable-next-line
          .filter((pk, idx, arr) => pokemonPoint(pk))
          .forEach((e) => pokemonAtPoint.push(e));
      }
      modalController.dismiss();
    };

    const setDetailsOpen = async (pk: Pokemon) => {
      const modal = await modalController.create({
        component: Details,
        componentProps: {
          pk: pk,
          point: pointInGame.value,
          modalCallback: modalController.dismiss,
        },
        cssClass: "details-modal",
      });
      return modal.present();
    };
    const setSearchListOpen = async () => {
      const modal = await modalController.create({
        component: SearchList,
        componentProps: {
          content: gamePoints,
          contentKey: "name",
          label: "Select A Point In Game",
          modalCallback: pokemonAvailable,
        },
      });
      return modal.present();
    };
    const pokemonPath = (pkId: number) => {
      return process.env.BASE_URL + "assets/pokemon/" + pkId + ".png";
    };
    const pokemonTypePath = (typeStr: string) => {
      return process.env.BASE_URL + "assets/types/" + typeStr + ".png";
    };
    const pokemonPoint = (pk: Pokemon) => {
      return pk.locations.filter(
        (loc) => loc.point === pointInGame.value.name
      )[0];
    };
    const dropdownLabel = () => {
      if (pokemonAtPoint.length > 0) {
        return pointInGame.value.name;
      } else {
        return "Select A Point In Game";
      }
    };

    return {
      searchOutline,
      searchSharp,
      globalStore,
      pokemonAtPoint,
      pokemonPath,
      pokemonTypePath,
      pokemonPoint,
      dropdownLabel,
      setDetailsOpen,
      setSearchListOpen,
    };
  },
});
</script>
<style scoped>
ion-list > ion-item {
  --background: rgba(var(--ion-color-primary-rgb), 0.05);
  font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
}

@media screen and (max-width: 768px) {
  .title {
    font-weight: bolder;
    font-style: italic;
    padding: 2px;
    font-size: 1.1em;
  }
  .method {
    font-size: 1.05em;
    font-weight: bold;
    margin: 0px;
    color: var(--ion-color-medium, --ion-color-dark);
  }

  .point {
    font-size: 0.95em;
    font-weight: 300;
    font-style: italic;
    margin: 0px;
    color: var(--ion-color-medium, --ion-color-dark);
  }
}

@media screen and (min-width: 768px) {
  .title {
    font-weight: bolder;
    font-style: italic;
    padding: 2px;
    font-size: 1.25em;
  }

  .method {
    font-size: 1.15em;
    font-weight: bold;
    margin: 0px;
    color: var(--ion-color-medium, --ion-color-dark);
  }

  .point {
    font-size: 1em;
    font-weight: 300;
    font-style: italic;
    margin: 0px;
    color: var(--ion-color-medium, --ion-color-dark);
  }
}

body {
  background-color: #eeeeee;
}

.dropdown:hover {
  --background: rgba(var(--ion-color-primary-rgb), 0.14);
}
</style>