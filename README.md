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

