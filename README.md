# Text-to-Music API Client

This script sends a request to the Text-to-Music API provided by Veed to generate a music file based on a given prompt and duration. It then saves the generated music as an MP3 file.

## Prerequisites

- Python 3.x
- requests library (`pip install requests`)

## Usage

1. Clone or download the repository.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the script `main.py`.
4. Follow the prompts to enter the desired prompt and duration in seconds.

## Parameters

- **Prompt:** The text prompt that describes the mood or theme of the music.
- **Duration:** The duration of the generated music in seconds. Note that 1 represents 1 second and 30 represents 30 seconds.

## Example

```bash
$ python text_to_music.py
Enter the prompt: calm beat
Enter the duration in seconds: 30
```

## Output

The script will save the generated music file as `music.mp3` in the current directory.

