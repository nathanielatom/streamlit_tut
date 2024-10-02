import streamlit as st

st.header("Streamlit Tutorial")

import streamlit as st
from bokeh.plotting import figure
import pandas as pd
import numpy as np

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(title="simple line example", x_axis_label="x", y_axis_label="y")
p.line(x, y, legend_label="Trend", line_width=2)

st.bokeh_chart(p, use_container_width=True)

df = pd.DataFrame({'a': [1, 1, 2, 3, 5, 8, 13] * 10,
                   'b': [1, 2, 3, 5, 7, 11, 13] * 10})

st.write(df.style.highlight_min(axis=0))

x = st.slider('Val', min_value=0, max_value=37)
st.write(f"The value of x is {x}, and x^2 is {x**2}") 

choice = st.selectbox('Which?', ('a', 'b'))

p = figure(title="simple line example", x_axis_label="x", y_axis_label="y")
p.line(np.arange(7 * 10), df[choice], legend_label="Trend", line_width=2)
st.bokeh_chart(p, use_container_width=True)

