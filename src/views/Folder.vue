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
      <ion-select @ionChange="gamePointChange($event)">
        <ion-select-option v-for="(pnt, idx) in gamePoints" :key="idx" :value="pnt.name">{{ pnt.name }}</ion-select-option>
      </ion-select>
    </ion-item>
    <ion-list>
      <ion-list-header>Item thumbnails</ion-list-header>
      <ion-item>
        <ion-thumbnail slot="start">
          <img :src="pokemonPath()">
        </ion-thumbnail>
        <ion-label>Lorem ipsum</ion-label>
      </ion-item>
      <ion-item>
        <ion-thumbnail slot="start">
          <img :src="pokemonPath()">
        </ion-thumbnail>
        <ion-label>
          <h3>Lorem ipsum</h3>
          <p>dolor sit amet</p>
        </ion-label>
      </ion-item>
      <ion-item>
        <ion-thumbnail slot="start">
          <img :src="pokemonPath()">
        </ion-thumbnail>
        <ion-label>
          <h3>Lorem ipsum</h3>
          <p>dolor sit amet</p>
          <p>consectetur adipiscing elit. Duis ut urna neque.</p>
        </ion-label>
      </ion-item>
      <ion-item>
        <ion-thumbnail slot="end">
          <img :src="pokemonPath()">
        </ion-thumbnail>
        <ion-label>Lorem ipsum</ion-label>
      </ion-item>
      <ion-item>
        <ion-thumbnail slot="end">
          <img :src="pokemonPath()">
        </ion-thumbnail>
        <ion-label>
          <h3>Lorem ipsum</h3>
          <p>dolor sit amet</p>
        </ion-label>
      </ion-item>
      <ion-item>
        <ion-thumbnail slot="end">
          <img :src="pokemonPath()">
        </ion-thumbnail>
        <ion-label>
          <h3>Lorem ipsum</h3>
          <p>dolor sit amet</p>
          <p>consectetur adipiscing elit. Duis ut urna neque.</p>
        </ion-label>
      </ion-item>
    </ion-list>
  </ion-content>
</template>

<script>
import { IonContent, IonItem, IonLabel, IonList, IonListHeader, IonThumbnail, IonSelect, IonSelectOption } from '@ionic/vue';
import { defineComponent, ref } from 'vue';
import { pokemonData10 } from './../data/gen1_0'
import { pokemonData11 } from './../data/gen1_1'
import { pokemonData20 } from './../data/gen2_0'
import { pokemonData30 } from './../data/gen3_0'
import { pokemonData40 } from './../data/gen4_0'
import { pokemonData50 } from './../data/gen5_0'
import { pokemonData60 } from './../data/gen6_0'
import { pokemonData70 } from './../data/gen7_0'
import { pokemonData80 } from './../data/gen8_0'
import { gamePoints, gameLocations } from './../data/reborn'

export default defineComponent({
  components: { IonContent, IonItem, IonLabel, IonList, IonListHeader, IonThumbnail, IonSelect, IonSelectOption },
  setup() {
    const pokemonId = ref(1)
    const pokemonData = pokemonData10.concat(pokemonData11, pokemonData20, pokemonData30, pokemonData40, pokemonData50, pokemonData60, pokemonData70, pokemonData80)
    const pokemonPath = () => {
      return process.env.BASE_URL + "assets/pokemon/" + pokemonId.value + ".png"
    }
    const gamePointChange = (event) => {
      const maxLv = gamePoints.filter((itm) => itm.name === event.target.value)[0].level
      console.log(event.target.value, maxLv)
    }
    return {
      pokemonId,
      pokemonData,
      gamePoints,
      gameLocations,
      pokemonPath,
      gamePointChange
    }
  }
});
</script>