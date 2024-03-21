import { createStore } from "vuex";

export default createStore ({
    state: {
        showInfo: false,
        cheaperInfo: null,
        confortInfo: null,
    },
    mutations: {
        setShowInfo(state) {
            state.showInfo = !state.showInfo
        },
        setCheaperInfo(state, payload) {
            state.cheaperInfo = payload
        },
        setConfortInfo(state, payload) {
            state.confortInfo = payload
        }
    }
})
