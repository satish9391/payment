# payment: Using python framework Django
to start your project some requrements
1st make a folder where you write your code

# Installation : Setup Django
What you need for a basic dev environment:

1. Python 2.7.x or 3.4.x
2. easy_install and Pip
3. Git
4. virtualenv
5. Django
6. Database SQLite (bydefault)

# Usage Description
The **recharge** folder has the following files
1. views.py : it is interface function that takes a Web request and returns a Web response. This file will initiate the sample test transaction through the Paytm gateway. Paytm parameters need to be added in this file.
2. urls.py : A URL is simply a web address. You can see a URL every time you visit a website – it is visible in your browser's address bar
3. Checksum.py : This file has the logic for checksum generation and verification.
connectionutils.py : This file has the logic for processing PG response after the transaction processing.

# Configure
1 .Copy the recharge folder into the django project of your machine and add in setting.py of your django project "INSTALLED_APPS"
2. to add **url(r'^recharge/', include('recharge.urls'))** in your django project urls.py file

# Some more installation
1. requests : Requests allows you to send organic, grass-fed HTTP/1.1 requests, without the need for manual labor. 
2. Crypto.Cipher : This is a collection of both secure hash functions (such as SHA256 and RIPEMD160), and various encryption algorithms (AES, DES, RSA, ElGamal, etc.). The package is structured to make adding new modules easy.
