# -*- coding: utf-8 -*-

from cards import db


class RedCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'Red_card("{self.text}")'


class WhiteCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'White_card("{self.text}")'
