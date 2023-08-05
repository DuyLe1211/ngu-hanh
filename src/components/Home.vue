<template>
  <div class="body flex flex-1 flex-col">
    <div
      class="main flex max-h-[48rem] min-h-[36rem] flex-1 items-center justify-center text-base"
    >
      <div
        class="mx-4 mb-5 flex max-w-4xl flex-col items-center justify-center text-base"
      >
        <img src="/img/logo.png" alt="Logo" class="w-64" />
        <p class="main__desc my-3 text-center">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut et massa
          mi. Aliquam in hendrerit urna. Pellentesque sit amet sapien fringilla,
          mattis ligula consectetur, ultrices mauris. Maecenas vitae mattis
          tellus.
        </p>
        <router-link
          to="/app"
          class="main__btn flex h-8 w-24 items-center justify-center border-2 border-solid border-black duration-200"
          ><span>Bắt đầu</span></router-link
        >
      </div>
    </div>

    <div
      class="feature flex min-h-[24rem] w-full flex-1 items-center justify-center bg-darkgray text-base"
    >
      <div class="mx-4 flex max-w-4xl flex-col items-center justify-center">
        <h3 class="feature__title text-5xl text-black">Feature 1</h3>
        <p class="feature__desc text-center">
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
