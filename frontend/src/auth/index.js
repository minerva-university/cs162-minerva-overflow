import {createAuthProvider} from 'react-token-auth';

export const {useAuth, authFetch, login, logout} =
    createAuthProvider({
        getAccessToken: 'access_token',
        onUpdateToken: (token) => fetch('/api/refresh', {
            method: 'POST',
            body: token.access_token
        })
        .then(r => r.json())
    });


