import io
import logging
import time
from typing import Generator
import numpy as np
from numpy.typing import NDArray
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
openai = OpenAI()
logger = logging.getLogger(__name__)

INSTRUCTION = """
You are a helpful AI assistant with a cheerful and friendly personality. Always respond in a warm, upbeat tone while keeping your answers simple and easy to understand. Use encouraging language and be genuinely enthusiastic about helping.

Guidelines:
- Keep responses concise and straightforward
- Use positive, uplifting language
- Sound genuinely excited to help
- always aware with conversation history
"""


def transcribe_audio(wav_buffer: io.BytesIO, start_time: float) -> str:
    transcriptions = openai.audio.transcriptions.create(model="whisper-1", file=wav_buffer)
    logger.info(f"transcription time: {time.time() - start_time}")
    logger.info(f"transcription: {transcriptions.text}")
    return transcriptions.text


def generate_ai_response(messages: list[dict], start_time: float) -> str:
    response_start = time.time()
    response_text = openai.responses.create(
        model="gpt-5",
        reasoning={"effort": "low"},
        instructions=INSTRUCTION,
        input=messages,  # type: ignore
    )
    logger.info(f"response generation time: {time.time() - response_start}")
    return response_text.output_text


def stream_tts_audio(text: str, start_time: float) -> Generator[tuple[int, NDArray[np.int16]], None, None]:
    tts_start = time.time()
    with openai.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="sage",
        input=text,
        instructions=INSTRUCTION,
        response_format="wav",
    ) as response_stream:
        # Buffer initial chunks to prevent choppy audio at start
        buffer = b''
        chunk_count = 0
        min_buffer_size = 8192  # Minimum buffer before starting playback
        
        for audio_chunk in response_stream.iter_bytes():
            if len(audio_chunk) == 0:
                continue
                
            buffer += audio_chunk
            chunk_count += 1
            
            # For first few chunks, build up buffer to ensure smooth start
            if chunk_count <= 3 and len(buffer) < min_buffer_size:
                continue
            
            # Process buffer in properly aligned chunks
            while len(buffer) >= 2048:  # Process in 2KB chunks
                chunk_to_process = buffer[:2048]
                buffer = buffer[2048:]
                
                # Ensure chunk size is multiple of int16 element size (2 bytes)
                if len(chunk_to_process) % 2 != 0:
                    # Move the odd byte to next buffer instead of discarding
                    buffer = chunk_to_process[-1:] + buffer
                    chunk_to_process = chunk_to_process[:-1]
                
                if len(chunk_to_process) > 0:
                    audio_array = np.frombuffer(chunk_to_process, dtype=np.int16).reshape(1, -1)
                    yield (24000, audio_array)
        
        # Process any remaining buffer
        if len(buffer) > 1:  # Only process if we have at least 2 bytes
            if len(buffer) % 2 != 0:
                buffer = buffer[:-1]  # Remove last odd byte
            if len(buffer) > 0:
                audio_array = np.frombuffer(buffer, dtype=np.int16).reshape(1, -1)
                yield (24000, audio_array)
    
    logger.info(f"TTS streaming time: {time.time() - tts_start}")
    logger.info(f"Total response time: {time.time() - start_time}")
