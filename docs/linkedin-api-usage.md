# LINKEDIN API USAGE

1) Getting started with the REST API - [https://developer.linkedin.com/docs/rest-api](https://developer.linkedin.com/docs/rest-api)

2) Authenticating with OAuth 2.0 - [https://developer.linkedin.com/docs/oauth2#](https://developer.linkedin.com/docs/oauth2#)

3) Create an application at [https://www.linkedin.com/secure/developer?newapp=](https://www.linkedin.com/secure/developer?newapp=) | Select it from [https://www.linkedin.com/secure/developer](https://www.linkedin.com/secure/developer)

You need to provide the below details at this stage

```bash
Company Name

Application Name 

Application Description

Application Logo (width & height should of same length)

Application Use

Website URL

Business Email

Bussiness Phone
```

After successful form submission, you will be redirected to **Application settings** page. Here you can do little customization or you can leave it na dmove forward.

4) Please copy and save your `Client ID` and `Client Secret` securely and go to [https://pypi.python.org/pypi/python-linkedin/4.0](https://pypi.python.org/pypi/python-linkedin/4.0).

5) Read the documentation and try to access linkedin APIs.


``` 
pip install python-linkedin
```

I saw following on my terminal

```bash
rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Tasks/PyLaTex/linkedin-api
$ pip install python-linkedin
Collecting python-linkedin
  Downloading python-linkedin-4.1.tar.gz
Requirement already satisfied: requests>=1.1.0 in c:\anacondapython2.5.0.1\lib\site-packages (from python-linkedin)
Collecting requests-oauthlib>=0.3 (from python-linkedin)
  Downloading requests_oauthlib-0.8.0-py2.py3-none-any.whl
Requirement already satisfied: chardet<3.1.0,>=3.0.2 in c:\anacondapython2.5.0.1\lib\site-packages (from requests>=1.1.0->python-linkedin)
Requirement already satisfied: idna<2.7,>=2.5 in c:\anacondapython2.5.0.1\lib\site-packages (from requests>=1.1.0->python-linkedin)
Requirement already satisfied: urllib3<1.23,>=1.21.1 in c:\anacondapython2.5.0.1\lib\site-packages (from requests>=1.1.0->python-linkedin)
Requirement already satisfied: certifi>=2017.4.17 in c:\anacondapython2.5.0.1\lib\site-packages (from requests>=1.1.0->python-linkedin)
Collecting oauthlib>=0.6.2 (from requests-oauthlib>=0.3->python-linkedin)
  Downloading oauthlib-2.0.6.tar.gz (127kB)
Building wheels for collected packages: python-linkedin, oauthlib
  Running setup.py bdist_wheel for python-linkedin: started
  Running setup.py bdist_wheel for python-linkedin: finished with status 'done'
  Stored in directory: C:\Users\rishikesh agrawani\AppData\Local\pip\Cache\wheels\4a\46\48\7216af2167f80966966b574f38f63a84cffda819a0eb4c3fc1
  Running setup.py bdist_wheel for oauthlib: started
  Running setup.py bdist_wheel for oauthlib: finished with status 'done'
  Stored in directory: C:\Users\rishikesh agrawani\AppData\Local\pip\Cache\wheels\e5\46\f7\bb2fde81726295a13a71e3c6396d362ab408921c6562d6efc0
Successfully built python-linkedin oauthlib
Installing collected packages: oauthlib, requests-oauthlib, python-linkedin
Successfully installed oauthlib-2.0.6 python-linkedin-4.1 requests-oauthlib-0.8.0
```

Please try the below code after replacing the ID and Secret of yours.

```python
"""
	{
		"createdOn": "28 Feb 2018, Web"
		"veryFirstAuthUrl": "https://www.linkedin.com/uas/oauth2/authorization?scope=r_basicprofile%20rw_nus%20r_network%20r_contactinfo%20w_messages%20rw_groups%20r_emailaddress%20r_fullprofile&state=f2c2b0c9508efcd47877f61ffbe3b4c8&redirect_uri=http%3A//rishikesh67.pythonanywhere.com&response_type=code&client_id=816he803kiagbc"
	}
"""
from linkedin import linkedin


def main(client_id, client_secret, return_url):
	authentication = linkedin.LinkedInAuthentication(client_id, client_secret, return_url, \
						linkedin.PERMISSIONS.enums.values()
					)

	print "Authorization Url:", authentication.authorization_url
	application = linkedin.LinkedInApplication(authentication)


if __name__ == "__main__":
	client_id = "816he803kiagBC"
	client_secret = "DKC5u7cGFVMixrcW"
	return_url = "http://rishikesh67.pythonanywhere.com"

	main(client_id, client_secret, return_url);
	print "Done with Linkedin API calls"
```

Quick way

```python
"""
	{
		"createdOn": "28 Feb 2018, Web"
	}
"""
from linkedin import server


def main(client_id, client_secret, return_url):
	application = server.quick_api(client_id, client_secret)
	print "PROFILE:- ", application.get_profile()

if __name__ == "__main__":
	client_id = "816he803kiagBC"
	client_secret = "DKC5u7cGFVMixrcW"

	main(client_id, client_secret, return_url);
	print "Done with Linkedin API calls"
```
