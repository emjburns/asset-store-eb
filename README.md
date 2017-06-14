## Running

```
pip install -r requirements.txt
python run.py
```
Or debug mode:

```
APP_DEBUG=true python run.py
```

## Assumptions
- No database, this will store in memory. This won't scale, but is a start.


## REST
While running, please visit `http://localhost:5000/api/spec.html` to test out using Swagger.

## Structure
```
Asset {
  name: string
    - alphanumeric ascii characters, underscores, and dashes
    - globally unique
    - cannot start with underscore or dashe
    - 4-64 chars log
  type: string
    - "satellite" or "antenna"
  class: string, depends on type
    - "satellite" assets - "dove" or "rapideye"
    - "antenna" assets - "dish" or "yagi"
}
```

APIS:
- POST /v1/asset
  body: name, type, class
- GET /v1/asset
  get whole list of assets
- GET/v1/asset/{name}
  get details about asset

## Adapted from
Adapted from [flask-good-start](https://github.com/Cogniteinc/flask-good-start)



All application code including tests, endpoints, response models, and routes are
contained in the `app` directory. `app.py` is solely for defining the services
the app should be run by using `run.py`.

`resources` contains the endpoint implementations (i.e. HTTP `PUT`s and `GET`s etc.)

`tests` uses standard `unittest` libraries and the Flask `test_client`. See [Flask Testing](http://flask.pocoo.org/docs/0.12/testing/)
for more.

`utils` can contain any utility helpers for running the app. Right now it contains a logging implementation. See below for more.

Feel free to create other directories for things you need like [dao](https://en.wikipedia.org/wiki/Data_access_object_) or [models](http://flask-sqlalchemy.pocoo.org/2.1/models/).


### Production / Deployment

For production use we want a more flexible, scalable server to run our code. [Gunicorn](http://gunicorn.org/) is a popular one. This is included already in your `requirements.txt` so you just have to launch it via command line to test "production like" behavior. Feel free to read docs and change options to fit your use case.

Here's a basic command to launch the gunicorn server in a similar state to the development configuration. Notice it points to the `app` object in your `app.app` module.

```
gunicorn -b 0.0.0.0:5000 app.app:app
```

## Testing

Standard [Python unittest framework](https://docs.python.org/3/library/unittest.html) is used in this project. This is a good, out of the box starting point. Out of the box [Test Discovery](https://docs.python.org/3/library/unittest.html#test-discovery) is used to run tests here.

This is meant to evolve with the project. Use of Mocks and Test Suites will be useful to know how to use as your project grows.

To "discover" and run tests:

```
python -m unittest
```

## Logging

We use standard python logging and `structlog` package to get good structured log messages. The `logging.yaml` file controls the loggers and handlers. This is relatively self-documenting. If it doesn't make sense to you, read on [Python Logging](https://docs.python.org/3/howto/logging.html) and [best practices](https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/) before making changes.

`ERROR` and `CRITICAL` levels are printed to stderr, everything else is printed to stdout. On your console you won't see a difference, this is primarily for sophisticated log streaming in production.

### Structlog
All this does is create nice, key-value or JSON output and provide a user friendly logging interface for you to drop complex data in. There is an example in `healthcheck.py` resource for reference.

## Swagger

The `flask-restful-swagger` package was added to aid in providing automatic API documentation for services. *This plugin is experimental in this case* and just an illustration of how swagger can be used to aid in documentation of services. It may be replaced by a different swagger implementation or something else altogether in the future.

Currently `healthcheck.py` has an example annotation for the endpoint. When the app runs `http://localhost:5000/api/spec.json` provides the Swagger spec and `http://localhost:5000/api/spec.html` provides an html documentation view.
