
from curses import BUTTON2_DOUBLE_CLICKED
from flask import Blueprint, jsonify, abort, make_response



books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

