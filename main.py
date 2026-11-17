# https://github.com/asalnorouzzade/Practice-41-YouTube-Link-Extraction.git
import re
html = input().strip()
pattern = r"https?://(www\.)?youtube\.com/embed/([A-Za-z0-9_-]+)"
result = re.search(pattern, html)

if result:
    video_id = result.group(2)
    print(f"https://youtu.be/{video_id}")
    
else:
    print("None")
