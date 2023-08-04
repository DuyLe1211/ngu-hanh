<template>
  <div class="body flex-1">
    <div class="main w-full h-96 text-base flex justify-center items-center">
      <div class="max-w-4xl flex flex-col justify-center items-center mx-4">
        <h1 class="main__title text-5xl text-title">Ngữ Hành</h1>
        <p class="main__desc my-3">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut et massa
          mi. Aliquam in hendrerit urna. Pellentesque sit amet sapien fringilla,
          mattis ligula consectetur, ultrices mauris. Maecenas vitae mattis
          tellus.
        </p>
        <router-link
          to="/app"
          class="main__btn w-24 h-8 border-solid border-2 border-black flex justify-center items-center"
          ><span>Bắt đầu</span></router-link
        >
      </div>
    </div>

    <div
      class="feature w-full h-96 text-base flex justify-center items-center bg-darkgray"
    >
      <div class="max-w-4xl flex flex-col justify-center items-center mx-4">
        <h3 class="feature__title text-5xl text-black">feature 1</h3>
        <p class="feature__desc">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut et massa
          mi. Aliquam in hendrerit urna. Pellentesque sit amet.
        </p>
      </div>
    </div>

    <footer class="footer navbar h-14 bg-black">
      <div
        class="container mx-auto text-gray flex font h-full text-base items-center"
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
