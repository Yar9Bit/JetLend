import requests


def my_ip(site_url) -> str:
    resp = requests.get(site_url)
    public_ip = resp.text
    print(public_ip)
    return public_ip


if __name__ == '__main__':
    site = 'https://ifconfig.me/'
    my_ip(site)
