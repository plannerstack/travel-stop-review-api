"""
TRAVEL STOP API HANDLER

Public facing API, currently offers:

    - GET request to retrieve Travel Stops
    - PUT request to create/adjust a Travel Stop

"""
import csv
import copy

# A fixture that complies with the YAML serializers (just copied and adjusted from http://0.0.0.0:8888/api/v1/ui/)
# - Also handy to use as base if you want to try out the PUT Request
# - Also used in tests



travel_stop_fixture = {
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [0,0]
  },
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
travel_stops = {}

def set_fixtures():
    stops = open('/code/api/stops.txt', 'rb')
    stop_id = 0
    stop_code = 1
    stop_name = 2
    stop_lat = 3
    stop_lon = 4
    location_type = 5
    parent_station =6
    stop_timezone = 7
    wheelchair_boarding = 8
    platform_code = 8
    zone_id =10

    skip_first = True
    for row in csv.reader(stops):
        if skip_first:
            skip_first = False
            continue
        if not row[stop_lat] or not row[stop_lon]:
            # No lat lon
            continue
        fixture = copy.deepcopy(travel_stop_fixture)
        fixture['properties']['id'] = row[stop_id]
        fixture['properties']['code'] = row[stop_code]
        fixture['geometry']['coordinates'] = [float(row[stop_lon]), float(row[stop_lat])]
        fixture['route_id'] = row[stop_name]
        travel_stops[row[stop_id]] = fixture

set_fixtures()


def get (bbox):
    """
        implement me:
        bbox = "52.5961812,4.8997355;52.0029709,5.8053975"
    """
    topleft, bottomright = bbox.split(';')
    topleft_lat, topleft_lon = [float(x) for x in topleft.split(",")]
    bottomright_lat, bottomright_lon = [float(x) for x in bottomright.split(",")]
    results = []
    for key, item in travel_stops.iteritems():
        between_lon = (topleft_lon <= item["geometry"]["coordinates"][0] <= bottomright_lon)
        between_lat = (bottomright_lat <= item["geometry"]["coordinates"][1] <= topleft_lat)
        if between_lat and between_lon:
            results.append(item)


    return { 'data': results, 'metadata': {'count':len(results)}}, 200


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
