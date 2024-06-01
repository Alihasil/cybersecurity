After running the tests, document the following:

## Blocked Payloads:

<script>alert(1)</script> (HTML entities)
<img src=x onerror=\x61\x6c\x65\x72\x74(1)> (Hex encoding)

## Successful Payloads:

<script>\u0061\u006c\u0065\u0072\u0074(1)</script> (Unicode encoding)
<img src=x onerror=alert(1)> (URL encoding)

## Analysis:

The WAF successfully blocked payloads encoded with HTML entities and hex encoding, indicating a robust character-based filter for these encodings.
The WAF failed to block payloads encoded with Unicode and URL encoding, suggesting that these specific encodings were not adequately filtered.
