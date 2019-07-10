from flask import Blueprint

main = Blueprint('main', __name__, template_folder='templates')

# this is to avoid the circular imports, importing at the end

from app.catalog import routes
