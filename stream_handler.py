import logging
import time
from typing import Any, Generator, Union

import numpy as np
from fastrtc import AdditionalOutputs
from numpy.typing import NDArray

from ai_services import generate_ai_response, stream_tts_audio, transcribe_audio
from audio_processing import process_audio_to_wav

logger = logging.getLogger(__name__)


def response(
    audio_data: tuple[int, NDArray[np.int16 | np.float32]],
) -> Generator[Union[bytes, Any], None, None]:
    chatbot = []
    messages = [{"role": d["role"], "content": d["content"]} for d in chatbot]
    start = time.time()

    # Process audio to WAV format
    wav_buffer = process_audio_to_wav(audio_data)

    try:
        # Transcribe audio
        transcription_text = transcribe_audio(wav_buffer, start)

        chatbot.append({"role": "user", "content": transcription_text})
        yield AdditionalOutputs(chatbot)

        messages.append({"role": "user", "content": transcription_text})

        # Generate AI response
        response_text = generate_ai_response(messages, start)

    except Exception as e:
        logger.error(f"Error in transcription/response: {e}")
        # Fallback response
        error_response = "I'm sorry, I encountered an error processing your request. Please try again."
        chatbot.append({"role": "user", "content": "Audio input received"})
        chatbot.append({"role": "assistant", "content": error_response})
        yield AdditionalOutputs(chatbot)
        return

    chatbot.append({"role": "assistant", "content": response_text})

    try:
        # Stream TTS audio
        for audio_chunk in stream_tts_audio(response_text, start):
            yield audio_chunk

    except Exception as e:
        logger.error(f"Error in TTS streaming: {e}")

    yield AdditionalOutputs(chatbot)
