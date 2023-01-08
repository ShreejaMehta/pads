import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from time import sleep


def whisper_model(filepath: Path) -> str:
    return "WHISPER RESULT"


def sphinx_model(filepath: Path) -> str:
    return "SPHINX RESULT"


def wave2vec2_model(filepath: Path) -> str:
    return "WAVE2VEC2 RESULT"


def runner(filepath: Path) -> [str]:

    res = []

    with ThreadPoolExecutor(max_workers=3) as executor:
        whisper = executor.submit(whisper_model, filepath)
        sphinx = executor.submit(sphinx_model, filepath)
        wave2vec2 = executor.submit(wave2vec2_model, filepath)

        res = [whisper.result(), sphinx.result(), wave2vec2.result()]

    return res

