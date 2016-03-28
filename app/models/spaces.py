from .. import db


class Spaces(db.Model):

  id = db.Column(db.Integer, primary_key=True)
  # Additional fields
  name = db.Column(db.String(128), nullable=False)
  is_active = db.Column(db.Boolean,
                        nullable=False,
                        server_default='1',
                        default=True)
  updated_at = db.Column(db.DateTime,
                         nullable=False,
                         server_default=db.text(
                           'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
  created_at = db.Column(db.DateTime,
                         nullable=False,
                         server_default=db.text('CURRENT_TIMESTAMP'))

  def __repr__(self):
    return 'Spaces {}>'.format(self.id)
