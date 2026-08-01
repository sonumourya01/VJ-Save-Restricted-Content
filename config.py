import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8767567999:AAF07meMh1DqfjDLs0sNjqx7bf2jRp-W5mA")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "21213634"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH",:59afaea9fa0d7e3afb99ea0 dd8abf9d8"")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "8039238762"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://sonuchaintoli1:<Bhjj0DLbWTER7pk5>@cluster0.pz9cc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', False))
