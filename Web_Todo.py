import streamlit as st
import Functions

def add_task():
    new_task =st.session_state["new_todo"] + "\n"
    st.write(new_task)
    todos.append(new_task)
    Functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my Todo app.")
st.write("This app is to increase your productivity.")

todos = Functions.get_todos()
for index, todo in enumerate(todos):
    cb = st.checkbox(todo, key=todo)
    if cb:
        todos.pop(index)
        Functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add a new Task", key="new_todo", on_change=add_task)
st.session_state
