import socket

domain = "www.kame.net"

print(f"Resolving DNS for {domain}...\n")

try:
    ipv4_info = socket.getaddrinfo(domain, None, socket.AF_INET)
    ipv4_addresses = {result[4][0] for result in ipv4_info}
    print("IPv4 Addresses:")
    for addr in ipv4_addresses:
        print(f"  - {addr}")
except Exception as e:
    print("Failed to resolve IPv4:", e)

try:
    ipv6_info = socket.getaddrinfo(domain, None, socket.AF_INET6)
    ipv6_addresses = {result[4][0] for result in ipv6_info}
    print("\nIPv6 Addresses:")
    for addr in ipv6_addresses:
        print(f"  - {addr}")
except Exception as e:
    print("Failed to resolve IPv6:", e)
