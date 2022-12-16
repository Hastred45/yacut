from datetime import datetime

from flask import url_for

from yacut import db


class URLMap(db.Model):
    API_FIELDS = {
        'url': 'original',
        'custom_id': 'short',
    }

    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(1024), nullable=False)
    short = db.Column(db.String(16), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for(
                'redirect_view', custom_id=self.short, _external=True
            )
        )

    def from_dict(self, data):
        for field in self.API_FIELDS:
            if field in data:
                setattr(self, self.API_FIELDS[field], data[field])
