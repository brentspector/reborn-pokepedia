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
import { IonContent, IonItem, IonLabel, IonThumbnail, IonSelect, IonSelectOption } from '@ionic/vue';
import { defineComponent, ref } from 'vue';
import { pokemonData } from './../data/pokemon'

export default defineComponent({
  components: { IonContent, IonItem, IonLabel, IonThumbnail, IonSelect, IonSelectOption },
  setup() {
    const pokemonId = ref(1)
    const pokemonPath = () => {
      return process.env.BASE_URL + "assets/pokemon/" + pokemonId.value + ".png"
    }
    return {
      pokemonId,
      pokemonData,
      pokemonPath
    }
  }
});
</script>