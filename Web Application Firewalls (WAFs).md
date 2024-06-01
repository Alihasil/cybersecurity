# Web Application Firewalls (WAFs):
WAFs are specialized security solutions designed to protect web applications by filtering and monitoring HTTP traffic between a web application and the Internet. They provide protection against various attacks such as SQL injection, cross-site scripting (XSS), and cross-site request forgery (CSRF).

## Mechanisms for Filtering XSS Attacks:

1. **Character-based Filters** :
 These filters look for specific patterns or characters associated with XSS attacks. For example, they might block input containing <script>, onerror=, or other known XSS vectors.   
2. **Signature-based Detection:**
This method relies on known attack signatures to identify malicious input.
3. **Behavioral Analysis:** 
Monitors how the input behaves within the application to detect anomalies indicative of an attack.
4. **Contextual Analysis:** 
Examines the context in which the input appears (e.g., within HTML, JavaScript, or URL parameters) to determine if it poses a threat.
