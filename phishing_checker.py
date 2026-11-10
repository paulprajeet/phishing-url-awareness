    
import re
from urllib.parse import urlparse


def inspect_url(raw_url):
    findings = []

    try:
        parsed_url = urlparse(raw_url)
        hostname = parsed_url.hostname

        # Check 1: @ symbol
        if "@" in raw_url:
            findings.append("URL contains an '@' symbol.")

        # Check 2: URL length
        if len(raw_url) > 100:
            findings.append("URL length is greater than 100 characters.")

        # Check 3: IPv4-looking hostname
        if hostname and re.match(r"^\d{1,3}(\.\d{1,3}){3}$", hostname):
            findings.append("Hostname looks like an IPv4 address.")

        # Check 4: Too many hostname segments
        if hostname and len(hostname.split(".")) >= 5:
            findings.append("Hostname contains 5 or more segments.")

        # Check 5: Punycode marker
        if hostname and "xn--" in hostname.lower():
            findings.append("Hostname contains a punycode marker (xn--).")

        # Check 6: HTTP scheme
        if parsed_url.scheme.lower() == "http":
            findings.append("URL uses HTTP instead of HTTPS.")

    except ValueError:
        findings.append("Invalid or malformed URL.")

    return findings


def main():
    print("=" * 50)
    print("       PHISHING URL AWARENESS CHECKER")
    print("=" * 50)

    while True:
        url = input("\nEnter a URL (or type 'quit' to exit): ").strip()

        if url.lower() == "quit":
            print("\nThank you for using the checker!")
            break

        if not url:
            print("Please enter a URL.")
            continue

        findings = inspect_url(url)

        print("\n--- URL ANALYSIS ---")
        print("URL:", url)

        if findings:
            print("\nWarning signs detected:")
            for finding in findings:
                print("[WARNING]", finding)

            print("\nResult: Review this URL carefully.")
        else:
            print("\nNo listed warning signs were detected.")
            print("This does NOT mean the URL is safe.")

        print("-" * 50)


if __name__ == "__main__":
    main()
