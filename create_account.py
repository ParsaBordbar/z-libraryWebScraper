import requests

def register_user(_email, _password, _user_name):
    url = "https://singlelogin.re/papi/user/verification/send-code"

    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryHFp1n9h9X8NcOfOl',
        'Cookie': 'siteLanguage=en; hide_scamSites_announcement=1; selectedSiteMode=books; hiddenMessages=%5B%22037c%22%5D',
        'Origin': 'https://singlelogin.re',
        'Referer': 'https://singlelogin.re/',
        'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'Sec-Ch-Ua-Mobile': '?1',
        'Sec-Ch-Ua-Platform': '"Android"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    }

    # Construct the payload string
    payload = f'''------WebKitFormBoundaryHFp1n9h9X8NcOfOl
Content-Disposition: form-data; name="email"

{_email}
------WebKitFormBoundaryHFp1n9h9X8NcOfOl
Content-Disposition: form-data; name="password"

{_password}
------WebKitFormBoundaryHFp1n9h9X8NcOfOl
Content-Disposition: form-data; name="name"

{_user_name}
------WebKitFormBoundaryHFp1n9h9X8NcOfOl
Content-Disposition: form-data; name="rx"

215
------WebKitFormBoundaryHFp1n9h9X8NcOfOl
Content-Disposition: form-data; name="action"

registration
------WebKitFormBoundaryHFp1n9h9X8NcOfOl
Content-Disposition: form-data; name="redirectUrl"


------WebKitFormBoundaryHFp1n9h9X8NcOfOl--
'''

    response = requests.post(url, headers=headers, data=payload)

    return response.status_code, response.text

email = "sad1381esm@gmail.com"
password = "w2314efwcsde"
user_name = "sadc232"

status_code, response_text = register_user(email, password, user_name)

print(f"Status Code: {status_code}")
print(f"Response: {response_text}")
