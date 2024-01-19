import streamlit as st
import random

l = ['TriageAtDawn', 'SilverDragon', 'SOMA', 'LDawly', '3m 3ly']

text = st.text_input('Enter your name or just press on the button')
if ((text or text != '')):
  if (text.lower() not in map(str.lower, l)):
    st.write("name entered successfully")
    l.append(text)
  else:
    st.write("name found before")

if st.button("I feel lucky"):
  st.markdown(f"{l[random.randint(0, len(l)-1)]} is {random.randint(0, 100)}% NOOB")