import os
import requests
from bs4 import BeautifulSoup
import time

def performance_agent(url):
    """
    Analyzes website performance using direct HTTP requests and HTML parsing.
    Returns a precise score and suggestions based on key performance factors: load time, resource count, and use of modern web standards.
    """
    try:
        start_time = time.time()
        resp = requests.get(url, timeout=15)
        load_time = time.time() - start_time
        html = resp.text
        soup = BeautifulSoup(html, 'html.parser')
        scripts = soup.find_all('script', src=True)
        styles = soup.find_all('link', rel=lambda x: x and 'stylesheet' in x)
        images = soup.find_all('img')
        videos = soup.find_all('video')
        if resp.headers.get('Content-Encoding') == 'gzip':
            gzip_used = True
        else:
            gzip_used = False
        total_assets = len(scripts) + len(styles) + len(images) + len(videos)
        suggestions = []
        score = 100
        if load_time > 3:
            score -= 25
            suggestions.append(f"Page load time is high: {load_time:.2f}s. Optimize server response and assets.")
        elif load_time > 2:
            score -= 10
            suggestions.append(f"Page load time is moderate: {load_time:.2f}s. Further optimization possible.")
        if len(scripts) > 10:
            score -= 10
            suggestions.append("Too many JavaScript files. Consider bundling/minifying scripts.")
        if len(styles) > 5:
            score -= 10
            suggestions.append("Too many CSS files. Combine and minify stylesheets.")
        if len(images) > 20:
            score -= 10
            suggestions.append("Too many images. Optimize or lazy-load images.")
        if len(videos) > 2:
            score -= 10
            suggestions.append("Too many videos. Consider lazy-loading or optimizing video content.")
        if total_assets > 30:
            score -= 10
            suggestions.append("High number of assets. Reduce requests for better performance.")
        if not gzip_used:
            score -= 5
            suggestions.append("Gzip compression not detected. Enable gzip for faster transfers.")
        if 'viewport' not in html:
            score -= 5
            suggestions.append("Missing viewport meta tag. Add for better mobile performance.")
        if score > 85:
            summary = "Excellent performance detected."
        elif score > 70:
            summary = "Good performance, but improvements possible."
        else:
            summary = "Performance issues found. Immediate attention recommended."
        if not suggestions:
            suggestions = ["Performance looks great!"]
        return {
            "summary": f"Performance score for {url}: {score}/100. " + summary,
            "score": score,
            "suggestions": suggestions[:3]
        }
    except Exception as e:
        return {
            "summary": f"Failed to analyze performance for {url}: {e}",
            "score": 0,
            "suggestions": ["Could not fetch or analyze the website."]
        }