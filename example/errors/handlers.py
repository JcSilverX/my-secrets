from flask import Blueprint, render_template

errors_bp = Blueprint(
    'errors',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@errors_bp.app_errorhandler(403)
def forbidden_page(error):
    return render_template('errors/403.html'), 403


@errors_bp.app_errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404


@errors_bp.app_errorhandler(500)
def server_error_page(error):
    return render_template('errors/500.html'), 500
