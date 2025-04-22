<script setup>
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import 'leaflet/dist/images/marker-icon-2x.png';
import 'leaflet/dist/images/marker-icon.png';
import 'leaflet/dist/images/marker-shadow.png';
import { onMounted, useId, watch } from 'vue';

const { center, zoom } = defineProps(['center', 'zoom']);
const id = 'map-' + useId();
let map;

onMounted(() => {
    map = L.map(id).setView(center, zoom);

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

    const homeLatLng = [59.44297, 24.81264];
    const blueIcon = new L.Icon({
        iconUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon-2x-blue.png',
        shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png',
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
        shadowSize: [41, 41]
    });

    const homeMarker = L.marker(homeLatLng, { icon: blueIcon }).addTo(map);
    homeMarker.bindPopup("Kodu").openPopup();

    const polygon = L.polygon([
        [homeLatLng[0] + 0.001, homeLatLng[1] - 0.001],
        [homeLatLng[0] + 0.001, homeLatLng[1] + 0.001],
        [homeLatLng[0] - 0.001, homeLatLng[1] + 0.001],
        [homeLatLng[0] - 0.001, homeLatLng[1] - 0.001]
    ], {
        color: 'blue',
        fillColor: '#3399ff',
        fillOpacity: 0.3
    }).addTo(map);
});

watch(() => center, (newCenter) => {
    if (map) {
        map.panTo(newCenter);
    }
});

watch(() => zoom, (newZoom) => {
    if (map) {
        map.setZoom(newZoom);
    }
});
</script>

<template>
    <div :id="id"></div>
</template>

<style scoped>
div {
    height: 90vh;
}
</style>
