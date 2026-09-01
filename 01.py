python3 -c '
import urllib.request, json, base64, sys, os

TOKEN = "YOUR_PAT_TOKEN_HERE"
USER = "samalpha4"
REPO = "demorepo"
FILE_PATH = "your_file.cpp"  # Change to your file name

if not os.path.exists(FILE_PATH):
    print(f"Error: {FILE_PATH} not found in current directory.")
    sys.exit(1)

with open(FILE_PATH, "rb") as f:
    content = base64.b64encode(f.read()).decode("utf-8")

filename = os.path.basename(FILE_PATH)
data = json.dumps({"message": f"Upload {filename} via Python", "content": content}).encode("utf-8")
req = urllib.request.Request(
    f"https://api.github.com/repos/{USER}/{REPO}/contents/{filename}",
    data=data,
    headers={"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github+json"},
    method="PUT"
)

try:
    with urllib.request.urlopen(req) as response:
        if response.status in (200, 201):
            print(f"Successfully uploaded {filename} to {USER}/{REPO}!")
except urllib.error.HTTPError as e:
    print(f"Failed to upload: HTTP {e.code} - {e.reason}")
'