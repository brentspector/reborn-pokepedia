<template>
  <ion-content fullscreen>
    <ion-list-header>Default</ion-list-header>
    <ion-input v-model="pokemonId"></ion-input>
    <ion-thumbnail class="ion-margin-start" style="--size:132px;">
      <img :src="pokemonPath()">
    </ion-thumbnail>


    <ion-list>
      <ion-list-header>Item thumbnails</ion-list-header>
      <ion-item>
        <ion-thumbnail slot="start">
          <img src="/assets/pokemon/132.png">
        </ion-thumbnail>
        <ion-label>Lorem ipsum</ion-label>
      </ion-item>
      <ion-item>
        <ion-thumbnail slot="start">
          <img src="/assets/pokemon/132.png">
        </ion-thumbnail>
        <ion-label>
          <h3>Lorem ipsum</h3>
          <p>dolor sit amet</p>
        </ion-label>
      </ion-item>
      <ion-item>
        <ion-thumbnail slot="start">
          <img src="/assets/pokemon/132.png">
        </ion-thumbnail>
        <ion-label>
          <h3>Lorem ipsum</h3>
          <p>dolor sit amet</p>
          <p>consectetur adipiscing elit. Duis ut urna neque.</p>
        </ion-label>
      </ion-item>
      <ion-item>
        <ion-thumbnail slot="end">
          <img src="/assets/pokemon/132.png">
        </ion-thumbnail>
        <ion-label>Lorem ipsum</ion-label>
      </ion-item>
      <ion-item>
        <ion-thumbnail slot="end">
          <img src="/assets/pokemon/132.png">
        </ion-thumbnail>
        <ion-label>
          <h3>Lorem ipsum</h3>
          <p>dolor sit amet</p>
        </ion-label>
      </ion-item>
      <ion-item>
        <ion-thumbnail slot="end">
          <img src="/assets/pokemon/132.png">
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
import { IonContent, IonInput, IonItem, IonLabel, IonThumbnail } from '@ionic/vue';
import { defineComponent, ref } from 'vue';

export default defineComponent({
  components: { IonContent, IonInput, IonItem, IonLabel, IonThumbnail },
  setup() {
    const pokemonId = ref(1)
    const pokemonPath = () => {
      return process.env.BASE_URL + "assets/pokemon/" + pokemonId.value + ".png"
    }
    return {
      pokemonId,
      pokemonPath
    }
  }
});
</script>