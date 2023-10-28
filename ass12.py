'''
Shantanu Ekad TA14
Domain name
'''
import socket

def dns_lookup(domain_name):
    try:
        ip_address = socket.gethostbyname(domain_name)
        print(f"IP Address for {domain_name} is {ip_address}")
    except socket.gaierror:
        print(f"Unable to resolve the IP address for {domain_name}")

if __name__ == "__main__":
    domain_name = input("Enter a domain name: ")
    dns_lookup(domain_name)
'''
OUTPUT:
Enter a domain name: reddit.com
IP Address for reddit.com is 151.101.65.140
Enter a domain name: web.whatsapp.com
IP Address for web.whatsapp.com is 157.240.16.52

'''