"""
Internet Protocol version 4 (IPv4) is the fourth version of the Internet Protocol (IP). It is one of the core 
protocols of standards-based internetworking methods in the Internet, and was the first version deployed for 
production in the ARPANET in 1983. It still routes most Internet traffic today.

Given an IPv4 address, find the equivalent integer and IPv4-mapped IPv6 address.

If the input string does not represent a valid IPv4 address, return an empty array.

Example

convertIPv4("216.58.200.14") = ["3627730958", "0:0:0:0:0:ffff:d83a:c80e"]

This example is the ip of google.com. You can try to visit http://216.58.200.14 or http://3627730958.

[time limit] 4000ms (py)
[input] string ip_v4_address

A non-empty string.

[output] array.string

Array of two strings in the following format: [IP Integer, IPv4-mapped IPv6 address]. Please, note that in each group
of hexadecimal digits in IPv4-mapped IPv6 address leading zeroes should be omitted.

# Challenge's link: https://codefights.com/challenge/in6dpQuF99YPNazib #
"""
def convertIPv4(ip_v4_address):
    octets = ip_v4_address.split('.')
    for octet in octets:
        if not octet.isdigit():
            return []
    
    if len(octets) != 4:
        return []
    octets = map(int, octets)
    hex_digits = '0123456789abcdef'
    
    # equivalent integer 
    equivalent_integer = sum([octet * 256 ** (3 - i) for i, octet in enumerate(octets)])
    equivalent_integer = str(equivalent_integer)

    # map IPv4 to IPv6
    prefix = '0:0:0:0:0:ffff:'
    ip_v6 = []
    
    for octet in octets:
        if octet < 0 or octet > 255:
            return []
        ip_v6.append(hex_digits[octet / 16])
        ip_v6.append(hex_digits[octet % 16])
        
    
    # remove leading zeros
    first_part, second_part = ip_v6[:4], ip_v6[4:]
    first_part = remove_leading_zeros(first_part)
    second_part = remove_leading_zeros(second_part)
    ip_v6 = prefix + ''.join(first_part) + ':' + ''.join(second_part)
    
    return [equivalent_integer, ip_v6]

def remove_leading_zeros(s):
    i = 0
    while i < len(s) - 1:
        if s[i] != '0':
            break 
        i += 1
    return s[i:]