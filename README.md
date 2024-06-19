# AVY-AI Virtual Assistant

AVY-AI is an advanced virtual assistant designed to simplify your daily tasks and provide you with the latest information through voice commands. It features schedule management, news updates, smart home control, and more.

## Task performed 

### Key Windows Tasks

- **Time Display**: Display the current time.
- **Open Google**: Launch the Google homepage.
- **Open YouTube**: Open the YouTube website.
- **Play Music**: Access the Gaana website to play music.
- **Weather**: Provide weather information.
- **Shutdown**: Initiate system shutdown.
- **Lock System**: Lock the user’s system.
- **Close Applications**: Close Command Prompt, Notepad, Microsoft Word, Microsoft Excel, and Microsoft PowerPoint.
- **Open Chrome**: Launch Google Chrome browser.
- **Maximize/Minimize/Close Windows**: Manipulate window states (maximize, minimize, close).
- **Google Search**: Perform a Google search.
- **Open Application**: Open specified applications.
- **Close Chrome**: Close the Google Chrome browser.
- **Take a Screenshot**: Capture and save screenshots.
- **Volume Control**: Adjust system volume (up, down, mute).

### Automation Tasks

- **Chrome Automation**: Opening, managing, and terminating Chrome browser sessions.
- **YouTube Automation**: Navigating to YouTube and playing music or videos.
- **Paint Automation**: Drawing shapes like square spirals, squares, and houses in Paint.
- **Notepad Automation**: Creating notes based on user input.

### Personalization Tasks

- **Greet User**: Respond to user greetings.
- **Thank User**: Acknowledge user gratitude.
- **Update To-Do List**: Add data to a Google Sheets-based to-do list.
- **Show Progress**: Display user progress using a Tableau dashboard.
- **Chat Interaction**: Engage in conversation using a generative language model.
- **Make Note**: Open Notepad and take notes based on user input.

### Conversational AI

- **Gemini API Integration**: Utilize the Gemini API to generate responses to user queries in both text and speech formats.
- **News API Integration**: Fetches and reads the latest news articles from various sources.

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Required Python libraries: `speech_recognition`, `pyttsx3`, `requests`, `flask`, etc.

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/AVY-Virtual-Assistant.git
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

### Sample `config.json`

```json
{
    "news_api_key": "your_news_api_key",
    "news_sources": ["source1", "source2"],
    "weather_api_key": "your_weather_api_key",
    "location": "your_location",

}
```
## Troubleshooting

### Common Issues

- **No response to voice commands**: Ensure your microphone is working and properly configured. Check the voice recognition library documentation for troubleshooting tips.
- **Error fetching news**: Verify that your API keys in `config.json` are correct and that you have internet connectivity.

### Debugging

Run the application with verbose logging to see detailed output:

```bash
python main.py --verbose


