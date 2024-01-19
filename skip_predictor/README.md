# Skip predictor

## Running service

1. Run `cp .env.example .env` to create a required config file.
2. Make sure that you have decision tree and random forest model files under the
paths specified in the `.env` config. By default these are `random_forest.pkl` and `decision_tree.pkl`.
3. Run `docker compose build` to build the microservice with its dependencies.
4. Run `docker compose up` to start the microservice.
5. By default, the REST api will be serving on `0.0.0.0:8080`. Go to `0.0.0.0:8080/docs` to see docs.
