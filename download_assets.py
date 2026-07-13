import os
import urllib.request

base_url = "https://dyners.com"

# Directory mappings
dirs = [
    "icons",
    "images",
    "images/move",
    "images/transparent"
]

for d in dirs:
    os.makedirs(d, exist_ok=True)

# List of assets to download
assets = [
    # Icons
    "icons/dyners.svg",
    "icons/close-btn.svg",
    "icons/lente.svg",
    "icons/banvit.svg",
    "icons/mc-cain.svg",
    "icons/heinz.svg",
    "icons/pinar.svg",
    
    # Parallax
    "images/move/ust-ekmek.png",
    "images/move/marul.png",
    "images/move/sogan.png",
    "images/move/tursu2.png",
    "images/move/sogan2.png",
    "images/move/domates.png",
    "images/move/tursu.png",
    "images/move/sos.png",
    "images/move/peynir.png",
    "images/move/kofte.png",
    "images/move/alt-ekmek.png",
    
    # Transparent Product Icons
    "images/transparent/hamburger.png",
    "images/transparent/double-hamburger.png",
    "images/transparent/cheese-burger.png",
    "images/transparent/double-cheeseburger.png",
    "images/transparent/lokum.png",
    "images/transparent/chicken.png",
    "images/transparent/sosis.png",
    "images/transparent/double-cheeseburger-3.png",
    
    # Product Images (Photos)
    "images/smash-burger.jpg",
    "images/smash-burger-xl.jpg",
    "images/smash-burger-xxl.jpg",
    "images/hamburgerr.jpg",
    "images/double-hamburger.jpg",
    "images/cheeseburger.jpg",
    "images/double-cheeseburger.jpg",
    "images/beef-tenderloin.jpg",
    "images/chicken-burger.jpg",
    "images/sausage-burger.jpg",
    "images/marsvic.jpg",
    "images/chips.png",
    "images/chips-bottom.png",
    "images/splitted-bg.png",
    "images/splitted-burger-5.png"
]

print("Starting download of dyners.com assets...")
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

success_count = 0
fail_count = 0

for asset in assets:
    url = f"{base_url}/{asset}"
    local_path = asset
    print(f"Downloading {url} -> {local_path} ...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': user_agent})
        with urllib.request.urlopen(req) as response:
            with open(local_path, "wb") as f:
                f.write(response.read())
        print(f" SUCCESS: {local_path}")
        success_count += 1
    except Exception as e:
        print(f" FAILED: {local_path} due to: {e}")
        fail_count += 1

print(f"\nDownload completed. Success: {success_count}, Failed: {fail_count}")
