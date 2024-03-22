<template>

    <div class="container">
        
            <div>
                <div class="title">
                    <i class="bi bi-cash-coin"></i>
                    <h2 class="form-title">Calcule o Valor da Viagem</h2>
                </div>
                <form @submit.prevent="sendForm">
                    <div class="mb-3">
                        <label for="selectOption" class="form-label label">Destino</label>
                        <CitySelector id="destinselected"/>
                    </div>
                    <div class="mb-3">
                        <label for="dateInput" class="form-label label">Data</label>
                        <input type="text" class="form-control date-input" id="dateInput" placeholder="Selecione uma data" onfocus="this.type='date'" >
                    </div>
                    <div class="text-center">
                        <button type="submit" class="btn btn-primary btn-enviar">Buscar</button>
                    </div>
                </form>
            </div>

    </div>
</template>

<script>
import axios from 'axios'
import store from '../store'   
import CitySelector from './CitySelector.vue' 


export default {
  name: 'FormCalculator',
  props: {
    msg: String
  },
  components: {
    CitySelector
  },
  methods: {
    sendForm() {
      const destino = document.getElementById('destinselected').innerText;
      const data = document.getElementById('dateInput').value;

      // Verifique se os campos foram preenchidos antes de enviar a requisição
      if (!destino || !data) {
        this.openModal();
        return;
      }
      // Envia a requisição GET para o backend
      axios.get(`http://localhost:3000/transport/cheaper?city=${destino}`)
        .then(response => {  
            // Chama a mutation para alterar showInfo para true
            store.commit("setCheaperInfo", response)
            // Faça algo com a resposta do backend, se necessário
            axios.get(`http://localhost:3000/transport/confort?city=${destino}`)
                .then(response2 => {
                    store.commit("setConfortInfo", response2)
                    store.commit("setShowInfoTrue")
                // Faça algo com a resposta do backend, se necessário
                })
                .catch(error => {
                    console.error(error);
                // Trate erros, se houver algum
                });
        })
        .catch(error => {
          console.error(error);
          // Trate erros, se houver algum
        });

     
    },
    openModal() {
        store.commit("setShowAlertTrue")
      },
  }
}
</script>

<style scoped>
    .container {
        width: fit-content;
        height: fit-content;
        padding: 3dvw;
        padding-bottom: 10dvh;
        display: flex;
        background-color: rgba(211, 211, 211, 0.554);
        border-radius: 10px;
    }

    .form-title {
        color: rgb(68, 68, 68);
        font-size: 1.2em;
        margin-left: 1dvw;
    }
                                         
    .btn-enviar {
        width: 80%;
        margin: auto;
        margin-top: 3.5dvh;
        font-size: .8em;
        font-weight: bold;
        color: black;
        background-color: #04a8b5;
        border: none;
    }

    .label {
        color: rgb(68, 68, 68);
        font-size: .8em;
        font-weight: bold;
    }

    .title {
        display: flex;
        align-items: center;
        justify-content: space-around;
        margin-bottom: 8px;
    }
    .bi-cash-coin {
        font-size: 1.2em;
        font-weight: bold;
    }

    .date-input {
        color: rgb(97, 96, 96);
    }
   
</style>