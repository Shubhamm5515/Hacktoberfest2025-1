#!/usr/bin/env python3
# url_checker.py
import urllib.request
import urllib.error
import sys

def check_url(url, timeout=5):
    try:
        req = urllib.request.Request(url, method="HEAD")
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as e:
        return f"ERR: {e.__class__.__name__}"

def main(argv):
    if len(argv) < 2:
        print("Usage: url_checker.py url1 [url2 ...]")
        return
    for url in argv[1:]:
        if not url.startswith(("http://", "https://")):
            url = "http://" + url
        status = check_url(url)
        print(f"{url:60} -> {status}")

if __name__ == "__main__":
    main(sys.argv)
