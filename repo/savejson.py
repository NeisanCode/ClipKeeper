from datetime import datetime
import json
from os import times


def save_clip(content):
    try:
        with open("repo/clips.json", "r") as file:
            clips = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        clips = []
    timestamp = datetime.now().isoformat()
    clip = {
        "content": content,
        "timestamp": timestamp,
        "id": max([clip["id"] for clip in clips]) + 1 if clips else 1,
    }
    clips.append(clip)
    with open("repo/clips.json", "w") as file:
        json.dump(clips, file, indent=4)


def load_clips():
    try:
        with open("repo/clips.json", "r") as file:
            clips = json.load(file)
            return clips
    except FileNotFoundError:
        return []


def clear_clips():
    with open("repo/clips.json", "w") as file:
        json.dump([], file, indent=4)
