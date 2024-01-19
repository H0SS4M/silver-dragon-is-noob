import streamlit as st
import random

l = ['TriageAtDawn', 'SilverDragon', 'SOMA', 'LDawly', '3m 3ly']

if st.button("Reset", type="primary"):
  st.markdown(f"{l[random.randint(0, len(l)-1)]} is {random.randint(0, 100)}% NOOB")