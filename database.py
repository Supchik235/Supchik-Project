import streamlit as st
from deta import Deta

KEY = st.secrets("DATA_KEY")

deta = Deta("a0rilpvt_kQbN234wh5ZUFpDA2VoEBzCYFfsULnV2")
db = deta.Base("cloudst")
               



def insert_period(name,Impo,order,status):
    """Returns the report on a successful creation, otherwise raises an error"""
    return db.put({"key": name,"Impo": Impo, "order": order, "status": status})


def fetch_all_periods():
    """Returns a dict of all periods"""
    res = db.fetch()
    return res.items


def get_period(name):
    """If not found, the function will return None"""
    return db.get(name)

def del_item(name):
    return db.delete(name)





