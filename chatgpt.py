import random

import streamlit as st
from streamlit_chat import message
import openai

api_keys = st.secrets["API_KEYS"]
openai.api_key = api_keys[random.randint(0, 4)]
# openAI code
# init_prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n \
# Human: Hello, who are you?\n \
# AI: I am an AI created by OpenAI. How can I help you today?\n"


def openai_create(prompt):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.9,
            max_tokens=2500,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        )

        answer = response["choices"][0]["text"].strip()
        return answer
    except Exception as exc:
        # print(exc)
        return "broken"


# Streamlit App
st.set_page_config(
    page_title="Streamlit Chat - Demo",
    page_icon=":robot:"
)

st.header("ChatGPT Clone with Streamlit")

# history_input = []
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

if 'turns' not in st.session_state:
    st.session_state['turns'] = []

if 'text' not in st.session_state:
    st.session_state['text'] = ""


def get_text():
    input_text = st.text_input("You:(Starting next conversation by inputting clear)", key="input")
    return input_text


question = get_text()
if question:
    if question == "clear":
        st.session_state.generated = []
        st.session_state.past = []
        st.session_state.text = ""
        st.session_state.turns = []
    else:
        st.session_state.past.append(question)
        prompt = st.session_state.text + "\nHuman: " + question
        print(prompt)
        result = openai_create(prompt)
        # print(result)
        if result.find(':'):
            index = result.find(':') + 1
        else:
            index = 0
        st.session_state.generated.append(result[index:])
        while result == "broken":
            result = openai_create(prompt)
            if result.find(':'):
                index = result.find(':') + 1
            else:
                index = 0
            st.session_state.generated.append(result[index:])
        else:
            st.session_state.turns += [question] + [result]
            print(st.session_state.turns)
        if len(st.session_state.turns) <= 10:
            st.session_state.text = " ".join(st.session_state.turns)
            print(st.session_state.turns)
        else:
            st.session_state.text = " ".join(st.session_state.turns[-10:])

if st.session_state['generated']:

    for i in range(len(st.session_state['generated']) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        # if st.session_state["generated"][i][1] != '':
        # print(st.session_state["generated"][i][0][1])
        message(st.session_state['past'][i],
                is_user=True, key=str(i) + '_user')
