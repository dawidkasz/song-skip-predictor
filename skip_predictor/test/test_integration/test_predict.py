from fastapi import status

from src.predictor.predictor_model_provider import (
    decision_tree_model,
    provide_random_model,
    random_forest_model,
)


def test_model_predicts_using_random_forest_model(
    api_client, raw_model_payload, override_dependency
):
    with override_dependency({provide_random_model: lambda: random_forest_model}):
        response = api_client.post("/predict", json=raw_model_payload)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"isskipped": True}


def test_model_predicts_using_decision_tree_model(
    api_client, raw_model_payload, override_dependency
):
    with override_dependency({provide_random_model: lambda: decision_tree_model}):
        response = api_client.post("/predict", json=raw_model_payload)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"isskipped": True}


def test_model_predictions_are_saved_during_ab_test(
    api_client, raw_model_payload, mongo_predictions
):
    api_client.post("/predict", json=raw_model_payload)
    api_client.post("/predict", json=raw_model_payload)

    saved_predictions = list(mongo_predictions.find({}))

    assert len(saved_predictions) == 2

    assert (
        saved_predictions[0]["input"]
        == saved_predictions[0]["input"]
        == raw_model_payload
    )

    assert saved_predictions[0]["model"] in ["random_forest", "decision_tree"]
    assert saved_predictions[1]["model"] in ["random_forest", "decision_tree"]

    assert saved_predictions[0]["output"] == {"isskipped": True}
    assert saved_predictions[1]["output"] == {"isskipped": True}
