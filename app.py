from agents import run_all_agents
from report import generate_pdf_report
from flask import Flask, render_template, request, send_from_directory, flash
import os

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'reports')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'supersecretkey'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        results = run_all_agents(url)
        # Move Performance to the top if present
        if "Performance" in results:
            results = {"Performance": results["Performance"], **{k: v for k, v in results.items() if k != "Performance"}}
        # Calculate overall score (average of available agent scores)
        scores = [data['score'] for data in results.values() if 'score' in data]
        overall_score = int(sum(scores) / len(scores)) if scores else 0
        # Generate PDF report
        pdf_path = generate_pdf_report(url, results)
        return render_template('result.html', url=url, results=results, pdf_path=os.path.basename(pdf_path), overall_score=overall_score)
    return render_template('index.html')

@app.route('/download/<filename>')
def download_report(filename):
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
    except FileNotFoundError:
        flash('Report not found.', 'danger')
        return render_template('index.html')

# Future: Implement advanced reporting endpoints and data aggregation here.

if __name__ == '__main__':
    app.run(debug=True)