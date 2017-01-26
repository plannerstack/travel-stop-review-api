"""
    THE MAIN APP

    - Loads a yaml file describing the API in swagger/OpenAPI 2.0
    - Links endpoints to functions in modules with the "operationId" declaration in the yaml
    - Serves:
        - The endpoints on their declared path: e.g.    http://0.0.0.0:8888/api/v1/travel-intents/
        - The Interactive Swagger UI:                   http://0.0.0.0:8888/api/v1/ui/
        - The raw swagger JSON:                         http://0.0.0.0:8888/api/v1/swagger.json
    - Served by "gevent"

    Run this main app with: `python app.py`
"""

import connexion

if __name__ == '__main__':
    # Config app
    app = connexion.App(__name__, specification_dir='openapi/', server='gevent')
    # Add API yaml file
    app.add_api('openapi.yaml', validate_responses=True)
    # Run
    print("RUN: http://0.0.0.0:8888/api/v1/ui/")
    app.run(port=8888)
