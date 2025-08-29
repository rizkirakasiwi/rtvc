import logging
from dotenv import load_dotenv
from fastapi import FastAPI
from app_config import create_stream

load_dotenv()

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

app = FastAPI()
stream = create_stream()
stream.mount(app)
