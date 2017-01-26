import unittest
import copy
import json
import connexion
from api.travel_stops import travel_stop_fixture


path_prefix = '/api/v1'

class SimpleStatusCodesTestCase(unittest.TestCase):
    """
        As the Connexion framework already does request and response validation
            we only make assertions on status codes here for now.
            As soon as the response or the request is not formatted correctly
            the status_code will deviate from a 200

            Tips & Tricks:
            - print(response.get_data())
    """

    def setUp(self):
        app = connexion.App(__name__, specification_dir='../openapi/', server='gevent')
        app.add_api('openapi.yaml', validate_responses=True)
        self.app_client = app.app.test_client()

    """
        Tests
    """

    def test_get_travel_stops_in_bbox(self):
        response = self.app_client.get(path_prefix+'/travel-stops?bbox=37.7902858,-122.4027371;37.7890649,-122.3993039')
        assert response.status_code == 200

    def test_put_travel_stop(self):
        response = self.app_client.put(path_prefix+'/travel-stops/TESTID',
            data=json.dumps(travel_stop_fixture),
            content_type = 'application/json')
        print(response)
        assert response.status_code == 200