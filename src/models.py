# import logging

from datetime import date, datetime

from dateutil.relativedelta import relativedelta

import peewee
# import peewee_migrate

from config import cfg_database_filename


db = peewee.SqliteDatabase(cfg_database_filename)
# # db.connect()
#
# logger = logging.getLogger(__name__)
# router = peewee_migrate.Router(db, migrate_table='migration', logger=logger)


class Nutrient(peewee.Model):
    conductivity = peewee.IntegerField(column_name='condutividade')
    ph_level = peewee.DoubleField(column_name='nivel_ph')
    local_temperature = peewee.IntegerField(column_name='temperatura_ambiente')
    water_temperature = peewee.IntegerField(column_name='temperatura_agua')
    local_humidity = peewee.IntegerField(column_name='umidade_ambiente')
    record_date = peewee.DateTimeField(column_name='data_registro', default=datetime.now)

    class Meta:
        database = db
        db_table = 'nutrientes'


class Customer(peewee.Model):
    name = peewee.CharField(column_name='nome')
    birth_date = peewee.DateField(column_name='nascimento')
    cpf = peewee.CharField(column_name='cpf')
    email = peewee.CharField(column_name='email')
    phone = peewee.CharField(column_name='telefone')
    city = peewee.CharField(column_name='cidade')
    state = peewee.CharField(column_name='uf')
    record_date = peewee.DateTimeField(column_name='data_registro', default=datetime.now)

    @property
    def age(self) -> int:
        birth_date: date = date(
            year=self.birth_date.year,
            month=self.birth_date.month,
            day=self.birth_date.day
        )
        return relativedelta(dt1=date.today(), dt2=birth_date).years

    class Meta:
        database = db
        db_table = 'clientes'
