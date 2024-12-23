**Report on OWASP Top 10 Vulnerabilities in the Application**

This app is a Cyber Security Base 2024 Project 1 repo with 5 OWASP vulnerabilities made with Django. This simple webapp demonstrates multiple different vulnerabilities that are common in similar web apps. This app should not be used in any other way than running locally and with acknowledgment of the vulnerabilities as this app is for educational purposes only. In the app, I have highlighted only a few vulnerabilities and their potential fixes, but the app does contain more vulnerabilities than the highlighted ones.

**FLAW 1: Broken Access Control**

Access control mechanisms are critical for restricting users to authorized resources. In this application, the admin_access view allows users to access the admin dashboard if a specific session variable, is_admin, is set to true. However, this variable is not tied to a user’s credentials or proper role validation. This creates a gap in access control that attackers can exploit. The lack of proper validation means any user with knowledge of the session handling mechanism can manipulate their session to gain unauthorised admin access. Broken access control is a common and damaging vulnerability, as it allows attackers to escalate privileges and compromise critical areas of an application. An attacker can manipulate session data using browser developer tools or external utilities like curl to set is_admin to True, bypassing any real authentication checks. This could allow them to perform admin actions, such as accessing critical user data or modifying application settings.

**Relevant Code:** views.py, Function: admin_access

![image](https://github.com/user-attachments/assets/d665cc60-3181-4c9f-bd8d-819a4a057399)

**How to Fix It:** To fix this vulnerability, implement a permission check based on the user’s role stored in the database. Using session variables alone is insufficient, as they can be tampered.

![image](https://github.com/user-attachments/assets/2a7886c7-3f35-450d-ba63-556b68f020aa)

**FLAW 2:** Cryptographic Failures

Passwords stored in plaintext in the database is a security risk. If the database is compromised, all user credentials are directly exposed, allowing attackers to reuse these credentials on other platforms where users may have identical passwords. If an attacker gains access to the database through an exploit, they can view user credentials in plaintext. In addition, users often reuse passwords across multiple platforms, increasing the likelihood of credential stuffing attacks.

**Relevant Code:** views.py, Function: register_view

![image](https://github.com/user-attachments/assets/74bbe34d-91aa-40af-8fce-f6c5533a02c5)

**How to Fix It:** Use strong, salted, and hashed passwords when storing user credentials. Django provides built-in utilities for secure password handling.

![image](https://github.com/user-attachments/assets/22d5a81d-985d-4c32-b2a6-9d28f91a94f3)

**FLAW 3: Injection**

The application uses raw SQL queries to authenticate users, so its vulnerable to SQL injection attacks. SQL injection happens when user input is included in a query without proper sanitisation, allowing attackers to manipulate the query’s logic and access unauthorized data. By injecting malicious SQL code, attackers can bypass authentication or extract sensitive data. For example, if you input the following queries into login form, you can bypass the authentication:

- Username: username = ' OR '1'='1
- Password: password = ' OR '1'='1

**Relevant Code:** views.py, Function: login_view

![image](https://github.com/user-attachments/assets/c726386e-26ab-4422-88be-9d62f76d83d9)
 
**How to Fix It:** Replace raw SQL queries with parameterized queries using Django ORM:

![image](https://github.com/user-attachments/assets/77d70148-26a8-45fe-9c16-73082d3a81aa)

In addition, you can use an Object-Relational Mapper (ORM) for database interactions, implement input validation to restrict acceptable data formats, use prepared statements or stored procedures for direct database queries.

 
**FLAW 4: Security Misconfiguration**

Security misconfigurations can happen from improper settings in production environments. The application has DEBUG enabled, which exposes sensitive information, e.g., stack traces and database configurations, when errors occur. An attacker can deliberately trigger errors to view detailed debug information. This data may reveal file paths, API keys, or other critical information to help in attacks. In addition, the secret key is exposed in the source code, which should not be the case. This is a common mistake, even though it can be removed later on, the secret key may persist in older commits.

**Relevant Code:** settings.py

![image](https://github.com/user-attachments/assets/3c10ed2c-7f3f-41de-b98e-ca7a64404ab7)

**How to fix:** Remove Debug settings and secret key from production.

**FLAW 5: Server-Side Request Forgery (SSRF)**

The application allows users to specify an arbitrary URL for redirection without validation. This lack of validation opens the application to SSRF attacks, where an attacker can make the server issue requests to unintended locations. Such requests could access sensitive internal systems, exploit cloud metadata endpoints, or redirect users to malicious websites. An attacker could abuse the next parameter to redirect users to a malicious site for phishing purposes or exploit internal server networks. For example:

- http://cyberapp.com/unvalidated-redirect/?next=http://malicious.com
- http://cyberapp.com/unvalidated-redirect/?next=http://internal-system/admin

These scenarios allow attackers to leverage the application's trust in its internal network or mislead users into visiting compromised pages. It can in theory also expose cloud provider metadata APIs, potentially leaking sensitive data like access tokens, and provide amplification of Distributed Denial of Service (DDoS) attacks by sending numerous requests via the application.

**Relevant Code:** views.py, Function: unvalidated_redirect

![image](https://github.com/user-attachments/assets/e113593e-3a76-4ed3-bac0-efdea3aa9470)

**How to Fix It:** To fix this vulnerability, in the application can be implemented stricter validation for the next parameter. The application should only redirect to trusted URLs and not allow every redirect:
 
![image](https://github.com/user-attachments/assets/09d51a3c-92f0-49fa-9d44-d52bbe84b37b)

**FLAW 6: Security Logging and Monitoring Failures**

The app has not included any kind of logging or monitoring mechanisms in order to detect security events or anomalies. Usually monitoring is the first step in order to rectify issues if tests do not detect a possible bug or security issue.

**How to Fix It:** Added monitoring capabilities to the app manage.py file:

![image](https://github.com/user-attachments/assets/08912199-720f-4109-8663-8c1adac67861)

