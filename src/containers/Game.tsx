import * as React from 'react'
import {connect} from 'react-redux'
// import {bindActionCreators} from 'redux'

// import * as actionCreators from '@src/actions.ts'
//
import {State} from '@src/types'


class GameComponent extends React.Component<any, any> {
    render() {
        return (
            <div>
                5 people have voted
            </div>
        )
    }
}

const mapStateToProps = (state: State, ownProps) => {
    return {
        ballot: state.ballot
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        //       actions: bindActionCreators<any>(actionCreators, dispatch),
    }
}
export const Game = connect(
    mapStateToProps,
    mapDispatchToProps
)(GameComponent)
