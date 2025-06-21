import re

def test_match(test):
    # Pattern for IPv4 address (not strict, but matches general format)
    pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
    ips = re.findall(pattern, test)
    if ips:
        print("IP addresses found:", ips)
    else:
        print("No IP address found.")

# Example test cases
print('Test 1:')
test_match("The quick brown fox jumps over the lazy dog")        # No IP address
print('Test 2:')
test_match("234.56.78.90 is a valid IP, but 999.999.999.999 is not.") # Should find 234.56.78.90
print('Test 3:')
test_match("My IPs are 192.168.1.1 and 10.0.0.1.") # Should find both IPs
