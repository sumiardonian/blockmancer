import requests

def get_orphaned_blocks():
    print("[+] Fetching orphaned blocks from Blockchair API...")
    url = "https://api.blockchair.com/bitcoin/blocks?q=is_orphan:true&limit=10"
    response = requests.get(url)
    blocks = response.json().get("data", [])
    return blocks
