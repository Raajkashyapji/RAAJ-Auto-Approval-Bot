# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "24421481"))
    API_HASH = getenv("API_HASH", "b1bb3604f99ed752cbbcaa269beedbc2")
    BOT_TOKEN = getenv("BOT_TOKEN", "6736791879:AAEDzUI2tujJf0m82IRc-78npFKnA0LF1WQ")
    FSUB = getenv("FSUB", "Hanuman2024")
    CHID = int(getenv("CHID", "-1002049231672"))
    SUDO = list(map(int, getenv("SUDO", "6267386260").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://pk4638794:CFAlVeFxCfrlAxym@cluster0.broigcp.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
