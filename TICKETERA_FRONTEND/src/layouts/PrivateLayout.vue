<script setup></script>

<template>
  <div class="private-layout">
    <aside class="sidebar">
      <nav>
        <ul>
          <li><router-link to="/dashboard">Dashboard</router-link></li>
          <li><router-link to="/">Home</router-link></li>
        </ul>
      </nav>
    </aside>
    <div class="content-area">
      <header class="private-header"><h2>Ticketera - Dashboard</h2></header>
      <main class="private-main">
        <slot />
      </main>
    </div>
  </div>
</template>

<style scoped>
.private-layout { display:flex; min-height:100vh; }
.sidebar { width:220px; background:#f0f0f0; padding:1rem; border-right:1px solid #ccc;}
.content-area { flex:1; display:flex; flex-direction:column; }
.private-header { padding:1rem; border-bottom:1px solid #ddd; }
.private-main { padding:1rem; flex:1; }
</style>
