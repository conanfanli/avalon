export function castVote(vote) {
    return {
        type: 'CAST_VOTE',
        vote,
    }
}
