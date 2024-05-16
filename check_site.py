import requests
from bs4 import BeautifulSoup
import re
import socket


def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True, response.text
        else:
            return False, None
    except Exception as e:
        print(f"Error: {e}")
        return False, None


def get_ip_address(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception as e:
        print(f"Error: {e}")
        return None


def get_phone_number(html_content):
    soup = BeautifulSoup(html_content, 'lxml')
    phone_number_div = soup.find('div', class_='phone-number')
    if phone_number_div:
        phone_number_a = phone_number_div.find('a')
        if phone_number_a and phone_number_a.has_attr('href'):
            pattern = r'^\+?\d{0,3}\(\d{1,}\)\d{3}-\d{2}-\d{2}|\(\d{1,}\)\d{3}-\d{2}-\d{2}$'
            phone_number = re.search(pattern, phone_number_a.text.replace(' ', ''))
            if phone_number:
                return phone_number.group()
    return None


if __name__ == "__main__":
    url = "https://sstmk.ru"
    status, content = check_website(url)
    if status:
        ip_address = get_ip_address("sstmk.ru")
        if ip_address:
            print(f"IP address of sstmk.ru: {ip_address}")
        phone_number = get_phone_number(content)
        if phone_number:
            print(f"Phone number of the company: {phone_number}")
        else:
            print("Phone number not found.")
    else:
        print("Website sstmk.ru is not accessible.")
