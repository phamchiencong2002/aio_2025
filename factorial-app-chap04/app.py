import streamlit as st
from factorial import fact
import os

def load_users():
    try:
        if os.path.exists("users.txt"):
            with open("users.txt", "r", encoding="utf-8") as f:
                users = [line.strip() for line in f.readlines() if line.strip()]
                return users
        else:
            st.error("File user.txt not found.")
            return []
    except Exception as e:
        st.error(f"Error loading users: {e}")
        return []    

def login_page():
    st.title("Login")
    username = st.text_input("Username:")
    if st.button("Login"):
        if username:
            users = load_users()
            if username in users:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()
            else:
                st.session_state.show_greeting = True
                st.session_state.username = username
                st.rerun()
        else:
            st.warning("Please enter a username.")

def factorial_calculator():
    st.title("Factorial Calculator")
    st.write(f"Welcome, {st.session_state.username}!")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()
    
    st.divider()

    number = st.number_input("Input a number:", min_value=0, max_value=900)
    if st.button("Calculate Factorial"):
        result = fact(number)
        st.write(f"Factorial of {number} is {result}.")

def greeting_page():
    st.title("Welcome!")
    st.write(f"Hello, {st.session_state.username}!")
    st.write("It seems you are a new user. Please contact the administrator to get access.")
    if st.button("Back to Login"):
        st.session_state.show_greeting = False
        st.session_state.username = ""
        st.rerun()

def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'username' not in st.session_state:
        st.session_state.username = ""
    if 'show_greeting' not in st.session_state:
        st.session_state.show_greeting = False
    
    if st.session_state.logged_in:
        factorial_calculator()
    elif st.session_state.show_greeting:
        greeting_page()
    else:
        login_page()

if __name__ == "__main__":
    main()