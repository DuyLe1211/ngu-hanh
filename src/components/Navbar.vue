<template>
  <nav class="navbar h-14 bg-black">
    <div class="container mx-auto flex h-full text-base text-gray">
      <router-link to="/" class="navbar_link mr-4 flex items-center"
        ><span>Home</span></router-link
      >
      <router-link to="/app" class="navbar_link flex items-center"
        ><span>Xử lý văn bản</span></router-link
      >
    </div>
  </nav>
</template>

<style scoped>
.navbar_link:hover {
  color: #ffffff;
}
</style>

<script></script>
