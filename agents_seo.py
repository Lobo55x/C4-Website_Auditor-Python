import requests

def seo_agent(url):
    """
    Analyzes website SEO using a real-time fetch and basic checks for meta tags, title, and alt attributes.
    """
    try:
        resp = requests.get(url, timeout=10)
        html = resp.text
        score = 100
        suggestions = []
        summary = []
        if '<title>' not in html or '</title>' not in html:
            score -= 20
            suggestions.append("Add a <title> tag for better SEO.")
        if '<meta name="description"' not in html:
            score -= 15
            suggestions.append("Add a meta description tag.")
        if 'alt="' not in html:
            score -= 10
            suggestions.append("Add alt attributes to images.")
        if '<h1' not in html:
            score -= 10
            suggestions.append("Add at least one <h1> heading.")
        if score > 85:
            summary.append("Excellent SEO practices detected.")
        elif score > 70:
            summary.append("Good SEO, but improvements possible.")
        else:
            summary.append("Several SEO issues found. Immediate attention recommended.")
        return {
            "summary": f"SEO score for {url}: {score}/100. " + " ".join(summary),
            "score": score,
            "suggestions": suggestions or ["SEO looks great!"]
        }
    except Exception as e:
        return {
            "summary": f"Failed to analyze SEO for {url}: {e}",
            "score": 0,
            "suggestions": ["Could not fetch or analyze the website."]
        }