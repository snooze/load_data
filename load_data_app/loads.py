from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from load_data_app.auth import login_required
from load_data_app.db import get_db

bp = Blueprint('loads', __name__)

@bp.route('/')
def index():
    db = get_db()
    loads = db.execute(
        'SELECT p.id, title, notes, created, author_id, username'
        ' FROM metallic_load p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('loads/index.html', posts=loads)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        notes = request.form['notes']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO metallic_load (title, notes, author_id)'
                ' VALUES (?, ?, ?)',
                (title, notes, g.user['id'])
            )
            db.commit()
            return redirect(url_for('loads.index'))

    return render_template('loads/create.html')

def get_load(id, check_author=True):
    load = get_db().execute(
        'SELECT p.id, title, notes, created, author_id, username'
        ' FROM metallic_load p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if load is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and load['author_id'] != g.user['id']:
        abort(403)

    return load

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    load = get_load(id)

    if request.method == 'POST':
        title = request.form['title']
        notes = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE metallic_load SET title = ?, notes = ?'
                ' WHERE id = ?',
                (title, notes, id)
            )
            db.commit()
            return redirect(url_for('loads.index'))

    return render_template('loads/update.html', post=load)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_load(id)
    db = get_db()
    db.execute('DELETE FROM metallic_load WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('loads.index'))
