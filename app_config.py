import gradio as gr
from fastapi import FastAPI
from fastrtc import ReplyOnPause, Stream, get_twilio_turn_credentials
from gradio.utils import get_space

from stream_handler import response


def create_stream() -> Stream:
    chatbot = gr.Chatbot(type="messages")
    stream = Stream(
        modality="audio",
        mode="send-receive",
        handler=ReplyOnPause(
            fn=response,  # type: ignore
            input_sample_rate=16000,
            output_sample_rate=24000,
        ),
        additional_outputs_handler=lambda outputs, chatbot: (
            chatbot if chatbot else outputs
        ),
        additional_inputs=[chatbot],
        additional_outputs=[chatbot],
        rtc_configuration=get_twilio_turn_credentials() if get_space() else None,
        concurrency_limit=5,
        time_limit=90 if get_space() else None,
    )

    return stream
