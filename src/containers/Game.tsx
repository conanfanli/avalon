import * as React from 'react'
import {connect} from 'react-redux'
import {bindActionCreators} from 'redux'

import {Chip, FlatButton, RaisedButton} from 'material-ui'
import * as actionCreators from '@src/actions.ts'
import {State, ActionType} from '@src/types'


interface Prop {
    actions: ActionType;
    ballot: Array<boolean>
}

class GameComponent extends React.Component<Prop, {showBallot: boolean}> {
    state = {
        showBallot: false
    }

    reset() {
        this.setState({showBallot: false})
        this.props.actions.reset()
    }

    render() {
        const {ballot, actions} = this.props
        const text = this.state.showBallot ? `${ballot}` : `${ballot.length} have voted`
        return (
            <div>
                <Chip>{text}</Chip>
                <FlatButton
                    primary label='Vote Yes' fullWidth
                    onClick={() => actions.castVote(true)}
                />
                <RaisedButton
                    primary label='Vote No' fullWidth
                    onClick={() => actions.castVote(false)}
                />
                <RaisedButton secondary fullWidth label='Show Result'
                    onClick={() => this.setState({showBallot: true})}
                />
                <FlatButton
                    primary label='Reset' fullWidth
                    onClick={this.reset.bind(this)}
                />
            </div>
        )
    }
}

const mapStateToProps = (state: State, ownProps) => {
    return {
        ballot: state.ballot,
        numberOfVoters: state.numberOfVoters,
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
