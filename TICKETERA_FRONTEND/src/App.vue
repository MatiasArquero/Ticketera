<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import PublicLayout from './layouts/PublicLayout.vue'
import PrivateLayout from './layouts/PrivateLayout.vue'

const route = useRoute()

const layout = computed(() => {
  const map = { PublicLayout, PrivateLayout }
  const key = route.meta && route.meta.layout ? route.meta.layout : 'PublicLayout'
  return map[key] || PublicLayout
})
</script>

<template>
  <component :is="layout">
    <router-view />
  </component>
</template>

<style scoped>
/* Minimal layout-neutral styles */
</style>
