import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

st.title("Testing all Elements learned")

st.header("1. Text Elements")
st.title("Title")
st.header("Header")
st.subheader("Sub-Header")
st.write("Text")
st.markdown("_Markdown_")
st.caption("caption")
st.divider()

st.header("2. Button Element")
but = st.button("Button") #everytime something happen like clicking a button, streamlit rerun entirely

st.write("Rendering Code")
st.code("print(Hello world)", language="python")

st.image("Picture1.png")

st.header("3. Data Elements")
df = pd.DataFrame({
    "Name" : ["Nagomi", "Maha", "Namitha"],
    "Age" : [21, 22, 21]
})

st.dataframe(df) #dataframe
st.data_editor(df) #editable dataframe
st.table(df) #Static table
st.metric(label = "Total Rows", value = len(df)) #metric
st.json({
    "Name" : ["Nagomi", "Maha", "Namitha"],
    "Age" : [21, 22, 21]
})

st.header("4. Charts")
dt=pd.DataFrame(np.random.randn(20, 3), 
    columns = ["A", "B", "C"])

st.area_chart(dt)
st.line_chart(dt)
st.bar_chart(dt)

sc=pd.DataFrame({"x" : np.random.randn(100), 
    "y" : np.random.randn(100)})
st.scatter_chart(sc)

st.header("5. Form Elements")

with st.form(key="my_form"):
    st.subheader("Interactive Elements goes here..")

    #Text inputs
    name = st.text_input("Enter your Name")
    des = st.text_area("Description")
    sal = st.number_input("Enter your Salary")

    #Date elements
    mi = datetime(1990, 1, 1)
    ma = datetime.now()
    dob = st.date_input("Enter your DOB", min_value=mi, max_value=ma)

    if dob:
        age = ma.year - dob.year
        if dob.month > ma.month or (dob.month == ma.month and dob.day > ma.day):
            age-=1
        st.write("Your Age is", age)
    time = st.time_input("Enter the your flexible time")

    #Selectors
    ch = st.radio("Profession", ["IT", "Student", "Others"]) 
    op = st.selectbox("Why here?", ["Study", "Work", "Chilling", "Bored", "Upskilling"]) #dropdown checkbox
    sl = st.select_slider("Rating", [1,2,3,4, 5])

    #toggles and checkbox
    nt = st.checkbox("Receive Notification?")
    tg = st.checkbox("Dark Mode", value = False)

    bt = st.form_submit_button("Submit")

    fields = [name, des, dob, time, ch, op, sl, nt, tg, age]
    if bt:
        if not all(fields):
            st.warning("Please enter all fields")
        else:
            st.balloons()
            st.success("Good to go")
            st.write("### Your Details")
            for i in fields:
                st.write(i)
            


if st.button("Click me"):
    st.write(f'hello {name}')
    st.write(f'your description {des}')
    st.write(f'your dob {dob}')
    st.write(f'your flexible time {time}')
    st.write(f'your have chosen {ch}')
    st.write(f'your have chosen {op}')
    st.write(f'your have chosen {sl}')
    st.write(f'your have chosen {nt}')
    st.write(f'your have chosen {tg}')

#Session State
st.header("6. Session State")
if 'counter' not in st.session_state:
    st.session_state.counter = 0

if st.button("Increement"):
    st.session_state.counter +=1
    st.write("Increemented to:",st.session_state.counter)

st.write(st.session_state.counter)


st.header("7. Layout")
tab1, tab2, tab3 = st.tabs(["Tab 1","Tab 2","Tab 3"]) 

with tab1:
    st.write("Hi")

with tab2:
    st.write("You Still Here")

with tab3:
    st.write("You have to leave now bye :(")

col1, col2 = st.columns(2) 
with col1:
    st.write("I am Left")

with col2:
    st.write("I am Right")

st.header("8. Container")
with st.container(border=True):
    st.write("I am inside a container")
    st.write("I am hiding")
    st.write("You cant see me")
    st.write("I am Invisible")

st.hader("9. Sidebar")

name = st.sidebar.text_input("Enter your name")
age = st.sidebar.number_input("Enter your age", min_value=1, max_value=100)
gender = st.sidebar.selectbox("Select your gender", ["Male", "Female", "Other"])

if st.sidebar.button("Submit"):
    st.write(f"Hello {name}, you are {age} years old and identify as {gender}.")


#Duplicate Widget Id Issue - use key
st.header("10. Duplicate Buttons with different Keys")
st.button("Fill")
st.button("Fill", key = "bt2")

#Empty Placeholder - lets you change inline text
st.header("Other")
ph = st.empty()
ph.write("I am good girl!")

if st.button("Really?"):
    ph.write("No, I am EVILLLLLL!")

#Expander
with st.expander("for more details"):
    st.write("Author: Nagomi")
    st.write("Year: 2025")

#Tooltip
st.button("Hover", help="This explains why, Dumbass")

# [theme]
# primaryColor = "#4CAF50"
# backgroundColor = "#F5F5F5"
# textColor = "#000000"
