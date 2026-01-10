from listening_port import is_listening_port

def test_listening_port():
    """
    Check if a listening port is open on httpbin.org
    """
    assert is_listening_port(ipaddr="example.com", port=443)

def test_non_listening_port():
    """Test that a non-listening port is correctly identified"""
    # Use a high port number that's unlikely to be in use
    # Note: On Unix-like systems, ports below 1024 are privileged
    unused_port = 65535
    
    # Test that our function correctly identifies the port as not listening
    # We'll use localhost to avoid any network issues
    assert not is_listening_port(ipaddr="localhost", port=unused_port)