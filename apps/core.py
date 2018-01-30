from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_uploads import UploadSet

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
photos = UploadSet('PHOTO')
