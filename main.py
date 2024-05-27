import requests

url = "https://www.veed.io/text-to-music-ap/api/text-to-music"

try:
    prompt = input("Enter the prompt: ")
    duration = int(input("Enter the duration in seconds: "))
    print(f"Generating music for prompt: {prompt} and duration: {duration} seconds")
    print("\n\n\n")

    payload = {
        "prompt": prompt,
        "vibe": "Chill",
        "duration": duration
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        with open('music.mp3', 'wb') as file:
            file.write(response.content)
        print("Request was successful")
        print("Audio file saved as 'music.mp3'")
    else:
        print("Failed to get a successful response")
        print("Status code:", response.status_code)
        print("Response text:", response.text)
except ValueError:
    print("Please enter a valid duration (an integer).")
except requests.exceptions.RequestException as e:
    print("An error occurred while making the request")
    print("Error:", str(e))
