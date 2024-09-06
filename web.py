import streamlit as st
import functions
todos = functions.get_todos()

def add_todo():
    todo = st.session_state['newtodo']+'\n'
    todos.append(todo)
    functions.writeTodos(todos)

st.title("To-do List")
st.write('This app is to increase your productivity')
try:
    for index,todo in enumerate(todos):
        checkbox=st.checkbox(todo,key=todo)
        if checkbox:
            todos.pop(index)
            functions.writeTodos(todos)
            del st.session_state[todo]
            st.rerun()
except:

    pass



st.text_input(label='',placeholder='Enter a todo...',on_change=add_todo,key='newtodo')