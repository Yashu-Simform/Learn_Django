## DRF - Django REST Framework
-   REST - REpresentational State Transfer: It is an architectural design introduced by Roy Fielding based on 6 key principles to ensure smooth communication.
    -   Principlpes:
        -   Resource Represented: Each resource is represented in form of a url.
        -   Stateless Communication: Both Server and Client side works independently. Server does not store the session details also making it independent from Client.
        -   Transfer of Representaions: Each resource object can be transfered into other supported formats like JSON to give it back in response.
        -   Uniform Interface: Support the most common or uniform HTTP calling methods GET, POST, PUT, PATCH and DELETE for Create, Read, Update and Delete operations respectively.
        -   Cacheable Resources: Can define explicitly which recources should be cached.
        -   Layered system: Supports to add multiple layers (e.g. proxies or load balancer) in the architecture independently, without being knowing to client.

### Why we use DRF? (Purpose of DRF)
-   If you want to make server side application independent of client side application and providing you a data service of CRUD over data where Relational objects are represented in specified format while responding to a request.

### Power of DRF:
-   <b>Serialization</b>: If helps to serialize the Python relational objects into the specified formats which can be easily undertandable by the clients.
-   <b>Deserialization</b>: It also supports deserialization which allows the data from client side to get converted into the Python relational objects.
-   <b>Representation</b>: Python relational objects can be converted into JSON, HTML, XML, etc formats easily.
-   <b>Browsable API's</b>: DRF provides a web interface to interact with apis in browsers.

### Serializer:
-   Used to serialize the Python relational objects.
-   It provides an interface between Python objects and data provided by clients.
-   It converts the data coming from client to Python object format and helps to perform db operations directly using serializer only. 


### Request object in DRF:
-   It is a specialized version of HttpRequest Object provided by django.http module.
-   It has taken some functionalities to make easy for developers to access data coming from request by client.
```
Difference between HttpRequest and Request objects:

request.POST    <-  django.http     Used for data coming in POST method only
request.data    <-  rest_framework.request      Used for POST, PUT and PATCH methods

```

### Response object in DRF:
-   It is a specialized version of TemplateResponse object.
-   TemplateResponse objects allows us to edit response before it gets rendered. The template and context will render only when required. Can add middleware to do something with the context or template in response before it gets rendered.
-   Response object of DRF comes with these properties. It gets the information about the required content type by the client and respond accordingly through content negotiation.


### Status code:
-   DRF provide status codes in status.py file, you can access status codes using identifiers from, `from django import status` and then use identifiers to mention status codes `status.HTTP_400_BAD_REQUEST`.


### API views:
-   The views that we declare normally in django takes HttpRequest object as parameter. Now to take the DRF Request object in argument we need to declare them as api views.
-   Two ways to declare a view as api view:
    -   Function based view: 
        -   Use `@api_view` decorator
        -   It takes list of methods as argument: ``` @api_view(['POST', 'GET']) ```  
    -   Class based view:
        -   Use `APIView` class and inherit It.

-   It sends the appropriate status code along with the response and handles the parsing exceptions.