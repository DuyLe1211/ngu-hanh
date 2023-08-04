<template>
  <div class="body flex-1">
    <div class="main flex h-96 w-full items-center justify-center text-base">
      <div class="mx-4 flex max-w-4xl flex-col items-center justify-center">
        <img src="../../public/img/logo.png" alt="Logo" class="w-36" />
        <p class="main__desc my-3">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut et massa
          mi. Aliquam in hendrerit urna. Pellentesque sit amet sapien fringilla,
          mattis ligula consectetur, ultrices mauris. Maecenas vitae mattis
          tellus.
        </p>
        <router-link
          to="/app"
          class="main__btn flex h-8 w-24 items-center justify-center border-2 border-solid border-black"
          ><span>Bắt đầu</span></router-link
        >
      </div>
    </div>

    <div
      class="feature flex h-96 w-full items-center justify-center bg-darkgray text-base"
    >
      <div class="mx-4 flex max-w-4xl flex-col items-center justify-center">
        <h3 class="feature__title text-5xl text-black">feature 1</h3>
        <p class="feature__desc">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut et massa
          mi. Aliquam in hendrerit urna. Pellentesque sit amet.
        </p>
      </div>
    </div>

    <footer class="footer navbar h-14 bg-black">
      <div
        class="font container mx-auto flex h-full items-center text-base text-gray"
      >
        <h5 class="footer__copyright">
          Copyright 2023 Lazy Team, All rights reserved.
        </h5>
      </div>
    </footer>
  </div>
</template>

<style scoped>
.main__btn:hover {
  background-color: #a3a3a3;
}
</style>

<script></script>
