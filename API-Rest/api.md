# API Rest - What is it?

## API - Application Programming Interface

- I send a request and wait for a response
- APIs communicate with each other by different means: they can return anything data to status
- We develop now functionalities
- Easier to integrate, hence, easier to change between APIs
- Better performance

## API Types

- Public: we can acces its endpoint without any authentication
- Private: usually works in private systems, such as entrerprise systems
- Third party: its usually marketed and offered as a license to use the service

## Communication using API

- Usually made with `.xml` or `.json`. Simplier file types to use
- Requests are made through HTTP

## HTTP verbs

- GET: get a item
- POST: send an item
- DELETE: delete an item from the database
- PUT: update an item
- PATCH: update partially an item

## What is an endpoint?

- It's an API url tha we access to get a response
- Uses the API's domain or just another
- Those techniques are useful to reduce project's complexity and apply the REST standard

## What is a REST API

- Architecture conventions related to APIs and HTTP protocol
- It's basically a standard to make high quality APIs
- Those are the characteristics that a RESTful API has: 
    - Uniformity: the same endpoint must return the same items to different requests
    - Decoupling: the API should be independent from the front-end application
    - Stateless: the requests are unique and independent and saves must be done by the side which made the request
    - Cache: use of cache system to improve the access speed
    - Layered Architecture: code hierarchy must be followed
    - Code on demand: some code must be runned on demand
