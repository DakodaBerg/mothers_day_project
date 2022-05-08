from flask import Flask
app = Flask(__name__)
app.secret_key = "Aa1242462"
DATABASE = 'mothersday'

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)