import requests

def mobile_agent(url):
    """
    Analyzes mobile-friendliness by checking for viewport meta tag and responsive design hints.
    """
    try:
        resp = requests.get(url, timeout=10)
        html = resp.text
        score = 100
        suggestions = []
        summary = []
        if '<meta name="viewport"' not in html:
            score -= 30
            suggestions.append("Add a viewport meta tag for mobile responsiveness.")
        if 'max-width' not in html:
            score -= 15
            suggestions.append("Use CSS max-width for responsive layouts.")
        if 'touch-action' not in html:
            score -= 10
            suggestions.append("Optimize touch targets for mobile devices.")
        if score > 85:
            summary.append("Excellent mobile experience and responsiveness.")
        elif score > 70:
            summary.append("Good mobile usability, but some improvements possible.")
        else:
            summary.append("Mobile usability issues detected. Optimize for mobile users.")
        return {
            "summary": f"Mobile score for {url}: {score}/100. " + " ".join(summary),
            "score": score,
            "suggestions": suggestions or ["Mobile usability looks great!"]
        }
    except Exception as e:
        return {
            "summary": f"Failed to analyze mobile usability for {url}: {e}",
            "score": 0,
            "suggestions": ["Could not fetch or analyze the website."]
        }