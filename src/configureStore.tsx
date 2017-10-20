import logger from 'redux-logger'
import thunk from 'redux-thunk'
import reducers from './reducers'
import { createStore, applyMiddleware } from 'redux'
import { routerMiddleware } from 'react-router-redux'
import {initApp} from '@src/actions'

const middleware = process.env.NODE_ENV === 'production' ?
  [ thunk ] :
  [ thunk, logger() ]


export const configureStore = (history) => {
    const store = createStore(
        reducers,
        applyMiddleware(...middleware, routerMiddleware(history))
    )

    store.dispatch<any>(initApp())

    return store
}
