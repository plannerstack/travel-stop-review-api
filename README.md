# Travel Stop Review API


An API to review travel stops within the Plannerstack environment.

* Retrieves Travel stops from different sources allowing them to be compared
* Possible to update a TravelStop by ID (will be saved in a specific Database)

## Table of content

<!-- MarkdownTOC -->

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running](#running)
	- [Locally](#locally)
	- [In Docker container](#in-docker-container)
	- [Notes](#notes)
- [Usage](#usage)
	- [API Reference](#api-reference)
	- [Examples](#examples)
- [Version](#version)
	- [0.0.1 • 2017-01-26](#001-•-2017-01-26)
- [Third party libraries](#third-party-libraries)
- [Tests](#tests)
- [History](#history)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)
- [Todo's](#todos)

<!-- /MarkdownTOC -->


## Prerequisites

* virtualenv *(optional)*
* docker *(optional)*

## Installation

* Clone this repo and move to its directory
* Create a virualenv if you want to, or use docker-compose
* `pip install -r requirements.txt`

## Running

### Locally

* `python app.py`
* visit: http://0.0.0.0:8888/api/v1/ui/

### In Docker container

`docker-compose up --build`

### Notes

* Currently uses `gevent` to serve, can be switched to `tornado` by changing it in `app.py` and changing the requirements.txt

## Usage

* Swagger UI: http://0.0.0.0:8888/api/v1/ui/
* Raw Swagger 2.0 JSON: http://0.0.0.0:8888/api/v1/swagger.json
* API: http://0.0.0.0:8888/api/v1
	* e.g. http://0.0.0.0:8888/api/v1/travel-stops

### API Reference

See YAML swagger/openapi definition in /openapi directory

### Examples

```
curl --request GET \
  --url 'http://0.0.0.0:8888/api/v1/travel-stops?bbox=37.7902858,-122.4027371;37.7890649,-122.3993039' \
  --header 'accept: application/json' \
```


## Version

### 0.0.1 • 2017-01-26

* Initial version


## Third party libraries

* connexion: automagically handles HTTP requests based on OpenAPI 2.0 Specification of an API 
	* http://connexion.readthedocs.io/en/latest/




## Tests

Found in `/tests`, to run:

* `python -m unittest discover`

## History

Build to start of the Toogethr project development.

## Contributing

Make sure to use pull requests when extending this API

```
# Before starting to touch code
git checkout -b feature/unicorn
# Make nice atomic commits
git commit
# Push back
git push -u origin feature/unicorn
```

## Credits

* Jasper Hartong - Plannerstack - 2017


## License

@todo:

## Todo's

* Implement the actual functions to retrieve data and set data

