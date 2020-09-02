import requests
from bs4 import BeautifulSoup

SITE_NAME = 'programmers'
SITE_URL = 'https://programmers.co.kr/'
SITE_LOGIN_FORM = {
    'utf8': '',
    'authenticity_token': '',
    'user[email]': '',
    'user[password]': '',
    'button': '',
}
"""

"""


with requests.Session() as sess:
    req = sess.get(SITE_URL + 'users/login')
    # print(req.headers)
    print(req.ok, req.status_code)

    soup = BeautifulSoup(req.text, 'lxml')

    login_form = SITE_LOGIN_FORM.copy()
    login_form['utf8'] = soup.select_one('#new_user > input[type=hidden]:nth-child(1)').get('value')
    login_form['authenticity_token'] = soup.select_one('#new_user > input[type=hidden]:nth-child(2)').get('value')
    login_form['user[email]'] = 'nyk700@naver.com'
    login_form['user[password]'] = '567849a10806'

    req = sess.post(SITE_URL + 'users/login', data=login_form)
    print(req.headers)
    print(req.ok, req.status_code)
    print(req.text)
