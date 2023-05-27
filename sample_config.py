ENV = os.environ.get("ENV", False)
try:
    API_ID = int(os.environ.get("API_ID", 0))
except ValueError:
    raise Exception(
        "Your API_ID is not a valid integer.\nPlease Check The APP_ID Correctly"
    )
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)

        
