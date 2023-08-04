<template>
  <div class="body container mx-auto flex items-center justify-center">
    <textarea
      name=""
      id=""
      class="h-5/6 flex-1 resize-none rounded-md border-2 border-solid border-black bg-bg p-3 text-black"
      placeholder="Nhập văn bản vào đây"
    ></textarea>
    <div
      class="sidebar ml-3 flex h-5/6 w-2/6 flex-col overflow-scroll rounded-md border-2 border-solid border-black bg-bg p-3"
    >
      <Error
        error-message="Loại lỗi"
        suggestion-message="Suggestionasdlksdlsdkdjdlskdjsdkdadkdlksdldjjkskdjsdkdadkdlksdldjj"
      />
      <Error
        error-message="Loại lỗi"
        suggestion-message="Suggestionasdlksdlsdkdjdlskdjsdkdadkdlksdldjjkskdjsdkdadkdlksdldjj"
      />
      <Error
        error-message="Loại lỗi"
        suggestion-message="Suggestionasdlksdlsdkdjdlskdjsdkdadkdlksdldjjkskdjsdkdadkdlksdldjj"
      />
      <Error
        error-message="Loại lỗi"
        suggestion-message="Suggestionasdlksdlsdkdjdlskdjsdkdadkdlksdldjjkskdjsdkdadkdlksdldjj"
      />
      <Error
        error-message="Loại lỗi"
        suggestion-message="Suggestionasdlksdlsdkdjdlskdjsdkdadkdlksdldjjkskdjsdkdadkdlksdldjj"
      />
      <Error
        error-message="Loại lỗi"
        suggestion-message="Suggestionasdlksdlsdkdjdlskdjsdkdadkdlksdldjjkskdjsdkdadkdlksdldjj"
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
};
</script>
