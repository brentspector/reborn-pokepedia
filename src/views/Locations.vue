<template>
  <ion-page>
    <ion-content fullscreen>
      <ion-item>
        <ion-label>Select a Location</ion-label>
        <ion-select @ionChange="pokemonAvailable($event)">
          <ion-select-option
            v-for="(loc, idx) in gameLocations"
            :key="idx"
            :value="loc"
            >{{ loc }}</ion-select-option
          >
        </ion-select>
      </ion-item>
      <ion-list>
        <ion-item
          v-for="pk in pokemonAtLocation"
          :key="pk.no"
          @click="setOpen(true, pk)"
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
                {{ pokemonLocation(pk).method }}
              </ion-text>
            </ion-row>
            <ion-row class="point">
              <ion-text>
                {{ pokemonLocation(pk).point }}
              </ion-text>
            </ion-row>
          </ion-col>
        </ion-item>
      </ion-list>
      <!--
        TODO:
        - Clicking modal does NOT clear current location selected
        -- ion-modal is clearing the ion-select value
        - Add close FAB
        - Toggle select pokemon dropdown in modal to be hidden when imported as modal
       -->
      <ion-modal
        :is-open="isOpenRef"
        :swipe-to-close="true"
        @didDismiss="setOpen(false)"
      >
        <Detailes :pk="modalPokemon"></Detailes>
      </ion-modal>
    </ion-content>
  </ion-page>
</template>

<script lang="ts">
import {
  IonCol,
  IonContent,
  IonItem,
  IonLabel,
  IonList,
  IonModal,
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
import { gameLocations } from "@/data/reborn";
import { Pokemon } from "@/interfaces/pokemon_interfaces";
import Detailes from "@/views/Details.vue";

export default defineComponent({
  components: {
    Detailes,
    IonCol,
    IonContent,
    IonItem,
    IonLabel,
    IonList,
    IonModal,
    IonPage,
    IonRow,
    IonSelect,
    IonSelectOption,
    IonText,
    IonThumbnail,
  },
  setup() {
    const isOpenRef = ref(false);
    let pokemonAtLocation: Pokemon[] = reactive([]);
    let locationInGame = "";
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
    const modalPokemon = ref(pokemonData[0]);
    const setOpen = (state: boolean, pk: Pokemon = pokemonData[0]) => {
      isOpenRef.value = state;
      modalPokemon.value = pk;
    };
    const pokemonPath = (pkId: number) => {
      return process.env.BASE_URL + "assets/pokemon/" + pkId + ".png";
    };
    const pokemonTypePath = (typeStr: string) => {
      return process.env.BASE_URL + "assets/types/" + typeStr + ".png";
    };
    const pokemonLocation = (pk: Pokemon) => {
      return pk.locations.filter((loc) => loc.location === locationInGame)[0];
    };

    const pokemonAvailable = (event: any) => {
      if (!isOpenRef.value) {
        // Clear the reactive array
        pokemonAtLocation.splice(0, pokemonAtLocation.length);

        // Set current point in game to whatever was in the event
        locationInGame = event.target.value;

        // Filter for pokemon and then add them to the reactive array
        pokemonData
          .filter((pk, idx, arr) => pokemonLocation(pk))
          .forEach((e) => pokemonAtLocation.push(e));
      }
    };
    return {
      gameLocations,
      isOpenRef,
      modalPokemon,
      pokemonAtLocation,
      pokemonPath,
      pokemonTypePath,
      pokemonLocation,
      pokemonAvailable,
      setOpen,
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
</style>