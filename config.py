import os
API_ID = "12096730" int(os.getenv("API_ID"))
API_HASH = "1a8c68a03f6b813d453371aebbd36f20" os.getenv("API_HASH")
BOT_TOKEN = "7453498842:AAFIN8Dp_x7TtWq7QF8G63eeZXMmm8lBUYs" os.getenv("BOT_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")
OWNER_ID = list({int(x) for x in os.environ.get("OWNER_ID", "").split()})
