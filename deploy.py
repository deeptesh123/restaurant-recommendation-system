import streamlit as st
import pandas as pd
import pickle
import random
st.image("./images/Restaurant.jpg")
if "recommendations" not in st.session_state:
    st.session_state.recommendations=pickle.load(open("recommendation.pkl","rb"))
if "options" not in st.session_state:
    st.session_state.options=[x for x in st.session_state.recommendations]
images=[f"./images/i{i}.jpg" for i in range(1,16)]
popular=pd.read_csv("popular.csv")
flag=True
with st.sidebar:
    st.title("**Select type of recommendation system:**")
    ch=st.radio(" ",["popularity based","content based"])
    for i in range(8): st.text("")
    if ch=="content based": flag=False
    st.title('**Select a restaurant**')
    name=st.selectbox(" ",st.session_state.options,disabled=flag)
    rec=st.button("Recommend")
if rec:
    if not flag:
        # st.write("contentttttttttt")
        st.header(f'Top 10 restaurants similar to "{name}" are: ')
        df=st.session_state.recommendations[name]
        col1,col2=st.columns([1,1])
        im=random.sample(range(1,16),k=10)
        for i in range(10):
            if i%2==0: col=col1
            else: col=col2
            with col:
                st.subheader("")
                st.image(f"./images/i{im[i]}.jpg")
                st.subheader(df.iloc[i]["name"])
                st.subheader(str(df.iloc[i]["Mean Rating"])+" "+":star2:")
                st.text("cusines served: "+df.iloc[i]["cuisines"])
                st.text("cost for two: "+str(df.iloc[i]["cost"]))
                st.text("")
    else:
        st.header("Top 10 most popular resarants are: ")
        col1,col2=st.columns([1,1])
        im=random.sample(range(1,16),k=10)
        for i in range(10):
            if i%2==0: col=col1
            else: col=col2
            with col:
                st.text("")
                st.image(f"./images/i{im[i]}.jpg")
                st.subheader(popular.iloc[i]["name"])
                rating=popular.iloc[i]["rate"]
                st.subheader(str(rating)+" "+":star2:")
                st.text("cusines served: "+popular.iloc[i]["cuisines"])
                st.text("cost for two: "+str(popular.iloc[i]["cost"]))
                st.text("")