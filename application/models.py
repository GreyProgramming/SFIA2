from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from enum import Enum

# Enums for 5e stuff

class size(Enum):
	Small = 1
	Medium = 2

class speed(Enum):
	25 ft = 1
	25/50 ft = 2
	30 ft = 3
	30/20C = 4
	30/30S = 5
	35 ft = 6
	40 ft = 7

class source(Enum):
	PHB = 1			# Player's Handbook
	DMG = 2			# Dungeon Master's Guide
	GGtR = 3		# Guildmasters' Guide to Ravnica
	EE = 4			# Elemental Evil Player's Companion
	MToF = 5		# Mordenkainens Tome of Foes
	SCG = 6			# Sword Coast Adventurer's Guide
	VGtM = 7		# Volo's Guide to Monsters
	PSK = 8			# Plane Shift: Kaladesh				https://media.wizards.com/2017/downloads/magic/Plane-Shift_Kaladesh.pdf
	PSZ = 9			# Plane Shift: Zendikar				https://media.wizards.com/2016/downloads/magic/Plane%20Shift%20Zendikar.pdf
	UAE = 10		# Unearthed Arcana: Eberron			https://media.wizards.com/2015/downloads/dnd/UA_Eberron_v1.pdf
	UAEG = 11 		# Unearthed Arcana: Eladrin & Gith		https://media.wizards.com/2017/dnd/downloads/UA-Eladrin-Gith.pdf
	UAWB = 12		# Unearthed Arcana: Waterborne Adventures	https://media.wizards.com/2015/downloads/dnd/UA_Waterborne_v3.pdf
	VGtM = 13		# Volo's Guide to Monsters


# Tables for the 5e stuff
class Language(db.Model):
	L_ID = db.Column(db.Integer, primary_key=True)
	Language = db.Column(db.String(15), nullable=False)
	Script = db.Column(db.String(15), nullable=False)

class Race(db.Model):
	R_ID = db.Column(db.Integer, primary_key=True)
	Fullname = db.Column(db.String(50), nullable=False)
	size = db.Column(db.String(10), nullable=False, Enum(size))
	speed = db.Column(db.string(10), nullable=False, Enum(speed))
	Language1 = db.Column(db.Integer, db.ForeignKey('language.l_id'), nullable=False)
	Language2 = db.Column(db.Integer, db.ForeignKey('language.l_id'), nullable=True)
	STRmod = db.Column(db.Integer(), default=0)
	DEXmod = db.Column(db.Integer(), default=0)
	CONmod = db.Column(db.Integer(), default=0)
	INTmod = db.Column(db.Integer(), default=0)
	WISmod = db.Column(db.Integer(), default=0)
	CHAmod = db.Column(db.Integer(), default=0)
	FREEmod = db.Column(db.Integer(), default=0)
	Notes = db.Column(db.String(1000))
	Source = db.Column(sb.String(5), Nullable = False, Enum(source))

class Spells(db.Model):
        S_ID = db.Column(db.Integer, primary_key=True)





class Feats(db.Model):
        F_ID = db.Column(db.Integer, primary_key=True)





class Gear(db.Model):
        G_ID = db.Column(db.Integer, primary_key=True)





class Weapons(db.Model):
        W_ID = db.Column(db.Integer, primary_key=True)





class Armour(db.Model):
        A_ID = db.Column(db.Integer, primary_key=True)





class Mounts(db.Model):
        M_ID = db.Column(db.Integer, primary_key=True)





class Vehicles(db.Model):
        V_ID = db.Column(db.Integer, primary_key=True)





class TradeGoods(db.Model):
        T_ID = db.Column(db.Integer, primary_key=True)





class Consumables(db.Model):
        C_ID = db.Column(db.Integer, primary_key=True)






# Tables for user functionality

class Posts(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False, unique=True)
	content = db.Column(db.String(1000), nullable=False, unique=True)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

	def __repr__(self):
		return ''.join([
			'User ID: ', str(self.user_id), '\r\n',
			'Title: ', self.title, '\r\n', self.content
		])

@login_manager.user_loader
def load_user(id):
	return Users.query.get(int(id))

class Users(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(30), nullable=False)
	last_name = db.Column(db.String(30), nullable=False)
	email = db.Column(db.String(150), nullable=False, unique=True)
	password = db.Column(db.String(200), nullable=False)
	posts = db.relationship('Posts', backref='author', lazy=True)

	def __repr__(self):
		return ''.join([
			'UserID: ', str(self.id), '\r\n',
			'Email: ', self.email, '\r\n',
			'Name: ', self.first_name, ' ', self.last_name
		])

class Content(db.Model):
	c_id = db.Column(db.Integer, primary_key=True)
	rolemodel = db.Column(db.String(50), nullable=False)
	history = db.Column(db.VARCHAR(10000), nullable = False)
	resources = db.Column(db.VARCHAR(5000))
	pictures = db.Column(db.VARCHAR(5000))
