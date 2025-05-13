import requests

def code_agent(url):
    """
    Analyzes code quality by checking for inline scripts, minified JS, and code comments in the HTML.
    """
    try:
        resp = requests.get(url, timeout=10)
        html = resp.text
        score = 100
        suggestions = []
        summary = []
        if '<script>' in html and '//' in html:
            score -= 10
            suggestions.append("Avoid inline scripts; use external JS files.")
        if '.min.js' not in html:
            score -= 10
            suggestions.append("Use minified JavaScript for better performance.")
        if '//' not in html and '/*' not in html:
            score -= 10
            suggestions.append("Add comments to your code for maintainability.")
        if score > 85:
            summary.append("Codebase is clean and maintainable.")
        elif score > 70:
            summary.append("Good code quality, but some refactoring suggested.")
        else:
            summary.append("Code issues detected. Refactoring recommended.")
        return {
            "summary": f"Code quality score for {url}: {score}/100. " + " ".join(summary),
            "score": score,
            "suggestions": suggestions or ["Code quality looks great!"]
        }
    except Exception as e:
        return {
            "summary": f"Failed to analyze code quality for {url}: {e}",
            "score": 0,
            "suggestions": ["Could not fetch or analyze the website."]
        }