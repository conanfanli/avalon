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