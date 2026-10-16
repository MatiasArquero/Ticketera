<script setup></script>

<template>
  <div class="public-layout">
    <header class="public-header"><h1>Ticketera</h1></header>
    <main class="public-main">
      <slot />
    </main>
    <footer class="public-footer">© Ticketera</footer>
  </div>
</template>

<style scoped>
.public-layout { display:flex; flex-direction:column; min-height:100vh; }
.public-header { background:#f5f5f5; padding:1rem; border-bottom:1px solid #ccc;}
.public-main { flex:1; padding:1rem; }
.public-footer { background:#f5f5f5; padding:0.5rem; text-align:center; }
</style>
