# -*- coding: utf-8 -*-
import datetime
from sqlalchemy.orm import class_mapper


def model_to_dict(obj, available_relation_list=None,
                  format_dt=str, fields=None):
    def _get_dict_data(columns):
        if fields:
            columns = filter(lambda x: x in fields, columns)
        out = dict(map(lambda c: (c, format_dt(getattr(obj, c))) if isinstance(getattr(obj, c), datetime.datetime) else (c, getattr(obj, c)), columns))
        return out

    fields = fields or []
    if not hasattr(obj, '__table__'):
        if not hasattr(obj, '_fields'):
            raise Exception(u'expect table instance')
        else:
            columns = obj._fields
            return _get_dict_data(columns)
    mapper = class_mapper(obj.__class__)
    columns = [column[0] for column in obj._sa_instance_state.attrs.items()]
    out = _get_dict_data(columns)
    available_relation_list = available_relation_list or []
    for name, relation in mapper.relationships.items():
        if name not in available_relation_list:
            if name in out:
                del out[name]
            continue
        related_obj = getattr(obj, name)
        if related_obj is not None:
            if relation.uselist:
                out[name] = [model_to_dict(child, available_relation_list)
                             for child in related_obj]
            else:
                out[name] = model_to_dict(related_obj, available_relation_list)
    return out


def db_to_dict():
    def _wrapped(self, available_relation_list=None, format_dt=str,
                 fields=None):
        return model_to_dict(self, available_relation_list, format_dt, fields)

    def _wrapper(self, *args, **kwargs):
        return _wrapped(self, *args, **kwargs)

    return _wrapper
