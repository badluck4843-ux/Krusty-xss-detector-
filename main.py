# Krusty XSS Detector - Ethical Edition v1
# Solo para labs autorizados - Uso educativo
# Author: Krusty Hack (badluck4843-ux)

import requests
from urllib.parse import urlparse

PAYLOADS = [
    "<krustyTest>",
    "\"'><krusty>",
    "<script>console.log('krusty')</script>"
]

def check_auth(url):
    try:
        with open("allowed_domains.txt") as f:
            allowed = [l.strip() for l in f if l.strip()]
        host = urlparse(url).netloc
        return any(host == a or host.endswith("."+a) for a in allowed)
    except FileNotFoundError:
        return False

def scan(url):
    if not check_auth(url):
        print(f"[!] BLOQUEADO: {url} no está en allowed_domains.txt")
        print("[!] Solo escanea tus labs propios.")
        return
    
    print(f"[+] Escaneando (autorizado): {url}\n")
    for p in PAYLOADS:
        try:
            r = requests.get(url, params={"q": p}, timeout=8)
            if p in r.text:
                print(f"  [!] REFLEJO DETECTADO -> {p}")
            else:
                print(f"  [OK] No reflejado -> {p}")
        except Exception as e:
            print(f"  [ERROR] {e}")

if __name__ == "__main__":
    print("=== KRUSTY XSS DETECTOR ===")
    print("Solo para entornos autorizados\n")
    target = input("URL de tu lab: ")
    scan(target)
