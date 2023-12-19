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


def verify_action(_email):
    url = "https://singlelogin.re/layer/_modals/verify_action_modal"

    params = {
        'email': _email,
        'action': 'registration'
    }

    headers = {
        'Accept': 'text/html, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
        'Cookie': 'siteLanguage=en; hide_scamSites_announcement=1; selectedSiteMode=books; hiddenMessages=%5B%22037c%22%5D',
        'Referer': 'https://singlelogin.re/',
        'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'Sec-Ch-Ua-Mobile': '?1',
        'Sec-Ch-Ua-Platform': '"Android"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    try:
        response = requests.get(url, params=params, headers=headers)

        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")

        return response.status_code

    except Exception as e:
        print(f"Error: {e}")
        return None, str(e)

def user_verify_code(_email, _password, _user_name, _verification_code):
    url = "https://singlelogin.re/rpc.php"

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
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
        'X-Requested-With': 'XMLHttpRequest',
    }

    payload = f"isModal=true&email={_email}&password={_password}&name={_user_name}&rx=215&action=registration&redirectUrl=&verifyCode={_verification_code}&gg_json_mode=1"

    response = requests.post(url, headers=headers, data=payload)

    return response.status_code, response.text

email = "parsab71@gmail.com"
password = "w2314efwcsdssss"
user_name = "Parsa"

status_code, response_text = register_user(email, password, user_name)

print(f"Status Code: {status_code}")
print(f"Response: {response_text}")
if response_text == '{"success":1}':
    response_code = verify_action(email)
    if response_code == 200:
        verification_code = input("vared kon: ")
        status_code, response_text = user_verify_code(email,password, user_name, verification_code)
        print('', status_code, response_text, sep='\n ____:\t')
