<template>
  <div
    class="body container mx-auto flex w-full flex-col items-center justify-center p-4 md:flex-row md:px-0"
  >
    <textarea
      name=""
      id=""
      class="h-full w-full flex-1 resize-none rounded-md border-2 border-solid border-black bg-bg p-3 text-black"
      placeholder="Nhập văn bản vào đây"
    ></textarea>
    <div
      class="sidebar ml-0 mt-3 flex h-64 w-full flex-col overflow-scroll rounded-md border-2 border-solid border-black bg-bg p-3 md:ml-3 md:mt-0 md:h-full md:w-2/6"
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
