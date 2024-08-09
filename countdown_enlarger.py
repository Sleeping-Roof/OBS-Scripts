import time
import math
from obswebsocket import obsws, requests

# OBS WebSocket connection settings
host = "localhost"
port = 4444
password = "your_password"

# Connect to OBS WebSocket
ws = obsws(host, port, password)
ws.connect()

# Countdown timer settings
countdown_time = 10  # Countdown time in seconds
image_source_name = "YourImageSource"  # Name of the image source in OBS
initial_scale = 0.1  # Initial scale of the image
final_scale = 1.0  # Final scale of the image

# Function to set the scale of the image source
def set_image_scale(scale):
    ws.call(requests.SetSceneItemProperties(item=image_source_name, scale={"x": scale, "y": scale}))

# Countdown loop
for i in range(countdown_time, -1, -1):
    print(f"Time left: {i} seconds")
    scale = initial_scale + (final_scale - initial_scale) * (1 - i / countdown_time)
    set_image_scale(scale)
    time.sleep(1)

# Disconnect from OBS WebSocket
ws.disconnect()
