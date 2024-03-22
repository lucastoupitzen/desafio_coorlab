import { createStore } from "vuex";

export default createStore ({
    state: {
        showInfo: false,
        cheaperInfo: null,
        confortInfo: null,
        showAlert: false,
    },
    mutations: {
        setShowInfoTrue(state) {
            state.showInfo = true
        },
        setShowInfoFalse(state) {
            state.showInfo = false
        },
        setCheaperInfo(state, payload) {
            state.cheaperInfo = payload
        },
        setConfortInfo(state, payload) {
            state.confortInfo = payload
        },
        setShowAlertTrue(state) {
            state.showAlert = true
        },
        setShowAlertFalse(state) {
            state.showAlert = false
        }
    }
})
