# Text-to-Speech Project

A Python project that converts text into speech using Google Text-to-Speech (gTTS).

## Setup Instructions

Follow these steps to set up and run the project:

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Steps

1. **Clone the Repository**
   ```bash
   git clone git@github.com:TaraJura/text_to_speech.git
   cd text_to_speech
   ```

2. **Create a Virtual Environment**
   
   Create an isolated environment to manage dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   
   Install all required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Project**
   
   Execute the program to convert text to speech:
   ```bash
   python main.py
   ```

5. **Test the Output**
   - Enter text when prompted
   - The MP3 file will be saved in the `output/` directory
   - Use a media player (like VLC) to play the file:
     ```bash
     vlc output/output.mp3
     ```

## Features

- Converts text to speech using Google Text-to-Speech
- Outputs speech as a high-quality MP3 file

## Notes

- An active internet connection is required, as the project uses Google Text-to-Speech, which operates online
- Avoid using sensitive or private information in the input text

## Project Structure

```
text_to_speech/
│
├── main.py           # Main script for the text-to-speech conversion
├── requirements.txt  # List of dependencies
├── output/          # Folder where MP3 files are saved
├── venv/            # Virtual environment (ignored by Git)
└── .gitignore       # Git ignore file
```

## Dependencies

The project uses the following Python libraries:

- **gTTS**: Google Text-to-Speech library for online TTS conversion

To install the dependencies manually:
```bash
pip install gTTS
```

## Contributing

We welcome contributions to improve this project! Please follow standard Git workflow:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the MIT License.