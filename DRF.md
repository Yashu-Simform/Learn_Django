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

### Serializer:
-   Used to serialize the Python relational objects.
-   It provides an interface between Python objects and data provided by clients.
-   It converts the data coming from client to Python object format and helps to perform db operations directly using serializer only. 