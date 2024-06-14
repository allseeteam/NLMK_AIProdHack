import streamlit as st
import datetime
from queries.query import query
import utils
import json


@st.cache_data
def get_items():
    with open("data/url_items_all.json", "r") as f:
        url_items = json.load(f)
    
    for item in url_items:
        item['relevance'] = int(item['relevance'])
        item['date'] = utils.parse_date(item['date'])
        
    # sort by relevance
    url_items = sorted(url_items, key=lambda x: x['relevance'], reverse=True)
    return url_items


today = datetime.datetime.now()
end = datetime.datetime(today.year, today.month, today.day)
start = end - datetime.timedelta(days=7)

url_items = get_items()


st.title('Дайджест новостей НЛМК')

category = st.selectbox('Категории', ['Все']+list(query.keys()))

d = st.date_input(
    "Выберите отрезок времени",
    (start, end),
    format="MM.DD.YYYY",
)
if len(d) == 2:
    d0, d1 = d
    # convert to datetime
    d0 = datetime.datetime.combine(d0, datetime.datetime.min.time())
    d1 = datetime.datetime.combine(d1, datetime.datetime.min.time())

    # filter by category
    if category != 'Все':
        url_items = [item for item in url_items if item['category'] == category]

    # filter by date
    url_items = [item for item in url_items if item['date'] is not None and d0 <= item['date'] <= d1]

    # Improved display format for news items
    for item in url_items[:10]:
        date = item['date']
        if date is not None:
            date = date.strftime('%d.%m.%Y')
        summary = item['answer']['summary']
        events = item['answer']['key_events']
        if isinstance(events, list):
            events = '\n - '.join(events)
        st.markdown(f"#### **{item['title']}**")
        st.markdown(f"*{item['category']}* | *{date}*")
        st.markdown(f"**Summary:** {summary}")
        st.markdown(f"**Events:** \n{events}")
        web_url = '/'.join(item['url'].split('/')[:3])
        st.markdown(f"Полная версия: [{web_url}]({item['url']})")
        st.markdown(f"**Relevance:** {item['relevance']}")
        st.write('---')

