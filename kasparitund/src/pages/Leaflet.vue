<script setup>
import { ref } from 'vue';
import LeafletMap from '../components/LeafletMap.vue';

let center = ref([59.42708, 24.74337]); 
let zoom = ref(19);
</script>

<template>
    <button class="button is-primary" @click="center=[59.44297, 24.81264]">Go To Home</button>
    <input type="range" min="1" max="19" v-model="zoom">
    <LeafletMap :center="center" :zoom="zoom"></LeafletMap>
    <LeafletMap :center="[59.44297, 24.81264]" :zoom="19"></LeafletMap>
</template>
