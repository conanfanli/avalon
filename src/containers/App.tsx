
// Libs
import * as React from 'react'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'
import { Provider } from 'react-redux'
import {Route} from 'react-router-dom'
// import {bindActionCreators} from 'redux'
import {connect} from 'react-redux'
import { ConnectedRouter } from 'react-router-redux'

class HomeContainer extends React.Component<any, any> {

    render() {
        return (
            <div>
                current room: 1234
            </div>
        )
    }
}


const mapStateToProps = (state): {} => {
    return {
    }
}
const mapDispatchToProps = (dispatch) => {
    return {
        // actions: bindActionCreators<any>(actionCreators, dispatch),
    }
}

export const AppComponent = connect(
    mapStateToProps,
    mapDispatchToProps
)(HomeContainer)

export const App = ({store, history}) => {
    return <Provider store={store}>
        <MuiThemeProvider>
            <ConnectedRouter history={history}>
                <Route path="/" component={AppComponent}/>
            </ConnectedRouter>
        </MuiThemeProvider>
    </Provider>
}
