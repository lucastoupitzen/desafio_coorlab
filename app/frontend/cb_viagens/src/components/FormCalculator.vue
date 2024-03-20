<template>

    <div class="container">
        
            <div>
                <h2 class="form-title">Calcule o Valor da Viagem</h2>
                <form @submit.prevent="sendForm">
                    <div class="mb-3">
                        <label for="selectOption" class="form-label label">Destino:</label>
                        <select class="form-select" id="destinselected" placeholder="Selecione o destino">
                            <option value="" disabled selected hidden>Selecione o destino</option>
                            <option value="Campinas">Campinas</option>
                            <option value="Belo Horizonte">Belo Horizonte</option>
                            <option value="São Paulo">São Paulo</option>
                        </select>
                    </div>
                    <div class="mb-3">
                        <label for="dateInput" class="form-label label">Data:</label>
                        <input type="date" class="form-control" id="dateInput" placeholder="Selecione uma data">
                    </div>
                    <div class="text-center">
                        <button type="submit" class="btn btn-primary btn-enviar">Enviar</button>
                    </div>
                </form>
            </div>

    </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'FormCalculator',
  props: {
    msg: String
  },
  methods: {
    sendForm() {
      const destino = document.getElementById('destinselected').value;
      const data = document.getElementById('dateInput').value;

      // Verifique se os campos foram preenchidos antes de enviar a requisição
      if (!destino || !data) {
        alert('Por favor, preencha todos os campos');
        return;
      }
      // Envia a requisição GET para o backend
      axios.get(`http://localhost:3000/transport/cheaper?city=${destino}`)
        .then(response => {  
          console.log(response.data);
          // Faça algo com a resposta do backend, se necessário
        })
        .catch(error => {
          console.error(error);
          // Trate erros, se houver algum
        });

      axios.get(`http://localhost:3000/transport/confort?city=${destino}`)
        .then(response => {
          console.log(response.data);
          // Faça algo com a resposta do backend, se necessário
        })
        .catch(error => {
          console.error(error);
          // Trate erros, se houver algum
        });
    }
  }
}
</script>

<style scoped>
    .container {
        width: fit-content;
        height: fit-content;
        padding: 25px;
        display: flex;
    }

    .form-title {
        color: rgb(68, 68, 68);
        font-size: 1em 
    }
                                         
    .btn-enviar {
        width: 50%;
        margin: auto;
    }

    .label {
        color: rgb(68, 68, 68);
        font-size: .8em;
        font-weight: bold;
    }


</style>