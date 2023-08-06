<template>
  <div
    :id="id"
    class="error-container mb-2 flex w-full flex-col rounded-md border-2 border-solid bg-bg p-3"
    v-if="isShow"
  >
    <h6 class="min-w-fit">{{ errorMessage }}</h6>
    <p class="my-2 w-full">{{ suggestionMessage }}</p>
    <div id="child" class="text-sm">
      <button
        id="btn-submit"
        class="h-8 w-24 rounded-sm bg-green duration-200"
        @click="submitBtn"
      >
        Chấp nhận
      </button>
      <button
        id="btn-cancel"
        class="ml-2 h-8 w-24 rounded-sm duration-200"
        @click="cancelBtn(this)"
      >
        Bỏ qua
      </button>
    </div>
  </div>
</template>

<style scoped>
h6 {
  border-bottom: solid 2px #36302d;
}

p {
  word-break: break-all;
  white-space: normal;
}

#btn-submit,
#btn-cancel {
  border-bottom: solid 2px #494949;
}

#btn-submit:hover {
  background-color: #a7ffaa;
}

#btn-cancel:hover {
  background-color: #ffbbbb;
}
</style>

<script>
export default {
  props: {
    errorMessage: String,
    suggestionMessage: String,
    id: Number,
  },
  data() {
    return {
      isShow: true,
    };
  },
  methods: {
    submitBtn: function () {
      let textElement = document.querySelector("#text");
      let containerElement = document.querySelector(".error-container");
      let text = textElement.value;
      let fix = containerElement.getAttribute("fix");
      let cur = containerElement.getAttribute("text");
      text = text.replace(cur, fix);

      textElement.value = text;
      this.isShow = false;
    },
    cancelBtn: function (e) {
      this.isShow = false;
    },
  },
};
</script>
