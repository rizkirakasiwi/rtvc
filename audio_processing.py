import io
import logging
import numpy as np
import wave
from numpy.typing import NDArray

logger = logging.getLogger(__name__)


def process_audio_to_wav(audio_data: tuple[int, NDArray[np.int16 | np.float32]]) -> io.BytesIO:
    sample_rate, audio_array = audio_data
    
    # Ensure valid sample rate for wave file
    if sample_rate <= 0:
        sample_rate = 16000  # Default to 16kHz
    
    wav_buffer = io.BytesIO()
    try:
        with wave.open(wav_buffer, 'wb') as wav_file:
            wav_file.setnchannels(1)  # Mono
            wav_file.setsampwidth(2)  # 16-bit
            wav_file.setframerate(sample_rate)
            wav_file.writeframes(audio_array.astype(np.int16).tobytes())
    except wave.Error as e:
        logger.error(f"Wave file error: {e}")
        # Fallback: use default sample rate
        wav_buffer = io.BytesIO()
        with wave.open(wav_buffer, 'wb') as wav_file:
            wav_file.setnchannels(1)
            wav_file.setsampwidth(2)
            wav_file.setframerate(16000)
            wav_file.writeframes(audio_array.astype(np.int16).tobytes())
    
    wav_buffer.seek(0)
    wav_buffer.name = "audio.wav"
    return wav_buffer