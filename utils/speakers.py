import os
import json


def make_speakers_json_path(out_path):
    """Returns conventional speakers.json location."""
    return os.path.join(out_path, "speakers.json")


def load_speaker_mapping(out_path):
    """Loads speaker mapping if already present."""
    try:
        with open(make_speakers_json_path(out_path)) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_speaker_mapping(out_path, speaker_mapping):
    """Saves speaker mapping if not yet present."""
    speakers_json_path = make_speakers_json_path(out_path)
    with open(speakers_json_path, "w") as f:
        json.dump(speaker_mapping, f, indent=4)


def copy_speaker_mapping(out_path_a, out_path_b):
    """Copies a speaker mapping when restoring a model from a previous path."""
    speaker_mapping = load_speaker_mapping(out_path_a)
    if speaker_mapping is not None:
        save_speaker_mapping(out_path_b, speaker_mapping)