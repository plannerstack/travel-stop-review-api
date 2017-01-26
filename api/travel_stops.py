"""
TRAVEL STOP API HANDLER

Public facing API, currently offers:

    - GET request to retrieve Travel Stops
    - PUT request to create/adjust a Travel Stop

"""


# A fixture that complies with the YAML serializers (just copied and adjusted from http://0.0.0.0:8888/api/v1/ui/)
# - Also handy to use as base if you want to try out the PUT Request
# - Also used in tests

travel_stop_fixture = {
  "type": "Point",
  "coordinates": [ 0,0 ],
  "properties": {
    "id": "MyFixtureID",
    "code": "1A|",
    "contact_email": "string",
    "created": "2017-01-26T10:06:12.869Z",
    "modified": "2017-01-26T10:06:12.869Z",
    "route_id": "MyFixtureRouteID",
    "source": "MyFixtureSourceDB"
  }
}

# Fake 'storage': used to return and store fixtures
travel_stops = {
    'MyFixtureID': travel_stop_fixture
}

def get (bbox):
    """
        implement me:
        bbox = "37.7902858,-122.4027371;37.7890649,-122.3993039"
    """
    return { 'data': [t[1] for t in travel_stops.items()], 'metadata': {'count':len(travel_stops.keys())}}, 200


def put (id, travel_stop):
    """
        Takes incoming travel_stop data and adds it to mapping, with count as id.
        - Also adjusts the source key

        implement me:
        id = string
        travel_stop = fixture like, also see yaml
    """
    travel_stop['source'] = "otherDB"
    travel_stop['id'] = id
    travel_stops[id] = travel_stop
    
    return travel_stop, 200
