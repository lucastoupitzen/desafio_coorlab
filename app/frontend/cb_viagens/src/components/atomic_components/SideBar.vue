<template>
  <!-- Sidebar -->
  <nav class="sidebar">
            <!-- Logo -->
            <div class="logo">
                <img src="../../../../../../doc/logo.png" alt="Logo CB viagens">
            </div>
            
            <!-- navigation menu -->
            <ul class="nav flex-column">
                <li class="nav-item calculator">
                  <i class="bi bi-calculator-fill"></i>
                    <a class="nav-link menu-option" href="#">Calculadora de Viagem</a>
                </li>
            </ul>
  </nav>
</template>

<script>
export default {
  name: 'SideBar',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .sidebar {
      background-color: #2a3a59;
      width: 22dvw;
      height: 100dvh;
      padding: 2dvw;
      padding-top: 2dvw;
    }
    .logo {
      margin-bottom: 7dvh;
    }
    .logo img{
      width: 12dvw;
      height: auto;
    }
    .menu-option {
      color: white;
      padding-left: 6px
    }
    .calculator {
      display: flex;
      align-items: center;

    }
    .bi-calculator-fill {
      color: white;
      font-size: 1.1em;
    }
</style>
