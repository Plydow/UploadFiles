from flask import Blueprint, render_template, session, request, jsonify, current_app
from ..decorators import login_required

import os

views = Blueprint('business', __name__)

@views.route('/context')
@login_required
def base_context():
    return {'logged_in': session.get('logged_in', False)}

@views.route('/upload')
@login_required
def upload():
    return render_template('upload.html', folders=current_app.config['EXPORT_PATH'])

@views.route('/proccess', methods=['POST'])
@login_required
def proccess():
    if 'files[]' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    files = request.files.getlist('files[]')
    folder = request.form['folder']

    for file in files:
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        filepath = os.path.join(current_app.config['BASE_EXPORT_PATH'], folder, file.filename)
        file.save(filepath)

    return jsonify({'success': 'Files uploaded successfully'}), 200
