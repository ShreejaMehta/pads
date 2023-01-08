# Potentially Accurate Dialogue Synthesis

This project is a demonstration of converting speech to text based dialogues. For the purpose of demonstration, a sample audio file *sampleaudio.wave* has been used.
The program produces three outputs based on different models from which the user can choose the closest output. 

### Dependencies required
+ [ffmpeg](https://ffmpeg.org/download.html) - working with audio files

```
# Debian based
sudo apt-get install ffmpeg

# Arch based
sudo pacman -S ffmpeg
```

+ [pipenv](https://pypi.org/project/pipenv/) - virtual env for package management
```
pip install pipenv
```

### Working 

1. Get to the project source folder  
```
pipenv shell
```

2. Once inside pipenv shell
```
pipenv install
```
This will install all python requirements(you only have to do it once)

3. While inside the pipenv shell, run the program by
```
python main.py AUDIO_FILE_PATH
```
OR
once you have set up the requirements 
```
pipenv run python main.py AUDIO_FILE_PATH
```
