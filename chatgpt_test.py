import random

import streamlit as st
from streamlit_chat import message
import openai

import sidebarInit

# api_keys = st.secrets["API_KEYS"]
api_keys = [
    "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",
    "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",
    "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",
    "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",
    "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"]
openai.api_key = api_keys[random.randint(0, 4)]
# openAI code
# init_prompt = "Next you will become my AI assistant, and the conversation between me and you will take place in the form below. Here's an example. \
#                 Human: Hello, who are you? \
#                 AI: I am an AI created by OpenAI. How can I help you today? \
#                 If you already understand, please reply me OK."


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
            # stop=[" Human:", " AI:"]
        )

        answer = response["choices"][0]["text"].strip()
        return answer
    except Exception as exc:
        # print(exc)
        return "broken"


text_input = {"English": "Input (Clear chat context by inputting clear)",
              "中文": "输入后按回车键发送消息(清空上下文请输入clear)"}

# Streamlit App
st.set_page_config(
    # ChatDaVinci -- Chatgpt's Sister
    page_title="ChatDaVinci -- Chatgpt's Sister",
    page_icon=":robot:"
)

st.header("ChatDaVinci -- Another ChatGPT")
# st.subheader("ChatGPT is a GPT-3 powered chatbot that can talk about anything. It is created by OpenAI.")

language = st.radio('选择语言  Choose language:', ['中文', 'English'], horizontal=True)
sidebarInit.sidebarInit(language)

# st.header("ChatGPT Clone with Streamlit")
# st.subheader("ChatGPT is a GPT-3 powered chatbot that can talk about anything. It is created by OpenAI.")
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
    input_text = st.text_input(text_input[language], key="input")
    return input_text


# init_result = openai_create(init_prompt)
# print(init_result)
# st.session_state.turns += [init_prompt] + [init_result]
# st.session_state.text = " ".join(st.session_state.turns)
# print(st.session_state.turns)

question = get_text()
if question:
    if question == "clear":
        st.session_state.generated = []
        st.session_state.past = []
        st.session_state.text = ""
        st.session_state.turns = []
    else:
        st.session_state.past.append(question)
        prompt = st.session_state.text + " Human: " + question
        print(prompt)
        result = openai_create(prompt)
        print(result)
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
            st.session_state.turns += ["Human: " + question] + [result]
            print(st.session_state.turns)
        if len(st.session_state.turns) <= 10:
            st.session_state.text = " ".join(st.session_state.turns)
            print(st.session_state.turns)
        else:
            st.session_state.text = " ".join(st.session_state.turns[-10:])

# st.session_state.generated.append("Hello, I am ChatDaVinci, a GPT-3 powered chatbot that can talk about anything. It is created by OpenAI.")
# if len(st.session_state.generated) == 1:
#     message(st.session_state["generated"][0], key="init")

if st.session_state['generated'] and st.session_state['past']:
    # message(st.session_state["generated"][0], key="init")
    for i in range(len(st.session_state['past']) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i],
                is_user=True, key=str(i) + '_user')
