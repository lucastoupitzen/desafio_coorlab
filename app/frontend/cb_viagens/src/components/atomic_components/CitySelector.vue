<template>
    <div class="city-selector-menu">
        <div class="select-btn">
            <span class="btn-text">Selecione o destino</span>
            <i class="bi bi-caret-right-fill"></i>
        </div>

        <ul class="options">
            <li class="option">
                <i class="bi bi-circle-fill"></i>
                <span class="option-text">Belo Horizonte</span>
            </li>
            <li class="option">
                <i class="bi bi-circle-fill"></i>
                <span class="option-text">Campinas</span>
            </li>
            <li class="option">
                <i class="bi bi-circle-fill"></i>
                <span class="option-text">Curitiba</span>
            </li>
            <li class="option">
                <i class="bi bi-circle-fill"></i>
                <span class="option-text">Fortaleza</span>
            </li>
            <li class="option">
                <i class="bi bi-circle-fill"></i>
                <span class="option-text">Manaus</span>
            </li>
            <li class="option">
                <i class="bi bi-circle-fill"></i>
                <span class="option-text">Natal</span>
            </li>
            <li class="option">
                <i class="bi bi-circle-fill"></i>
                <span class="option-text">Recife</span>
            </li>
            <li class="option">
                <i class="bi bi-circle-fill"></i>
                <span class="option-text">Rio de Janeiro</span>
            </li>
            <li class="option">
                <i class="bi bi-circle-fill"></i>
                <span class="option-text">Salvador</span>
            </li>
            <li class="option">
                <i class="bi bi-circle-fill"></i>
                <span class="option-text">São Paulo</span>
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: 'CitySelector',
        mounted() {
           
            const optionMenu = document.querySelector(".city-selector-menu"),
                 selectBtn = optionMenu.querySelector(".select-btn"),
                 options = optionMenu.querySelectorAll(".option"),
                 btnText = optionMenu.querySelector(".btn-text");

            selectBtn.addEventListener("click", () => optionMenu.classList.toggle("active"));
            
            Array.from(options).forEach(option => {
                option.addEventListener("click", () => {
                    let selectedOption = option.querySelector(".option-text").innerText;
                    btnText.innerText = selectedOption;

                    optionMenu.classList.remove("active");
                })
            })
           
        }
    }
</script>

<style scoped>
    .select-btn {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background-color: #fff;
        padding: 0.5dvw;
        padding-left: 0.9dvw;
        border-radius: 5px;
        box-shadow: 0 0 2px rgba(136, 136, 136, 0.505);
        cursor: pointer;
        color: rgb(97, 96, 96);
    }
    .select-btn i {
        font-size: 1em;
        color: rgb(117, 117, 117);
        transition: 0.2s;
    }
    .city-selector-menu .options {
        position: absolute;
        max-height: 16dvh; /* Defina a altura máxima desejada para o menu */
        width: 20dvw;
        overflow-y: auto;
        padding: 0.5dvw;
        background-color: #fff;
        border-radius: 2px;
        box-shadow: 0 0 2px rgba(136, 136, 136, 0.505);
        display: none;
        
    }

    .city-selector-menu.active .options {
        display: block;
        
    }

    .city-selector-menu.active .select-btn i {
        transform: rotate(90deg);
    }

    .options .option {
        display: flex;
        cursor: pointer;
        align-items: center;
        padding: 0.5dvw 0;
        background-color: #fff;
        border-radius: 4px;
        color: rgb(141, 141, 141);
        border-bottom: 2px solid #cccccc;
    }

    .options .option:hover {
        background-color: #f2f2f2;
    }

    .option i {
        color: rgb(198, 196, 196);
        margin-right: 8px;
    }
</style>