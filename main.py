import click
from pathlib import Path
import ffmpeg
from models.interface import runner
from pick import pick
import os

@click.command()
@click.argument("filepath")
def main(filepath: str):
    print(filepath)
    filename = filepath.split("/")[-1]

    # Check if file exists
    if not Path(filepath).exists():
        print(f"[Error] {filepath} not found!")
        exit()

    filename_stem, filename_ext = filename.split(".", 1)

    # Place it in current directory if already .wav
    # Or convert it into .wav file and place it in current dir
    # TODO: Don't process it if already .wav
    output_filename = f"tmp_{filename}"
    if filename_ext != "wav":
        output_filename = f"tmp_{filename_stem}.wav"

    stream = ffmpeg.input(filepath)
    stream = ffmpeg.output(stream, output_filename, loglevel="quiet") # Remove "quite" for debugging

    print("Loading audio file...")
    ffmpeg.run(stream, overwrite_output=True)

    # Spinning threads!
    result = runner(Path(f"./{output_filename}"))

    title = "Select the closest matching query: -"
    option, index = pick(result, title)
    print(option)

    # Remove the temporary file
    os.remove(output_filename)
if __name__ == '__main__':
    main()
