
export const BASE_URL = `${window.location.protocol}//${window.location.hostname}:${window.location.port ? '8000': ''}/api/v1`


export function callApi(url: string, method: string, data: any = null, is_ajax:boolean = true) {
    const jwt = sessionStorage.getItem('jwt')
    let call = fetch(`${BASE_URL}/${url}`, {
        method: method,
        body: data ? JSON.stringify(data) : null,
        // credentials: 'include',
        headers: is_ajax ? {
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            Authorization: jwt ? `JWT ${jwt}` : null,
        }: null
    })
    return call.then(response => {
        if (response.ok) {
            return response.json()
        } else {
            throw response
        }
    })
}
