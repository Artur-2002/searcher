from app import db
from datetime import datetime

class Document(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	rubrics = db.Column(db.String(64))
	text = db.Column(db.String(64))
	created_date = db.Column(db.String(64))

	def __repr__(self):
		return str(self.id)

	def get_rubrics(self):
		result = self.rubrics
		result = result.replace('[', '').replace(']', '').replace(' ', '').replace("'", "")

		return result

	def get_created_date(self):
		parse_rule = '%Y-%m-%d %H:%M:%S'

		return datetime.strptime(self.created_date, parse_rule)