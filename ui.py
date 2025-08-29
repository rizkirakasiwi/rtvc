from fastapi import FastAPI
import gradio as gr
from app_config import create_stream

app = FastAPI()
stream = create_stream()
app = gr.mount_gradio_app(app, stream.ui, path="/")

if __name__ == "__main__":
    stream.ui.launch(server_port=7860)
