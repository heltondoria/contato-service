import logging

from flask import Flask
from logging import FileHandler, Formatter

app = Flask(__name__)


@app.route('/contatos', methods=['GET'])
@app.route('/contatos?<int:page>')
def list_contato():
    pass


@app.route('/contatos/<id>', methods=['GET'])
def get_contato(id):
    pass


@app.route('/contatos', methods=['POST'])
def create_contato():
    pass


@app.route('/contatos/<id>', methods=['PUT'])
def update_contato(id):
    pass


@app.route('/contatos/<id>', methods=['DELETE'])
def delete_contato(id):
    pass


@app.errorhandler(500)
def internal_error(error):
    # db_session.rollback()
    return 'Server error'


@app.errorhandler(404)
def not_found_error(error):
    return 'Not found'


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

if __name__ == '__main__':
    app.run()
