<template>
  <div
    class="body container mx-auto flex w-full flex-col items-center justify-center p-4 md:flex-row md:px-0"
  >
    <textarea
      name=""
      id="text"
      class="h-full w-full flex-1 resize-none rounded-md border-2 border-solid border-black bg-bg p-3 text-black"
      placeholder="Nhập văn bản vào đây"
      @keypress.enter="reset"
    ></textarea>
    <div
      id="sidebar"
      class="ml-0 mt-3 flex h-64 w-full flex-col overflow-scroll rounded-md border-2 border-solid border-black bg-bg p-3 md:ml-3 md:mt-0 md:h-full md:w-2/6"
    >
      <Error
        v-for="(mistake, index) in data"
        :error-message="mistake.desc"
        :suggestion-message="mistake.fix"
        :id="index"
        :descf="mistake.bound[0]"
        :descs="mistake.bound[1]"
        :text="mistake.text"
        :fix="mistake.fix"
      />
    </div>
  </div>
</template>

<style scoped>
.body {
  height: calc(100vh - 56px);
}
</style>

<script>
import Error from "./Error.vue";

export default {
  components: {
    Error,
  },
  data() {
    return {
      data: [],
    };
  },
  methods: {
    reset: async function () {
      let textElement = document.querySelector("#text");
      let text = textElement.value;
      data = await fetch(`http://localhost:8008`, {
        method: "POST",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json",
        },
        redirect: "follow",
        referrerPolicy: "no-referrer",
        body: JSON.stringify(text),
      })
        .then((res) => {
          return res.json();
        })
        .then((resdata) => {
          return (this.data = resdata);
        });
    },
  },
};
</script>
