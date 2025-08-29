# Real-Time Voice Conversation (RTVC)

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Project Example for Basic real-time voice chat application that demonstrates how to build AI-powered voice conversations using Python. This project showcases integration between OpenAI's AI services, real-time audio streaming, and web technologies to create a seamless voice chat experience.

## 🎯 Overview

This application enables natural voice conversations with AI through a web browser. Users can speak directly to the application, which transcribes their speech, generates intelligent responses using GPT, and speaks back using text-to-speech - all in real-time.

## ✨ Features

- 🎤 **Real-time voice streaming** using FastRTC for low-latency audio
- 🗣️ **Speech-to-text** transcription with OpenAI Whisper
- 🧠 **AI-powered responses** using GPT models
- 🔊 **Text-to-speech** output with OpenAI TTS
- 🌐 **Web-based interface** built with Gradio and FastAPI
- 📝 **Conversation history** management and persistence
- ☁️ **Cloud deployment ready** with Gradio Spaces support
- 🔄 **Automatic error handling** and recovery

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- Microphone access in your browser

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rizkirakasiwi/rtvc.git
   cd rtvc
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Run the application:**
   ```bash
   python main.py
   ```

6. **Open your browser:**
   Navigate to `http://localhost:7860` and start talking!

## 🏗️ Architecture

The application follows a modular architecture:

```
rtvc/
├── main.py              # API entry point
├── ui.py                # UI entry point (can't run both main.py and ui.py) 
├── app_config.py        # Stream configuration
├── stream_handler.py    # Main audio processing pipeline
├── ai_services.py       # OpenAI API integrations
├── audio_processing.py  # Audio format conversion
├── requirements.txt     # Python dependencies
└── .env                # Environment variables
```

### Component Overview

- **FastAPI Backend**: Handles HTTP requests and WebSocket connections
- **Gradio Frontend**: Provides the web interface and real-time audio streaming
- **Audio Pipeline**: 16kHz input → Processing → 24kHz output
- **AI Services**: Whisper (STT) → GPT (Text) → TTS (Speech)

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | ✅ Yes |
| `TWILIO_ACCOUNT_SID` | Twilio account SID (for Spaces deployment) | ❌ No |
| `TWILIO_AUTH_TOKEN` | Twilio auth token (for Spaces deployment) | ❌ No |

### Audio Settings

- **Input**: 16kHz sample rate, mono channel
- **Output**: 24kHz sample rate, WAV format
- **Processing**: Real-time chunks with automatic padding

## 🌐 Deployment

### Local Development
```bash
python main.py
```

### Gradio Spaces
The application automatically detects Gradio Spaces environment and configures:
- Twilio TURN credentials for WebRTC
- Concurrency limits (5 concurrent users)
- Time limits (90 seconds per session)

### Docker (Optional)
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 7860

CMD ["python", "main.py"]
```

## 🛠️ Development

### Project Structure
- `main.py` - FastAPI application entry point
- `ui.py` - UI application entry point
- `app_config.py` - Gradio Stream configuration with audio settings
- `stream_handler.py` - Core audio processing pipeline
- `ai_services.py` - OpenAI API integrations (Whisper, GPT, TTS)
- `audio_processing.py` - Audio format conversion utilities

### Key Dependencies

| Package | Purpose |
|---------|---------|
| `fastapi[standard]` | Web framework and server |
| `fastrtc[vad]` | Real-time audio streaming with voice activity detection |
| `gradio` | Web UI framework |
| `openai` | OpenAI API client |
| `python-dotenv` | Environment variable management |
| `numpy` | Audio data processing |

### Adding Features

1. **Custom AI Models**: Modify `ai_services.py` to use different models
2. **Audio Effects**: Extend `audio_processing.py` for filters or effects  
3. **UI Customization**: Update `app_config.py` to modify the Gradio interface
4. **New Endpoints**: Add routes in `main.py` for additional functionality

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [OpenAI](https://openai.com/) for providing the AI services
- [Gradio](https://gradio.app/) for the excellent web interface framework
- [FastRTC](https://github.com/gradio-app/fastrtc) for real-time audio streaming
- The open-source community for inspiration and tools

## 📞 Support

If you have any questions or run into issues:

1. Check the [Issues](https://github.com/rizkirakasiwi/rtvc/issues) page
2. Create a new issue with detailed information
3. Join the discussion in existing issues

---

**Built with ❤️ using Python, OpenAI, and Gradio**
