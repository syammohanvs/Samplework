import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns   


# Set the title of the Streamlit app
st.title("Auto EDA with Streamlit")
st.header("Explore your dataset with ease!")
st.subheader("Upload your CSV file below:")
st.markdown("This app uses various libraries for *automated Exploratory* **Data Analysis** (EDA).")
st.code("""
import pandas as pd
""",language='python')

st.text("Upload your CSV file to get started.")
st.subheader("JSon and Dictionary")
my_dict = {
    "Name": "John Doe",
    "Age": 30,
    "Occupation": "Data Scientist"
}
st.write("JSon View:")
st.json(my_dict)

st.write("Dictionary View:", my_dict) # Treats python dict as json

st.subheader("Editable DataFrame")
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Occupation": ["Engineer", "Doctor", "Artist"]
})

editable_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)
st.write("Edited Data:")
st.dataframe(editable_df)

# Static Table
st.subheader("Static Tables")
st.table(editable_df)

# Charts Section
st.subheader("Charts")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)


st.subheader("Area Chart")
st.area_chart(chart_data)

st.subheader("Bar Chart")
st.bar_chart(chart_data)

st.subheader("Line Chart")
st.line_chart(chart_data)

st.subheader("Scatter Plot")
scatter_data = pd.DataFrame({
    'x': np.random.rand(100),
    'y': np.random.rand(100)
})
st.write("Scatter Plot Data:")
st.scatter_chart(scatter_data)

st.subheader("Map")
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(map_data)

#PyPlot and Seaborn Charts
st.subheader("Matplotlib and Seaborn Charts")
fig, ax = plt.subplots()
ax.plot(chart_data['A'], label='A')
ax.plot(chart_data['B'], label='B')
ax.plot(chart_data['C'], label='C')
ax.set_title('Line Chart using Matplotlib')
ax.legend()
st.pyplot(fig)