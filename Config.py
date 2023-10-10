import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6477491824:AAHc9YB4VJ74qr85tkEANCrBGtkVB80bSuM)
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQChdWhYinMbW9i9YIGbpp9_8ysvb4_rijlk9i_TOhP3aIn1eqEgupQp3JadbZB7n1jKode9wOS9mvB_o3CmOLiaST-0yLdocLPrO0EKlqpojDiy39RXmaExKs5AX_B9rlEnLrQ-AA4msWxTncP7UtxyUaDleBP6OCdtCxxSJEd0kreX929S8YhODgnGcTHL-BphDsi0C3cVXBYXQgpeiZ0qRgi9ktvqBJuh0QgWRLotiEe2eR2lG7qm7lRltptEf6jtHrj8NopkgYiIIHgO6SSV5ZPnd2GGSzaOozXtiyDIvZbcV8ojv4DQm7kYVqKVXVnEB-4Kt93cMczB-D8r5qtYAAAAAUBUVPcA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME",@SongMusicVideo_bot "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
