<template>
  <div
    class="error-container mb-2 flex w-full flex-col rounded-md border-2 border-solid bg-bg p-3"
  >
    <h6 class="min-w-fit">{{ errorMessage }}</h6>
    <p class="my-2 w-full">{{ suggestionMessage }}</p>
    <div class="text-sm">
      <button class="btn-submit h-8 w-24 rounded-sm bg-green duration-200">
        Chấp nhận
      </button>
      <button class="btn-cancel ml-2 h-8 w-24 rounded-sm duration-200">
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

.btn-submit,
.btn-cancel {
  border-bottom: solid 2px #494949;
}

.btn-submit:hover {
  background-color: #a7ffaa;
}

.btn-cancel:hover {
  background-color: #ffbbbb;
}
</style>

<script>
export default {
  props: {
    errorMessage: String,
    suggestionMessage: String,
  },
};
</script>
