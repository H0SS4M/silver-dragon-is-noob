import streamlit as st
import random

l = ['TriageAtDawn', 'SilverDragon', 'SOMA', 'LDawly', '3m 3ly']

text = st.text_input('Enter your name')
if ((text or text != '') and text.lower() not in map(str.lower, l)):
  l.append(text)

if st.button("I feel lucky", type="primary"):
  st.markdown(f"{l[random.randint(0, len(l)-1)]} is {random.randint(0, 100)}% NOOB")