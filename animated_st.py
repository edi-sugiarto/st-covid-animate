import plotly.express as px
import streamlit as st
import pandas as pd

df = px.data.gapminder()

st.write(df)

year_options = df['year'].unique().tolist()
# year = st.selectbox('Which year yould you like to see?', year_options, 0)
# df = df[df['year'] == year]

st.markdown('## GDP vs Life Expectancy Evolution')

fig = px.scatter(df, x='gdpPercap', y='lifeExp',
                 size='pop', color='continent', hover_name='country',
                 log_x=True, size_max=55, range_x=[100, 100000], range_y=[25, 90],
                 animation_frame='year', animation_group='country')

fig.update_layout(width=800)
st.write(fig)


# Different section
covid = pd.read_csv('daily-new-confirmed-cases-of-covid-19-tests-per-case.csv')
covid.columns = ['Country', 'Code', 'Date', 'Confirmed', 'Days since confirmed']
covid['Date'] = pd.to_datetime(covid['Date']).dt.strftime('%Y-%m-%d')
country_options = covid['Country'].unique().tolist()

st.write(covid)

date_options = covid['Date'].unique().tolist()
# date = st.selectbox('Which date would you like to see?', date_options, 100)
country = st.multiselect('Which country would you like to see?', country_options, ['Brazil', 'United States', 'India'])

st.markdown('## Daily Covid Cases Evolution')

covid = covid[covid['Country'].isin(country)]
# covid = covid[covid['Date'] == date]

fig2 = px.bar(covid, x='Country', y='Confirmed', color='Country',
              range_y=[0, 35000], animation_frame='Date', animation_group='Country')

# changing the animation speed
fig2.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 100
fig2.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 80

fig2.update_layout(width=800)
st.write(fig2)