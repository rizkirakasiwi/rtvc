# Real-Time Voice Conversation (RTVC)

A real-time voice chat application built with Python that enables natural voice conversations using OpenAI's AI services.

## Features

- **Real-time voice streaming** using FastRTC
- **Speech-to-text** transcription with OpenAI Whisper
- **AI-powered responses** using GPT-5
- **Text-to-speech** output with OpenAI TTS
- **Web-based interface** built with Gradio and FastAPI
- **Conversation history** management

## Requirements

- Python 3.8+
- OpenAI API key
- Twilio TURN credentials (for deployment to Gradio Spaces)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd rtvc
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file with your OpenAI API credentials and other required configuration.

## Usage

Run the application:
```bash
python main.py
```

The application will be available at `http://localhost:7860`

## Architecture

- **Backend**: FastAPI web framework
- **Frontend**: Gradio web interface
- **Audio Processing**: 16kHz input, 24kHz output, real-time streaming
- **AI Services**: OpenAI Whisper, GPT-5, and TTS integration

## Deployment

The application is designed to work both locally and on Gradio Spaces with automatic configuration for different environments.

## Dependencies

Key libraries used:
- `fastapi` - Web framework
- `fastrtc` - Real-time audio streaming
- `gradio` - Web UI framework  
- `openai` - OpenAI API client
- `python-dotenv` - Environment management
- `numpy` - Audio processing