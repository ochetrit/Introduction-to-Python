import time

from datetime import datetime

timestamp = (time.time())



print("Seconds since January 1, 1970:", f"{timestamp:,.4f}", "or", f"{timestamp:.2e}", "in scientific notation")

now = datetime.now()
print(now.strftime("%b %d %Y"))