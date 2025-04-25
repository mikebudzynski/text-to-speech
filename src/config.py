INPUT_FILE_PATH = "input/sample.txt"
OUTPUT_FILE_PATH = "output/" + str.replace(str.split(INPUT_FILE_PATH, "/")[1], ".", "_") + ".wav"

# Favorites include: en-US-Andrew2:DragonHDLatestNeural, en-US-Nova:DragonHDLatestNeural, zh-CN-YunxiNeural
# Doesn't apply to ssml method, but can be used for plain text method.
SPEECH_VOICE = "en-US-Nova:DragonHDLatestNeural"

# Creates an instance of a speech config with specified subscription key and service region.
SPEECH_KEY = ""
SERVICE_REGION = "eastus2"
# ENDPOINT = ""