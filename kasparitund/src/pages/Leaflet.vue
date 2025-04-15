<script setup>
import { ref } from 'vue';
import LeafletMap from '../components/LeafletMap.vue';
 
let center = ref([59.42708, 24.74337]);
let zoom = ref(19);
</script>
 
<template>
    <button class="button is-primary" @click="center=[-25.06623, -130.09967]">Go To Home</button>
    <input type="range" min="1" max="19" v-model="zoom">
    <LeafletMap :center="center" :zoom="zoom"></LeafletMap>
    <LeafletMap :center="[24.74337, 59.42708]" :zoom="19"></LeafletMap>
</template>