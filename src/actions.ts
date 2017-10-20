import {callApi} from '@src/apis'

export function castVote(vote) {
    return (dispatch) => {
        callApi('votes/', 'POST', {
            decision: vote,
            voter: 'me'
        }).then(res =>
            dispatch({
                type: 'CAST_VOTE',
                vote,
            })
        )
    }
}

export function reset() {
    return dispatch => {
        callApi('votes/reset/', 'POST', {}).then(res => dispatch({
            // type: 'RESET'
            type: 'SHOW_MISSION',
            votes: res.votes,
            number_of_voters: res.number_of_voters
        }))
    }
}

export function setNumberOfVoters(num: number) {
    return dispatch => {
        callApi('votes/reset/', 'POST', {
            number_of_voters: num
        }).then(res => dispatch({
            // type: 'SET_NUMBER_OF_VOTERS',
            // num,
            type: 'SHOW_MISSION',
            votes: res.votes,
            number_of_voters: res.number_of_voters
        }))
    }
}

export function initApp() {
    return dispatch => {
        callApi('missions/show/', 'GET').then(res => {
            dispatch({
                type: 'SHOW_MISSION',
                votes: res.votes,
                number_of_voters: res.number_of_voters
            })
        })
        setTimeout(() => dispatch(initApp()), 2000)
    }
}
