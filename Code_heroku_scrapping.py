import  requests #requests are a python package that send HTTP, HTTPs requests to the server and get the HTML of the page
from bs4 import BeautifulSoup

session_requests = requests.session()

payload = {
	'email': 'test123@codeheroku.com', 
	'password' : 'test123',
	'_formname': 'login' 
}

##Do a get request on login page 
login_url = "http://www.codeheroku.com/login"
result = session_requests.get(login_url)

soup = BeautifulSoup(result.content, 'html.parser')
tag = soup.find("input",attrs={'name':'_formkey'})


##Parse the formkey and add it to the payload
payload['_formkey'] = tag['value']
print(payload)


##Make a post request to login
result = session_requests.post(login_url, data = payload)
print(result.content)


##Do a get request on Dashboard to see if you are able to reach there
url = 'http://www.codeheroku.com/dashboard/'
result = session_requests.get(url, headers = dict(referer = url))

