## Running

```
pip install -r requirements.txt
python run.py
```

## Swagger 
While running, please visit `http://localhost:5000/api/spec.html` to test out using Swagger.


## Testing

To "discover" and run tests:

```
python -m unittest discover
```

## Improvements
I've used an in-memory database (dict) for simplicity. The AssetStore class provides an abstraction for it.
The next step I'd take is replacing the dict with an actual database so that information is persisted.
This could easily be built in to the AssetStore class without changing any other code.

Right now we have two different types of assets (satellites and antennas). Currently they're represented
with one class, since they aren't very different. The next step I'd take is abstracting this to a base asset class with child classes representing the specific type of asset. Each child would handle its specific validation and methods. This would allow the types of assets to be managed easily and grow as the project grows.

I've defined all my tests in one file, since this project is small. The next step I'd take is
moving these to separate files based on the API endpoint so that as the project grows
it's easier to maintain the tests and run them separately.

## Structure
```
Asset {
  assetName: string
    - alphanumeric ascii characters, underscores, and dashes
    - globally unique
    - cannot start with underscore or dash
    - 4-64 chars log
  assetType: string
    - "satellite" or "antenna"
  assetClass: string, depends on type
    - "satellite" assets - "dove" or "rapideye"
    - "antenna" assets - "dish" or "yagi"
}
```

APIS:
- GET /v1/assets
  list of all assets
- POST /v1/asset/{name}    
  body: assetType, assetClass   
  create asset
- GET/v1/asset/{name}    
  get specific asset

## Adapted from
Adapted from [flask-good-start](https://github.com/Cogniteinc/flask-good-start).
Since I'm new to Python, I've started with a skeleton project. I've kept the
logging and layout of this sample. All code for solving the problem is my own.

## Layout

All application code including tests, endpoints, response models, and routes are
contained in the `app` directory. `app.py` is solely for defining the services
the app should be run by using `run.py`.

`resources` contains the endpoint implementations (i.e. HTTP `PUT`s and `GET`s etc.)

`tests` uses standard `unittest` libraries and the Flask `test_client`.

`utils` contains a logging implementation.
