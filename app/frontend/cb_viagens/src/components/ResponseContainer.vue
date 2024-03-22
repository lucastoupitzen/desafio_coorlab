<template>

    <div class="container">
        
        <div v-if="$store.state.showInfo">
            <div  class="response-area">
                <p class="message">Essas são as melhores alternativas de viagens para a data selecionada </p>
            
                <TransportInfo :campo1="$store.state.confortInfo.data.data['name']"
                               :campo2="'Poltrona: '+$store.state.confortInfo.data.data['bed']+' (Completo)'"
                               :campo3="'Tempo estimado: ' + $store.state.confortInfo.data.data['duration']"
                               :campo4="$store.state.confortInfo.data.data['price_confort']"
                               :icon="'bi bi-clock-history'" class="infos-requested"/>

                <TransportInfo :campo1="$store.state.cheaperInfo.data.data['name']"
                               :campo2="'Leito: '+$store.state.cheaperInfo.data.data['seat']+' (Convencional)'"
                               :campo3="'Tempo estimado: ' + $store.state.cheaperInfo.data.data['duration']"
                               :campo4="$store.state.cheaperInfo.data.data['price_econ']"
                               :icon="'bi bi-cash-coin'" class="infos-requested"/>
            
                            </div>
                <div class="d-flex justify-content-end mt-5">
                    <button @click='$store.commit("setShowInfoFalse")' type="submit" class="btn btn-primary btn-limpar">Limpar</button>
                </div>
        </div>
        <div v-else>
            <p>Nenhum dado selecionado</p>
        </div>

    </div>

</template>

<script>
  import TransportInfo from './TransportInfo.vue'
 
  export default {
    name: 'ResponseContainer',
    props: {
      msg: String
    },
    components: {
        TransportInfo
    },
    
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
      .container {
        width: fit-content;
        height: fit-content;
      }
      .infos-requested {
        margin-bottom: 20px;
      }
      .response-area{
        display: flex;
        align-items: flex-start;
        flex-direction: column;
      }
      .message {
        padding-top: 3dvw;
        padding-left: 12px;
        width: 320px;
      }
      .btn-limpar {
        background-color: #f4a532;
        width: 150px;
        border: none;
        font-size: .8em;
        font-weight: bold;
        color: black;
        margin-right: 12px;
      }
  </style>