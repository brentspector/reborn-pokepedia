<template>
  <ion-content fullscreen>
    <ion-list-header>Default</ion-list-header>
                <ion-item>
              <ion-label>Select a Pokemon</ion-label>
              <ion-select v-model="pokemonId">
                <ion-select-option v-for="(pk, idx) in pokemonData" :key="idx" :value="pk.no">{{ pk.name }}</ion-select-option>
              </ion-select>
            </ion-item>
    <ion-thumbnail class="ion-margin-start" style="--size:132px;">
      <img :src="pokemonPath()">
    </ion-thumbnail>

    <ion-item>
      <ion-label>Point in Game</ion-label>
      <ion-select @ionChange="pokemonAvailable($event)">
        <ion-select-option v-for="(pnt, idx) in gameLocations" :key="idx" :value="pnt">{{ pnt }}</ion-select-option>
      </ion-select>
    </ion-item>
    <ion-list>
      <ion-list-header>Item thumbnails</ion-list-header>
      <ion-item v-for="pk in pointInGame" :key="pk.no">
        <ion-thumbnail slot="start">
          <img :src="pokemonPath2(pk.no)">
        </ion-thumbnail>
        <ion-label>
          <h3>{{ pk.name }}</h3>
          <ion-thumbnail class="ion-margin-start">
            <img v-for="type in pk.types" :key="type" :src="pokemonTypePath(type)" :title="type">
          </ion-thumbnail>
        </ion-label>
      </ion-item>
    </ion-list>
  </ion-content>
</template>

<script>
import { IonContent, IonItem, IonLabel, IonList, IonListHeader, IonThumbnail, IonSelect, IonSelectOption } from '@ionic/vue';
import { defineComponent, ref, reactive } from 'vue';
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
import { gamePoints, gameLocations } from '@/data/reborn'

export default defineComponent({
  components: { IonContent, IonItem, IonLabel, IonList, IonListHeader, IonThumbnail, IonSelect, IonSelectOption },
  setup() {
    let pointInGame = reactive([])
    const pokemonId = ref(1)
    const pokemonData = pokemonData10.concat(pokemonData11, pokemonData12, pokemonData20, pokemonData21,
      pokemonData30, pokemonData31, pokemonData32, pokemonData40, pokemonData41,
      pokemonData50, pokemonData51, pokemonData52, pokemonData60, pokemonData61, pokemonData70, pokemonData71)
    const pokemonPath = () => {
      return process.env.BASE_URL + "assets/pokemon/" + pokemonId.value + ".png"
    }
    const pokemonPath2 = (pkId) => {
      return process.env.BASE_URL + "assets/pokemon/" + pkId + ".png"
    }
    const pokemonTypePath = (typeStr) => {
      return process.env.BASE_URL + "assets/types/" + typeStr + ".png"
    }
    const pokemonAvailable = (event) => {
      // Clear the reactive array
      pointInGame.splice(0, pointInGame.length)

      // Filter for pokemon and then add them to the reactive array
      pokemonData.filter((pk, idx, arr) => {
        if (!pk.locations) {
          return false;
        }
        return pk.locations.find(loc => loc.location === event.target.value)
      }).forEach(e => pointInGame.push(e))
    }
    return {
      pointInGame,
      pokemonId,
      pokemonData,
      gamePoints,
      gameLocations,
      pokemonPath,
      pokemonPath2,
      pokemonTypePath,
      pokemonAvailable
    }
  }
});
</script>