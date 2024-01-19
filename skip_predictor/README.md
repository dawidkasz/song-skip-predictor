# Skip predictor

## Running service

1. Run `cp .env.example .env` to create a required config file.
2. Make sure that you have decision tree and random forest model files under the
paths specified in the `.env` config. By default these are `random_forest.pkl` and `decision_tree.pkl`.
3. Run `docker compose build` to build the microservice with its dependencies (mongodb).
4. Run `docker compose up` to start the microservice.
5. By default, the REST api will be serving on `0.0.0.0:8080`. Go to `0.0.0.0:8080/docs` to see docs.

If you do not want to run service in a container then instead of using `docker compose` run `python3 main.py`.

## Running tests

[Integration tests](test/test_integration) require the same setup as a complete application: `.env` configuration. If you want to run tests locally, outside of the docker container, you can:
1. Run `cp .env.example .env`.
2. Start the default `DB__HOST` value to `localhost`.
3. Run `docker compose -f docker-compose-test.yml up`.
4. Run `pytest` to run the test suites.
