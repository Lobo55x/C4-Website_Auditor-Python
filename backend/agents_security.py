import requests

def security_agent(url):
    """
    Analyzes website security by checking for HTTPS, security headers, and basic vulnerabilities.
    """
    try:
        resp = requests.get(url, timeout=10)
        score = 100
        suggestions = []
        summary = []
        if not url.startswith("https://"):
            score -= 30
            suggestions.append("Implement HTTPS for secure communication.")
        headers = resp.headers
        if "Content-Security-Policy" not in headers:
            score -= 15
            suggestions.append("Add a Content-Security-Policy header.")
        if "X-Frame-Options" not in headers:
            score -= 10
            suggestions.append("Add X-Frame-Options header to prevent clickjacking.")
        if "X-Content-Type-Options" not in headers:
            score -= 5
            suggestions.append("Add X-Content-Type-Options header.")
        if score > 85:
            summary.append("Site is highly secure with best practices in place.")
        elif score > 70:
            summary.append("Good security, but some vulnerabilities found.")
        else:
            summary.append("Security issues detected. Immediate action required.")
        return {
            "summary": f"Security score for {url}: {score}/100. " + " ".join(summary),
            "score": score,
            "suggestions": suggestions or ["Security looks great!"]
        }
    except Exception as e:
        return {
            "summary": f"Failed to analyze security for {url}: {e}",
            "score": 0,
            "suggestions": ["Could not fetch or analyze the website."]
        }