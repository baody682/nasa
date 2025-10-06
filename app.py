from flask import Flask, render_template, url_for
import os 

STATIC_PLOT_FILENAME = 'hotspot_globe_npp_strict_mask.html' 
STATIC_PLOT_PATH = 'images/' + STATIC_PLOT_FILENAME

STATIC_PLOT_FILENAME_2 = 'hotspot_globe_3d.html' 
STATIC_PLOT_PATH_2 = 'images/' + STATIC_PLOT_FILENAME_2

os.makedirs('static/images', exist_ok=True) 

app = Flask(__name__)

@app.route('/')
def home():
    hotspot_globe_url = url_for('static', filename=STATIC_PLOT_PATH) 
    return render_template('index.html', hotspot_globe_url=hotspot_globe_url) 

@app.route('/tag_details')
def tag_details():
    return render_template('tag.html')

@app.route('/mathematical_model')
def mathematical_model():
    hotspot_globe_url_value = url_for('static', filename=STATIC_PLOT_PATH_2)  
    return render_template('model.html', hotspot_globe_3d=hotspot_globe_url_value)

@app.route('/research_details')
def research_details():
    return render_template('research.html')

if __name__ == '__main__':
    app.run(debug=True)