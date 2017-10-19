import * as React from 'react'
import {connect} from 'react-redux'
import {bindActionCreators} from 'redux'

import {RaisedButton} from 'material-ui'
import * as actionCreators from '@src/actions.ts'
import {State, ActionType} from '@src/types'


interface Prop {
    actions: ActionType;
    ballot: Array<boolean>
}

class GameComponent extends React.Component<Prop, any> {
    render() {
        const {ballot, actions} = this.props
        return (
            <div>
                {`${ballot.length}`} voted
                <RaisedButton
                    primary label='Vote Yes'
                    onClick={() => actions.castVote(true)}
                />
                <RaisedButton
                    primary label='Vote No'
                    onClick={() => actions.castVote(false)}
                />
                <RaisedButton secondary fullWidth label='Show Result'
                    onClick={()=>console.log(111)}
                />
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
        actions: bindActionCreators<any>(actionCreators, dispatch),
    }
}
export const Game = connect(
    mapStateToProps,
    mapDispatchToProps
)(GameComponent)
