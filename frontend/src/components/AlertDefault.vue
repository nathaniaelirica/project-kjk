<template>
    <div>
      <!-- Modal -->
      <div
        v-if="OpenClose"
        class="modal fade show"
        tabindex="-1"
        aria-labelledby="exampleModalLabel"
        aria-modal="true"
        role="dialog"
        style="display:block"
      >
        <div class="modal-dialog modal-dialog-centered">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">Modal Title</h5>
              <!-- <button type="button" @click="OpenCloseFun()" class="btn-close"></button> -->
            </div>
            <div class="modal-body">
              <slot></slot>
            </div>
            <div class="modal-footer">
              <!-- <button type="button" @click="OpenCloseFun()" :class="'btn btn-' + variant"></button> -->
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AlertDefault',
    props: {
      visible: Boolean,
      variant: String,
    },
    data() {
      return {
        OpenClose: false, // Inisialisasi ke false
      };
    },
    methods: {
      OpenCloseFun() {
        this.OpenClose = !this.OpenClose; // Toggle OpenClose
        this.$emit('update:visible', this.OpenClose); // Menggunakan emit untuk memperbarui prop visible di luar komponen
      },
    },
    watch: {
      visible: function (newVal, oldVal) {
        // Watch the 'visible' prop and update 'OpenClose' accordingly
        this.OpenClose = newVal;
      },
    },
  };
  </script>
  