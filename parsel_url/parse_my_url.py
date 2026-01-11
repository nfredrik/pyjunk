import re
from urllib.parse import urlparse, unquote
from typing import Tuple, Optional


def parse_jenkins_url(url: str) -> Tuple[str, str]:
    """
    Parse a Jenkins job URL and extract the job name and build number.
    
    Args:
        url: The Jenkins job URL (e.g., 'http://jenkins/job/My%20Job/42/')
        
    Returns:
        A tuple of (job_name, job_id)
        
    Raises:
        ValueError: If the URL is invalid or doesn't match the expected Jenkins job URL format
        
    Example:
        >>> parse_jenkins_url("http://localhost:8080/job/My%20Job/42/")
        ('My Job', '42')
    """
    if not url:
        raise ValueError("URL cannot be empty or None")

    try:
        parts = urlparse(unquote(url))
    except Exception as e:
        raise ValueError(f"Invalid URL: {e}")

    if not all([parts.scheme, parts.netloc]):
        raise ValueError("Invalid URL: missing scheme or netloc")

    # Match job name (allowing spaces, hyphens, etc.) and build number
    match = re.search(r'/job/([^/]+?)/(\d+)(?:/|$)', parts.path)
    if not match:
        raise ValueError(
            "Invalid Jenkins job URL format. "
            "Expected format: http(s)://<host>/job/<job_name>/<build_number>/"
        )

    job_name = match.group(1)
    job_id = match.group(2)

    if not job_name:
        raise ValueError("Could not extract job name from URL")
    if not job_id.isdigit():
        raise ValueError(f"Invalid build number: {job_id}")

    return job_name, job_id


if __name__ == "__main__":
    # Example usage
    test_urls = [
        "http://localhost:8080/job/fredde%20med%20mera/1/console",
        "http://jenkins.example.com/job/Test-Job/42/",
        "http://jenkins.example.com/job/Project%20X/123/build"
    ]
    
    for url in test_urls:
        try:
            job_name, job_id = parse_jenkins_url(url)
            print(f"URL: {url}")
            print(f"  Job Name: {job_name}")
            print(f"  Build ID: {job_id}")
        except ValueError as e:
            print(f"Error parsing URL '{url}': {e}")
