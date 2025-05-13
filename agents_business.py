import requests

def business_agent(url):
    """
    Analyzes business health by checking for business-related keywords and contact info in the HTML.
    """
    try:
        resp = requests.get(url, timeout=10)
        html = resp.text.lower()
        score = 100
        suggestions = []
        summary = []
        if 'contact' not in html and 'about' not in html:
            score -= 20
            suggestions.append("Add a Contact or About page for business credibility.")
        if 'privacy' not in html and 'terms' not in html:
            score -= 15
            suggestions.append("Add Privacy Policy and Terms of Service.")
        if 'phone' not in html and 'email' not in html:
            score -= 10
            suggestions.append("Provide business phone or email for customer support.")
        if 'kpi' not in html and 'revenue' not in html and 'customer' not in html:
            score -= 10
            suggestions.append("Highlight business KPIs, revenue, or customer testimonials.")
        if score > 85:
            summary.append("Business KPIs are excellent and well-managed.")
        elif score > 70:
            summary.append("Good business health, but some KPIs need attention.")
        else:
            summary.append("Business health concerns detected. Review KPIs urgently.")
        return {
            "summary": f"Business Health score for {url}: {score}/100. " + " ".join(summary),
            "score": score,
            "suggestions": suggestions or ["Business health looks great!"]
        }
    except Exception as e:
        return {
            "summary": f"Failed to analyze business health for {url}: {e}",
            "score": 0,
            "suggestions": ["Could not fetch or analyze the website."]
        }