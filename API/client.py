import requests

if __name__ == '__main__':
    print(requests.get("http://127.0.0.1:5000/all").text)
    print("===================================")
    print(requests.get("http://127.0.0.1:5000/top-3-by-population").text)
    print("===================================")
    print(requests.get("http://127.0.0.1:5000/top-3-by-surface").text)
    print("===================================")
    print(requests.get("http://127.0.0.1:5000/language=English").text)
    print("===================================")
    print(requests.get("http://127.0.0.1:5000/timezone=UTC+2").text)
