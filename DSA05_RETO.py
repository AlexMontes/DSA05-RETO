import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Link when using Colab and GDrive
#URL = ('/content/gdrive/MyDrive/Colab Notebooks/DSA05 - Aplicacion web en la Ciencia de Datos/Reto/Employees.csv')

# Link when using stremlit with github
URL = ('Employees.csv')

st.title('DSA05 - RETO')

@st.cache
def load_data(nrows):
    employees = pd.read_csv(URL, nrows = nrows)
    lowercase = lambda x: str(x).lower()
    return employees

@st.cache
def Emp_ID_filter(Emp_ID):
    Filtered_EmpID_data = employees[employees['Employee_ID'].str.upper().str.contains(Emp_ID)]
    return Filtered_EmpID_data

@st.cache
def Hometown_filter(Home):
    Filtered_Home_Data = employees[employees['Hometown'] == Home]
    return Filtered_Home_Data

@st.cache
def Unit_filter(Unit_data):
    Filtered_Unit_Data = employees[employees['Unit'] == Unit_data]
    return Filtered_Unit_Data

@st.cache
def Edu_Level_Filter(Edu):
    Filtered_Edu_Data = employees[employees['Education_Level'] == Edu]
    return Filtered_Edu_Data

loading_state = st.text('Loading cicle DSA05-RETO data...')
employees = load_data(500)
loading_state.text("Done! (using st.cache)")

# Side Bar

# Side Bar - Options 
st.sidebar.title('Options') 
st.sidebar.markdown("___")

# Side Bar - checkbox
if st.sidebar.checkbox('¿Show Data Frame?'):
    st.subheader('Data Frame overview employees')
    st.write(employees)

# Side Bar search Emp ID
if st.sidebar.checkbox('Search by ID'):
    ID = st.sidebar.text_input('Employee ID :')
    btnBuscar = st.sidebar.button('Buscar ID')

    if (btnBuscar):
       data_ID = Emp_ID_filter(ID.upper())
       count_row = data_ID.shape[0]  # Gives number of rows
       st.write(f"Total ID mostrados : {count_row}")
       st.write(data_ID)

# Side Bar search Hometown
if st.sidebar.checkbox('Search by Hometown'):
    selected = st.sidebar.selectbox('Select Hometown', employees['Hometown'].unique())
    btnHome = st.sidebar.button('Filter Hometown ')

    if (btnHome):
       Home_Filter = Hometown_filter(selected)
       count_row = Home_Filter.shape[0]  
       st.write(f"Total Home : {count_row}")
       st.dataframe(Home_Filter)

# Side Bar search Unit
if st.sidebar.checkbox('Search by Unit'):
    selected_Unit = st.sidebar.selectbox('Select Unit', employees['Unit'].unique())
    btnUnit = st.sidebar.button('Filter Unit ')

    if (btnUnit):
       Unit_Filter = Unit_filter(selected_Unit)
       count_row = Unit_Filter.shape[0] 
       st.write(f"Total Units : {count_row}")
       st.dataframe(Unit_Filter)

# Side Bar Select Box Education Level
Selected_Edu_Level = st.sidebar.selectbox('Select Education Level', employees['Education_Level'].unique())
btnEdu_Level = st.sidebar.button('Filter Level')

if(btnEdu_Level):
    Edu_Filter = Edu_Level_Filter(Selected_Edu_Level)
    count_row = Edu_Filter.shape[0]
    st.dataframe(Edu_Filter)

# Histogram of Age
st.header('Age Histogram')
Age_values = np.histogram(employees['Age'], bins = 10, range = (employees['Age'].min(), employees['Age'].max()))[0]
st.bar_chart(Age_values)
st.markdown("___")

# Histogram of Unit
st.header('Unit Histogram')
fig, ax1 = plt.subplots(figsize = (15, 5))
ax1.set_xlabel('Unit')
ax1.tick_params(axis = 'x', rotation = 45)
ax1.hist(employees['Unit'])
st.pyplot(fig)
st.markdown("___")

# Attrition Rate by Hometown
st.header('Attrition Rate by Hometown')
fig2, ax2 = plt.subplots(figsize = (15, 5))
ax2.set_xlabel('Hometown')
ax2.set_ylabel('Attrition rate', color = 'blue')
ax2.bar(employees['Hometown'], employees['Attrition_rate'])
st.pyplot(fig2)
st.markdown('___')

# Attrition Rate by Age
st.header('Attrition Rate by Age')
fig3, ax3 = plt.subplots(figsize = (15, 5))
ax3.set_xlabel('Age')
ax3.set_ylabel('Attrition rate', color = 'blue')
ax3.bar(employees['Age'], employees['Attrition_rate'])
st.pyplot(fig3)
st.markdown('___')

# Attrition Rate by Time of Service
st.header('Attrition Rate by Time of Service')
fig4, ax4 = plt.subplots(figsize = (15, 5))
ax4.set_xlabel('Time of Service')
ax4.set_ylabel('Attrition rate', color = 'blue')
ax4.bar(employees['Age'], employees['Attrition_rate'])
st.pyplot(fig4)
st.markdown('___')
