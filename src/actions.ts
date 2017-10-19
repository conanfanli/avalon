export function castVote(vote) {
    return {
        type: 'CAST_VOTE',
        vote,
    }
}

export function reset() {
    return {
        type: 'RESET',
    }
}

export function setNumberOfVoters(num: number) {
    return {
        type: 'SET_NUMBER_OF_VOTERS',
        num,
    }
}
