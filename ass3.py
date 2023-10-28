import ipaddress

def is_private_ipv4(ip_address):
    private_ranges = [
        ipaddress.IPv4Network('10.0.0.0/8'),
        ipaddress.IPv4Network('172.16.0.0/12'),
        ipaddress.IPv4Network('192.168.0.0/16')
    ]
    
    return any(ip_address in private_range for private_range in private_ranges)

def calculate_subnet_mask(num_hosts):
    # Determine the number of bits required for the host part
    num_bits = 1
    while (2 ** num_bits - 2) <= num_hosts:
        num_bits += 1
    
    # Calculate the subnet mask
    subnet_mask = 32 - num_bits
    return f"255.255.255.{256 - (2 ** num_bits)}"

def calculate_subnets(ip_str, num_hosts):
    try:
        ip = ipaddress.IPv4Address(ip_str)
    except ValueError:
        print("Invalid IP address format.")
        return

    subnet_mask = calculate_subnet_mask(num_hosts)

    network = ipaddress.IPv4Network(f'{ip}/{subnet_mask}', strict=False)
    subnets = list(network.subnets())

    print(f"Subnet Mask: {subnet_mask}")
    print("\nSubnets:")
    for subnet in subnets:
        print(f"Subnet: {subnet.network_address} - {subnet.broadcast_address}")

if __name__ == "__main__":
    ip_address_str = input("Enter an IP address (e.g., 192.168.1.0): ")
    num_hosts = int(input("Enter the total number of hosts: "))
    
    calculate_subnets(ip_address_str, num_hosts)
