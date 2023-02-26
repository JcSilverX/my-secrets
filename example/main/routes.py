from flask import Blueprint, render_template

main_bp = Blueprint(
    'main',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@main_bp.route('/')
@main_bp.route('/home')
def home():
    return render_template('main/index.html')
