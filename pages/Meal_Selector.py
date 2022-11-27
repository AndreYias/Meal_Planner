import streamlit as st
import random as rand

meals = ["","Cottage pie","Lasagna","Fajitas","Burrito","Indian Curry","Thai Curry","Katsu Curry","Greek Spag","Faghi","Spinach and Brocolli", "Sausage Ragu","Salmon Pasta","Lasagna","Pesto pasta","Tomato Mozarella pasta","Roast Dinner","Stuffed Peppers","Baked Tofu w/Rice","Sechuan Noodles","Cuban Black Beans","Vegi Chilli"]
past_meals = []
meal_plan = []
form_submit = False

def pick_random_meals(meals):
    if not len(past_meals) == 0:
        new_meals = list(set(meals) - set(past_meals[-1]))
    else:
        new_meals = meals
    meal_plan = rand.sample(new_meals,k=7)
    past_meals.append(meal_plan)
    return meal_plan

# The streamlit elements

st.title("Meal Planner")

st.text("Untick the days you don't want to plan")

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    Monday = st.checkbox("Monday", value = True)
with col2: 
    Tuesday = st.checkbox("Tuesday", value = True) 
with col3:
    Wednesday = st.checkbox("Wednesday", value = True) 
with col4:
    Thursday = st.checkbox("Thursday", value = True)
with col5: 
    Friday = st.checkbox("Friday", value = True) 

col6,col7,col8,col9,col10 = st.columns(5)
with col6:
    Saturday = st.checkbox("Saturday", value = True) 
with col7:
    Sunday = st.checkbox("Sunday", value = True)

if st.button("Choose your meals"):
    meal_plan = ["","","","","","",""]

if st.button("Randomise"):
    meal_plan = pick_random_meals(meals[1:])  

if not len(meal_plan) == 0: 
    with st.form("final_choices"):
        st.date_input("What is the date?")
        st.subheader("Your meals this week")

        if Monday is True:
            Monday_Choice = st.selectbox("Monday Meal", options = meals, index = meals.index(meal_plan[0]))
        if Tuesday is True:
            Tuesday_Choice = st.selectbox("Tuesday Meal", options = meals, index = meals.index(meal_plan[1]))
        if Wednesday is True:
            Wednesday_Choice = st.selectbox("Wednesday Meal", options = meals, index = meals.index(meal_plan[2]))
        if Thursday is True:
            Thursday_Choice = st.selectbox("Thursday Meal", options = meals, index = meals.index(meal_plan[3]))
        if Friday is True:
            Friday_Choice = st.selectbox("Friday Meal", options = meals, index = meals.index(meal_plan[4]))
        if Saturday is True:
            Saturday_Choice = st.selectbox("Saturday Meal", options = meals, index = meals.index(meal_plan[5]))
        if Sunday is True:
            Sunday_Choice = st.selectbox("Sunday Meal", options = meals, index = meals.index(meal_plan[6]))

        form_submit = st.form_submit_button(on_click=st.balloons,help="This will confirm your meal choices")

if form_submit:
    st.write("aaaa")











