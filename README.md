# Django - A Web Framework


## HTTP Status codes: ['status codes'](https://gist.github.com/sandrabosk/d125177b31eca8dc3e5c524e703ba94d)

## Types of Objects a Django View Method Can Return

In Django, view methods are expected to return specific types of objects. Below is a list of the commonly returned objects:

### 1. HttpResponse or its Subclasses
- `HttpResponse`: The basic HTTP response object.
- `JsonResponse`: For sending JSON data.
- `FileResponse`: For serving files.
- `StreamingHttpResponse`: For streaming large responses.

### 2. Redirect Responses
- `HttpResponseRedirect`: For temporary redirects.
- `HttpResponsePermanentRedirect`: For permanent redirects.

### 3. Django Shortcut Responses
- `render()`: Combines a template and context into an `HttpResponse`.
- `redirect()`: A shortcut for creating a redirect response.

### 4. Django Exceptions (Handled by Middleware)
- `Http404`: Indicates that a requested resource is not found.
- `PermissionDenied`: Indicates that the user is not authorized to access a resource.
- `SuspiciousOperation`: For invalid or potentially harmful user input.

### 5. Callable Objects
A callable object or function that returns an `HttpResponse`. For instance, class-based views or middleware may return such responses.

### 6. None (Specific to Middleware and Class-Based Views)
Certain methods like `dispatch()` in class-based views or custom middleware can return `None` if they don’t directly generate a response. Django ensures an appropriate response is eventually returned.

**Note:** Returning anything other than the listed objects will result in an error.

DRF - [Django REST Framework]('DRF.md')

### Token based authorization:
-   Token is used for authorization not for authentication.
-   Token is passed along with the header to see that user requesting to server is the actual user that has logged in to the application at browser.
-   Process:
    -   When the user logged in the server generate a JWT - JSON web Token and a secret key(stored at server side only) and send JWT token to the client which is going to be stored in browser memory in cache or somewhere.
    -   Now this JWT token has hashed data that server has sent to use it whenever the client requests to the server.
    -   When user make a request to server this JWT token is passed along with header and server receives it and try to validate it using secret key.
    -   If the JWT token is validated then user is authorized.
    -   This JWT token is sent along with some expiration time.
-   JWT token format:
    -   JWT token is divided into 3 parts: header, payload, verification(or signature) key
    -   JWT token: 
        ```
            eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c

            header                              | payload                                                                    | Verification or signature key
        ```
    -   refer: [ref](https://jwt.io/)

    -   A hashing algorithm is used to generate JWT token as: f'{base64_encode(header)}.{base64_encode(payload)}.{secret_key}'
    -   Header portion includes two important information: 
        -   Algorithm to be used for hashing: alg
        -   Type of token to be used: typ
        ```
            {   
                "alg": "HS256",
                "typ": "JWT"
            }
        ```
        -    Payload is the information that server wants to keep at client side and wants it along with the request.
        -   secret key: 
            -   First two parts are used and gets hashed using some algorithm and a secret key is generated.
            -   Thus a secret key is specific to header and payload.

    - server side validation:
        -   `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.secret_key` here the first 2 parts of JWT token {header and payload} are hashed using some algorithm and a signature key is generated.
        -   This generated signature key is then matched with the secret key stored at server side if it matches then server knows that it is the authenticated user otherwise not.
        -    If there is any change in first two part, signature key generated will be different from that is stored in server. 