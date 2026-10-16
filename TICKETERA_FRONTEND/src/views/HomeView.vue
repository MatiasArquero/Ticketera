<script setup></script>

<template>
  <div>
    <h1>Bienvenido a Ticketera</h1>
    <p>Página pública de inicio.</p>
    <router-link to="/login">Iniciar sesión</router-link> |
    <router-link to="/dashboard">Ir al Dashboard</router-link>
  </div>
</template>

<style scoped>
h1 { margin-bottom: 0.5rem }
</style>
