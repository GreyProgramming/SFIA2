from application import db
from application.models import Posts, Users, Content

db.drop_all()
db.create_all()
