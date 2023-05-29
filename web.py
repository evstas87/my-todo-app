import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    local_todo = st.session_state["new_todo"]
    todos.append(local_todo + '\n')
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.text("This app is to increase your productivity.")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

# for todo in todos:
#     st.checkbox(todo)

st.text_input(label="Enter a todo", placeholder="Add new todo",
              on_change=add_todo, key="new_todo")
# st.session_state