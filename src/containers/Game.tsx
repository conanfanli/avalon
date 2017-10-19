import * as React from 'react'
import {connect} from 'react-redux'
import {bindActionCreators} from 'redux'

import {Chip, TextField, FlatButton, RaisedButton} from 'material-ui'
import * as actionCreators from '@src/actions.ts'
import {State, ActionType} from '@src/types'


interface Prop {
    actions: ActionType;
    ballot: Array<boolean>;
    numberOfVoters: number;
}

class GameComponent extends React.Component<Prop, {showBallot: boolean}> {
    state = {
        showBallot: false
    }

    reset() {
        this.setState({showBallot: false})
        this.props.actions.reset()
    }

    setNumberOfVoters(event, newValue) {
        this.reset()
        this.props.actions.setNumberOfVoters(newValue)
    }

    render() {
        const {ballot, actions, numberOfVoters} = this.props
        const text = this.state.showBallot ? `${ballot}` : `${ballot.length} have voted`
        const finished = !!(numberOfVoters && (ballot.length == numberOfVoters))
        return (
            <div>
                <TextField
                    floatingLabelText="Number of Voters"
                    type='number'
                    onChange={this.setNumberOfVoters.bind(this)}
                />
                <Chip>{text}</Chip>
                <FlatButton
                    primary label='Succeed' fullWidth disabled={finished}
                    onClick={() => actions.castVote(true)}
                />
                <RaisedButton
                    primary label='Fail' fullWidth disabled={finished}
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
