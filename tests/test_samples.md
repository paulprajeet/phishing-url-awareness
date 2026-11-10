# Phishing URL Awareness Checker – Test Results

## Project Details
- **Project:** Phishing URL Awareness Checker
- **Language:** Python 3.14.10
- **Testing type:** Manual testing
- **Purpose:** Identify common warning signs in URL text without visiting the website.

## Test Cases

| Test | Input URL | Expected warning signs | Actual status |
|---|---|---|---|
| 1 | `http://192.0.2.10/account` | IPv4-looking hostname, HTTP | PASS |
| 2 | `https://www.example.com/login` | No listed warning signs | PASS |
| 3 | `http://example.com@sample.invalid/login` | `@` symbol, HTTP | PASS |
| 4 | `https://a.b.c.d.e.example.invalid/path` | Hostname has 5 or more segments | PASS |
| 5 | `https://xn--example.invalid/` | Punycode marker | PASS |

## Test Observations

1. The program successfully identifies an IPv4-looking hostname.
2. The program detects URLs that use HTTP instead of HTTPS.
3. The program checks for the presence of the `@` symbol.
4. The program checks the number of hostname segments.
5. The program identifies the `xn--` punycode marker.
6. The program displays a cautionary message when warning signs are found.

## Conclusion

The five sample URLs were used to test the URL warning-sign detection functionality. The program analyzes URL text locally and does not visit websites or make network requests.

**Important limitation:** The absence of detected warning signs does not guarantee that a URL is safe. This project is an educational awareness tool, not a complete phishing detection system.

## Evidence

Screenshots of the actual program execution are saved in the `screenshots` folder.
