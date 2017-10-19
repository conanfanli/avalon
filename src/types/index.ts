import * as actionCreators from '@src/actions'

export type ActionType = typeof actionCreators

export interface State {
    ballot: Array<boolean>;
}
