import { combineReducers } from 'redux'
import { routerReducer } from 'react-router-redux'
import {State} from '@src/types'
// import u from 'updeep'


export const initialState: State = {
    ballot: []
}

function createReducer(initialState, handlers) {
    return function reducer(state = initialState, action) {
        if (handlers.hasOwnProperty(action.type)) {
            return handlers[action.type](state, action)
        } else {
            return state
        }
    }
}

const ballot = createReducer(initialState.ballot, {
    CAST_VOTE: (state, action) => {
        return [...state, action.vote]
    },
    RESET: (state, action) => {
        return []
    }
})



const reducers = combineReducers({
    ballot,
    router: routerReducer,
})


export default reducers
