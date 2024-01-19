import pandas as pd
from sklearn.preprocessing import LabelEncoder


def preprocess_dataset(df: pd.DataFrame):
    final_dataset = df.dropna()
    label_encoder = LabelEncoder()
    final_dataset["city"] = label_encoder.fit_transform(final_dataset["city"])

    final_dataset["day"] = final_dataset["timestamp"].dt.dayofyear
    final_dataset["hourminute"] = (
        final_dataset["timestamp"].dt.hour * 60 + final_dataset["timestamp"].dt.minute
    )
    final_dataset["date_completeness"] = label_encoder.fit_transform(
        final_dataset["date_completeness"]
    )

    # IMPORTANT DROP FOR LEAKAGE
    final_dataset = final_dataset.drop(columns=["block_duration", "song_listened"])

    final_dataset["session_duration"] = final_dataset["session_duration"].apply(
        lambda x: x.total_seconds()
    )
    final_dataset["user_listen_time"] = final_dataset["user_listen_time"].apply(
        lambda x: x.total_seconds()
    )

    final_dataset["premium_user"] = final_dataset["premium_user"].astype(int)
    final_dataset["isliked"] = final_dataset["isliked"].astype(int)
    final_dataset["isskipped"] = final_dataset["isskipped"].astype(int)
    final_dataset["previous_action"] = (
        final_dataset["previous_action"].astype(bool).astype(int)
    )

    return final_dataset.drop(
        columns=[
            "timestamp",
            "street",
            "name",
            "favourite_genres",
            "genres",
            "session_id",
            "track_id",
            "user_id",
            "id_artist",
        ]
    )
