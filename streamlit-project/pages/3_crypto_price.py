
import pandas as pd
import streamlit as st
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'
parameters = {
  'slug' : 'bitcoin',
}
headers = {
  "X-CMC_PRO_API_KEY": "c293622c-65c9-4490-81f6-61a5c1930bb1",
  "Content-Type": "application/x-www-form-urlencoded"
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  payload = response.json()
  st.write(payload)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  st.write(e)


st.write(payload.keys())

df = pd.DataFrame(payload['data'])
df