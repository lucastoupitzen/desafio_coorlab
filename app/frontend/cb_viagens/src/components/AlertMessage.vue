<template>
      
     <div class="popup">

        <div class="popup-content">
            <i class="bi bi-exclamation-square"></i>
            <p class="message">Insira os valores para realizar a cotação</p>
            <button @click="closeModal" class="btn btn-primary btn-fechar popup-close">Fechar  </button>
        </div>
     </div>

  </template>
  
  <script>

  import store from '../store'   
  export default {
    name: 'AlertMessage', 
    methods: {
      
      closeModal() {
        store.commit("setShowAlertFalse")
      }
    }
  }
  </script>
  
  <style scoped>
    .popup {
        position: fixed;
        top: 0;
        right: 0;
        left: 0;
        bottom: 0;
        z-index: 99;
        background-color: rgba(0,0,0, 0.3);
        display: flex;
        align-items: center;
        justify-content: center
    }
    .popup-content {
        background-color: white;
        position: relative;
        width: 30dvw;
        padding: 3dvw 7dvw;
        display: flex;
        align-items: center;
        flex-direction: column;
        border-radius: 10px;
    }
    .bi-exclamation-square {
        font-size: 3em;
        color: #037179;
    }
    .message {
        width: 100%;
        color: rgb(97, 97, 97);
        font-weight: bold;
        text-align: center;
    }

    .btn-fechar {
        width: 80%;
        margin: auto;
        margin-top: 2dvh;
        font-size: .8em;
        font-weight: bold;
        color: black;
        background-color: #04a8b5;
        border: none;
    }
  </style>