import os
from peewee import \
    CharField, BooleanField, TextField, Model, SqliteDatabase, \
    DateField, ForeignKeyField, IntegerField
import datetime

BASE_DIR = os.path.dirname(__file__)

db = SqliteDatabase('%s/banco.db' % BASE_DIR)

class Politician(Model):
    name = CharField(max_length=200)
    party = CharField(max_length=50)

    class Meta:
        database = db


class Presence(Model):
    politician = ForeignKeyField(Politician, related_name='presences')

    date = DateField()
    is_presente = BooleanField()
    frequencia_no_dia = CharField(max_length=250)
    justificativa = CharField(max_length=250, null=True)
    qtde_sessoes = IntegerField(default=0)

    class Meta:
        database = db


class PresenceSession(Model):
    presence = ForeignKeyField(Presence, related_name='sessions')

    description = CharField(max_length=250)
    is_presente = BooleanField()

    class Meta:
        database = db


def install_database():
    db.create_tables([Politician, Presence, PresenceSession])