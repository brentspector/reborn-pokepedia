<template>
  <ion-page>
    <ion-content fullscreen>
      <ion-item>
        <ion-label>Select a Location</ion-label>
        <ion-select @ionChange="pokemonAvailable($event)">
          <ion-select-option
            v-for="(pnt, idx) in gameLocations"
            :key="idx"
            :value="pnt"
            >{{ pnt }}</ion-select-option
          >
        </ion-select>
      </ion-item>
      <ion-list>
        <ion-item v-for="pk in pointInGame" :key="pk.no">
          <ion-thumbnail slot="start">
            <img :src="pokemonPath2(pk.no)" />
          </ion-thumbnail>
          <ion-label>
            <h3>{{ pk.name }}</h3>
            <ion-thumbnail class="ion-margin-start">
              <img
                v-for="type in pk.types"
                :key="type"
                :src="pokemonTypePath(type)"
                :title="type"
              />
            </ion-thumbnail>
          </ion-label>
          <ion-col>
            <ion-row>
              <ion-col
                class="ion-text-center"
                v-for="(stat, i) in pk.stats"
                :key="i"
              >
                <ion-badge color="secondary">{{ stat }}</ion-badge>
                <br />
                <ion-text color="medium" style="font-size: 0.8em">{{
                  statOrder[i]
                }}</ion-text>
              </ion-col>
            </ion-row></ion-col
          >
          <ion-col>
            <ion-text>{{ pk.locations[0].point }}</ion-text>
          </ion-col>
        </ion-item>
      </ion-list>
    </ion-content>
  </ion-page>
</template>

<script>
import {
  IonBadge,
  IonCol,
  IonContent,
  IonItem,
  IonLabel,
  IonList,
  IonPage,
  IonRow,
  IonSelect,
  IonSelectOption,
  IonText,
  IonThumbnail,
} from "@ionic/vue";
import { defineComponent, ref, reactive } from "vue";
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

export default defineComponent({
  components: {
    IonBadge,
    IonCol,
    IonContent,
    IonItem,
    IonLabel,
    IonList,
    IonPage,
    IonRow,
    IonSelect,
    IonSelectOption,
    IonText,
    IonThumbnail,
  },
  setup() {
    let pointInGame = reactive([]);
    const pokemonId = ref(1);
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
    const pokemonPath = () => {
      return (
        process.env.BASE_URL + "assets/pokemon/" + pokemonId.value + ".png"
      );
    };
    const pokemonPath2 = (pkId) => {
      return process.env.BASE_URL + "assets/pokemon/" + pkId + ".png";
    };
    const pokemonTypePath = (typeStr) => {
      return process.env.BASE_URL + "assets/types/" + typeStr + ".png";
    };
    const pokemonAvailable = (event) => {
      // Clear the reactive array
      pointInGame.splice(0, pointInGame.length);

      // Filter for pokemon and then add them to the reactive array
      pokemonData
        .filter((pk, idx, arr) => {
          if (!pk.locations) {
            return false;
          }
          return pk.locations.find(
            (loc) => loc.location === event.target.value
          );
        })
        .forEach((e) => pointInGame.push(e));
    };
    return {
      pointInGame,
      pokemonId,
      pokemonData,
      gamePoints,
      gameLocations,
      statOrder,
      pokemonPath,
      pokemonPath2,
      pokemonTypePath,
      pokemonAvailable,
    };
  },
});
</script>