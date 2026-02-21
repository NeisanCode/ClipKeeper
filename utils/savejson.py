import json


def save_clip(content, timestamp):
    clip = {"content": content, "timestamp": timestamp}

    try:
        with open("data/clips.json", "r") as file:
            clips = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        clips = []

    clips.append(clip)

    with open("data/clips.json", "w") as file:
        json.dump(clips, file, indent=4)


def load_clips():
    try:
        with open("data/clips.json", "r") as file:
            clips = json.load(file)
            return clips
    except FileNotFoundError:
        return []


def clear_clips():
    with open("data/clips.json", "w") as file:
        json.dump([], file, indent=4)
