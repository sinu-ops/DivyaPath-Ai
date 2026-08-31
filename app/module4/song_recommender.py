import pandas as pd
from pathlib import Path
import random

# Path to mood-song dataset
DATA_PATH = Path("C:/Users/yshel/Desktop/DivyaPath-Ai/data/mood_song.csv")

# Load once
songs_df = pd.read_csv(DATA_PATH)

# Normalize text
songs_df["mood"] = songs_df["mood"].str.lower().str.strip()
songs_df["category"] = songs_df["category"].str.lower().str.strip()

# Emotion → Mood mapping
EMOTION_TO_MOOD = {
    "happy": ["happy", "energy", "motivation"],
    "sad": ["sad", "calm"],
    "angry": ["energy", "motivation"],
    "neutral": ["focus", "calm"],
    "fear": ["calm"],
    "surprise": ["energy", "happy"],
    "disgust": ["calm"]
}

def recommend_songs(emotion, n=5):
    """
    Given detected emotion, return n recommended songs.
    """
    emotion = emotion.lower().strip()

    moods = EMOTION_TO_MOOD.get(emotion, ["calm"])

    # Filter songs by mapped moods or categories
    filtered = songs_df[
        songs_df["mood"].isin(moods) |
        songs_df["category"].isin(moods)
    ]

    if filtered.empty:
        # fallback
        filtered = songs_df.sample(min(n, len(songs_df)))

    # Randomly select songs
    sample = filtered.sample(min(n, len(filtered)))

    recommendations = []
    for _, row in sample.iterrows():
        recommendations.append({
            "song": row["song"],
            "artist": row["artist"],
            "mood": row["mood"],
            "category": row["category"],
            "language": row.get("language", "")
        })

    return recommendations


# Quick local test
if __name__ == "__main__":
    demo = recommend_songs("sad")
    for s in demo:
        print(f"{s['song']} - {s['artist']} ({s['mood']})")
