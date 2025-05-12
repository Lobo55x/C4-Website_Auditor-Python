import requests

def uiux_agent(url):
    """
    Analyzes UI/UX by checking for accessibility and navigation hints in the HTML.
    """
    try:
        resp = requests.get(url, timeout=10)
        html = resp.text
        score = 100
        suggestions = []
        summary = []
        if 'nav' not in html:
            score -= 15
            suggestions.append("Add a <nav> element for better navigation.")
        if 'aria-' not in html:
            score -= 10
            suggestions.append("Add ARIA attributes for accessibility.")
        if 'contrast' not in html and 'color' not in html:
            score -= 10
            suggestions.append("Ensure sufficient color contrast for accessibility.")
        if score > 85:
            summary.append("Outstanding user experience and accessibility.")
        elif score > 70:
            summary.append("Good UI/UX, but some areas can be improved.")
        else:
            summary.append("UI/UX issues detected. Consider redesign for better usability.")
        return {
            "summary": f"UI/UX score for {url}: {score}/100. " + " ".join(summary),
            "score": score,
            "suggestions": suggestions or ["UI/UX looks great!"]
        }
    except Exception as e:
        return {
            "summary": f"Failed to analyze UI/UX for {url}: {e}",
            "score": 0,
            "suggestions": ["Could not fetch or analyze the website."]
        }