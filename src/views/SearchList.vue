<template>
  <ion-page>
    <ion-header translucent>
      <ion-toolbar>
        <ion-title>{{ label }}</ion-title>
      </ion-toolbar>
      <ion-toolbar>
        <ion-searchbar
          animated
          debounce="500"
          show-cancel-button="focus"
          v-model="searchQuery"
        ></ion-searchbar>
      </ion-toolbar>
    </ion-header>
    <ion-content fullscreen>
      <ion-list>
        <ion-item
          v-for="value in searchResults()"
          :key="value"
          @click="modalCallback(value)"
          >{{ getValue(value) }}</ion-item
        >
      </ion-list>
      <ion-fab vertical="bottom" horizontal="end" slot="fixed">
        <ion-fab-button
          activated="true"
          @click="modalCallback()"
        ></ion-fab-button>
      </ion-fab>
    </ion-content>
  </ion-page>
</template>

<script lang="ts">
import {
  IonContent,
  IonFab,
  IonFabButton,
  IonHeader,
  IonItem,
  IonList,
  IonPage,
  IonSearchbar,
  IonTitle,
  IonToolbar,
} from "@ionic/vue";
import { defineComponent, ref } from "vue";

export default defineComponent({
  components: {
    IonContent,
    IonFab,
    IonFabButton,
    IonHeader,
    IonList,
    IonItem,
    IonPage,
    IonSearchbar,
    IonTitle,
    IonToolbar,
  },
  props: {
    content: {
      type: Object as () => Record<string, any>[],
      required: true,
    },
    contentKey: {
      type: String,
      required: true,
    },
    label: {
      type: String,
      required: true,
    },
    modalCallback: {
      type: Function,
      required: true,
    },
  },
  setup(props) {
    const searchQuery = ref("");
    const searchResults = () => {
      if (searchQuery.value) {
        console.log(props.contentKey);
        return props.content.filter((item) => {
          if (props.contentKey) {
            return (
              item[props.contentKey]
                .toLowerCase()
                .indexOf(searchQuery.value.toLowerCase()) != -1
            );
          } else {
            console.log(item);
            return (
              item.toLowerCase().indexOf(searchQuery.value.toLowerCase()) != -1
            );
          }
        });
      } else {
        return props.content;
      }
    };
    const getValue = (item: Record<string, any>) => {
      if (props.contentKey) {
        return item[props.contentKey];
      } else {
        return item;
      }
    };
    return {
      getValue,
      searchQuery,
      searchResults,
    };
  },
});
</script>
<!-- GLOBAL STYLES
    AVOID USING THIS -->
<style>
.modal-wrapper {
  --box-shadow: 0 28px 48px rgba(0, 0, 0, 0.4);
  --backdrop-opacity: var(--ion-backdrop-opacity, 0.32);
}
</style>