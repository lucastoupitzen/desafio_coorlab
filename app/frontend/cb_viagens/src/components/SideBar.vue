<template>
  <!-- Sidebar -->
  <nav class="sidebar">
            <!-- Logo -->
            <div class="logo">
                <img src="../../../../../doc/logo.png" alt="Logo CB viagens">
            </div>
            
            <!-- navigation menu -->
            <ul class="nav flex-column">
                <li class="nav-item">
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
      background-color: black;
      width: 20dvw;
      height: 100dvh;
      padding: 1dvw;
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
    }
</style>
