from app import app
from flask import render_template


@app.route('/admin')
def admin_home():
    return render_template('admin/admin_index.html')


@app.route('/admin/about')
def admin_about():
    return render_template('admin/admin_about.html')
