import streamlit as st
import foodfunction
import os

meals = foodfunction.get_meals()


def add_meal():
    meal = st.session_state['new_meal'] + "\n"
    meals.append(meal)
    foodfunction.write_meals(meals)


if not os.path.exists('meals.txt'):
    with open('meals.txt', 'w') as file:
        pass

st.title('My meal planner')
st.subheader('This is my meal planner app')
st.write('This app is to help to plan my meals')

for index, meal in enumerate(meals):
    checkbox = st.checkbox(meal, key=meal)
    if checkbox:
        meals.pop(index)
        foodfunction.write_meals(meals)
        del st.session_state[meal]
        st.rerun()

st.text_input(label='New meal', placeholder='Enter your meal here...',
              on_change=add_meal, key='new_meal')
