import os
from pathlib import Path
import pytz
from dotenv import load_dotenv
import logging
import colorlog


# -------------------------------
# Project Root and Timezone Config
# -------------------------------
# Define project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Define timezone for Singapore
SGT = pytz.timezone('Asia/Singapore')


# -------------------------------
# Load environment variables from .env file
# -------------------------------
dotenv_path = PROJECT_ROOT / '.env'
load_dotenv(dotenv_path)


# -------------------------------
# API Keys and Authentication
# -------------------------------
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise EnvironmentError("OpenAI API key not found in environment variables.")


# -------------------------------
# Participant and Messaging Config
# -------------------------------
# Define the participant's JID
PARTICIPANT_JID = '6581574286@s.whatsapp.net'

# Define participant mapping
PARTICIPANT_MAPPING = {
    PARTICIPANT_JID: "Elizabeth",  # Use the participant JID variable as the key
    None: "Jason"
}


# -------------------------------
# Batch Processing Config
# -------------------------------
# Completion window for batch jobs (in hours)
COMPLETION_WINDOW = "24h"

# Use DATA_DIR for all paths under the data directory
DATA_DIR = PROJECT_ROOT / 'data'

# Directories for batch input/output files
BATCH_INPUT_DIR = DATA_DIR / "batch_inputs"
BATCH_OUTPUT_DIR = DATA_DIR / "batch_outputs"
BATCH_TRACKING_FILE = DATA_DIR / 'tracking.json'


# -------------------------------
# Data and Storage Config
# -------------------------------
# Directory for data and error logs
ERROR_LOGS_DIRECTORY = DATA_DIR / 'error_logs'
BLOB_INFO_DIRECTORY = DATA_DIR / 'blob_info'
WHATSAPP_MESSAGES_FILE = DATA_DIR / 'whatsapp_messages_by_day.json'
MD_DIR = DATA_DIR / 'markdown'
MD_DIR2 = Path("/Users/jasonnathan/Documents/ChatGPT-Exports/md")

# Directory for storage (e.g., SQLite database)
STORAGE_DIR = PROJECT_ROOT / 'storage'
DATABASE_PATH = STORAGE_DIR / 'ChatStorage.sqlite'
CHUNKED_DIR = PROJECT_ROOT / "chunked"
SUMMARY_DIR = PROJECT_ROOT / "summarized_chunked"

# -------------------------------
# Summarization Config
# -------------------------------
SUMMARY_LENGTH = 1000  # Tokens or words for the summary
SUMMARY_MODEL = "phi3:medium-128k" 
SUMMARY_LENGTH = 1000 

# -------------------------------
# Logging Config
# -------------------------------
# Ensure the error log directory exists
ERROR_LOGS_DIRECTORY.mkdir(parents=True, exist_ok=True)

# Setup logging configuration
log_file = ERROR_LOGS_DIRECTORY / "app.log"
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,  # Default to DEBUG level for more detailed logs
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode='a'
)

# Set up colorlog for prettier console logs
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Define colored formatter
color_formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(asctime)s - %(levelname)s - %(message)s",
    datefmt=None,
    reset=True,
    log_colors={
        'DEBUG':    'cyan',
        'INFO':     'green',
        'WARNING':  'yellow',
        'ERROR':    'red',
        'CRITICAL': 'bold_red',
    }
)
console_handler.setFormatter(color_formatter)

# Add the console handler to the root logger
logging.getLogger().addHandler(console_handler)


# -------------------------------
# Debugging and Manual Testing Config
# -------------------------------
# Enable/disable debug mode
DEBUG = True

# Enable/disable manual testing mode (e.g., to prevent actual API calls)
MANUAL_TESTING = False
