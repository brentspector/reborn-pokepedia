<template>
  <ion-page>
    <ion-content fullscreen>
      <ion-item>
        <ion-label>Select a Pokemon</ion-label>
        <ion-select v-model="pokemonSel">
          <ion-select-option
            v-for="(pk, idx) in pokemonData"
            :key="idx"
            :value="pk"
            >{{ pk.name }}</ion-select-option
          >
        </ion-select>
      </ion-item>
      <ion-thumbnail class="ion-margin-start" style="--size: 132px">
        <img :src="pokemonPath()" />
      </ion-thumbnail>
      <ion-list>
        <ion-item v-for="(val, key) in pokemonSel" :key="key">
          <ion-col>
            <ion-text>{{ key }}</ion-text>
          </ion-col>
          <ion-col>
            <ion-text>{{ val }}</ion-text>
          </ion-col>
        </ion-item>
      </ion-list>
    </ion-content>
  </ion-page>
</template>

<script>
import {
  IonCol,
  IonContent,
  IonItem,
  IonLabel,
  IonList,
  IonPage,
  IonSelect,
  IonSelectOption,
  IonText,
  IonThumbnail,
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

export default defineComponent({
  components: {
    IonCol,
    IonContent,
    IonItem,
    IonLabel,
    IonList,
    IonPage,
    IonSelect,
    IonSelectOption,
    IonText,
    IonThumbnail,
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
    const pokemonSel = ref(pokemonData[0]);
    const pokemonPath = () => {
      return (
        process.env.BASE_URL + "assets/pokemon/" + pokemonSel.value.no + ".png"
      );
    };
    return {
      pokemonSel,
      pokemonData,
      gamePoints,
      gameLocations,
      statOrder,
      pokemonPath,
    };
  },
});
</script>