import requests

# URL of the web application
url = 'http://example.com/vulnerable-input'

# Headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0',
    'Content-Type': 'application/x-www-form-urlencoded',
}

# Function to test XSS payloads
def test_xss_payloads(url, payloads):
    for payload in payloads:
        response = requests.post(url, headers=headers, data={'input': payload})
        if payload in response.text:
            print(f'Payload executed: {payload}')
        else:
            print(f'Payload blocked: {payload}')

# Test the generated XSS payloads
test_xss_payloads(url, xss_payloads)
