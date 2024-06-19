# AVY-AI Virtual Assistant

AVY-AI is an advanced virtual assistant designed to simplify your daily tasks and provide you with the latest information through voice commands. It features schedule management, news updates, smart home control, and more.

## Features

- **Voice Recognition**: Understands and processes voice commands.
- **Schedule Management**: Manages your appointments, reminders, and events.
- **News Updates**: Fetches and reads the latest news articles from various sources.
- **Weather Updates**: Provides current weather information.
- and much more...

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Required Python libraries: `speech_recognition`, `pyttsx3`, `requests`, `flask`, `openai`

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/avy-ai.git
    cd avy-ai
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

## Usage

1. Start the AVY-AI application:

    ```bash
    python main.py
    ```

2. Interact with AVY-AI through voice commands:

    - "What's the news?"
    - "Set a reminder for my meeting at 10 AM."
    - "Turn off the living room lights."
    - "What's the weather like today?"

## Configuration

To customize AVY-AI, edit the `config.json` file. Here, you can set your preferences for:

- **News API Key and Sources**: Configure your news API key and preferred news sources.
- **Weather API Key and Location**: Set your weather API key and location.
- **Smart Home Device Configurations**: Add and configure your smart home devices.
- **Additional Plugins and Modules**: Include and configure additional plugins for extended functionality.

### Sample `config.json`

```json
{
    "news_api_key": "your_news_api_key",
    "news_sources": ["source1", "source2"],
    "weather_api_key": "your_weather_api_key",
    "location": "your_location",
    "smart_home": {
        "device1": "configuration1",
        "device2": "configuration2"
    },
    "plugins": ["plugin1", "plugin2"]
}
