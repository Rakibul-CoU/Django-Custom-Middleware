A middleware is a class (or function) integrated into the request/response lifecycle in a Django application. Middlewares are called twice in the life cycle of the application: for requests, before carrying out the routing and the call of the views; for responses, before returning the response to the web server. Each request/response will be processed by all the middlewares in the order provided by the project.

Middlewares make it possible to add certain functionalities and to carry out operations on the requests/responses before continuing their journey. It is a very efficient and very flexible tool.

By default, Django integrates several middlewares allowing to ensure the authentication of the request, the respect of certain security mechanisms (CSRF, XSS…) or even the increase of the response with specific features (internationalization, messages...).

There are many reasons for adding custom middleware. They offer great flexibility for adding specific features to your application, without any particular complexity.

For example, a personalized middleware can make it possible to add request pre-processing operations, to check requests parameters, to record statistics, to improve error management or even to connect to an external API…
