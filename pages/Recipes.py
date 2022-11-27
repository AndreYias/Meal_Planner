import streamlit as st

st.text("Scroll to the right ->")
meals = ["","Cottage pie","Lasagna","Fajitas","Burrito","Indian Curry","Thai Curry","Katsu Curry","Greek Spag","Faghi","Spinach and Brocolli", "Sausage Ragu","Salmon Pasta","Lasagna","Pesto pasta","Tomato Mozarella pasta","Roast Dinner","Stuffed Peppers","Baked Tofu w/Rice","Sechuan Noodles","Cuban Black Beans","Vegi Chilli"]
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14, tab15, tab16, tab17, tab18, tab19, tab20, tab21 = st.tabs(meals[1:])