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
            max_tokens=2000,
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

text_input = {"English" : "Input (Clear chat context by inputting clear)", "中文" : "输入后按回车键发送消息(清空上下文请输入clear)"}

# Streamlit App
st.set_page_config(
    # ChatDaVinci -- Chatgpt's Sister
    page_title="ChatDaVinci -- Chatgpt's Sister",
    page_icon=":robot:"
)

st.header("ChatDaVinci -- Another ChatGPT")

language = st.radio('选择语言  Choose language:', ['中文','English'], horizontal=True)

if language == "English":
    st.sidebar.info(
        "Here are some prompts on what role you want the AI assistant to be."
    )

    add_selectbox = st.sidebar.selectbox(
        "What kind of assistant do you want?",
        ("Resume", "Copywriting", "Role Playing", "Programming", "Useful Prompts", "Daily Life", "Marketing", "Writing", "Learning New Things", "Language Learning")
    )

    if add_selectbox == "Resume":
        with st.sidebar:
            with st.expander("**Ask for Resume Feedback**"):
                st.write(
                    "What can I do to make this `position` resume better? Please provide specific suggestions and rewrite the experience with your suggestions. Please keep the format. `Attach the resume`")
            with st.expander("**Add Quantitative Data to Resume**"):
                st.write(
                    "Add quantitative data to the following resume. `Attach the resume`")
            with st.expander("**Make Resume More Concise**"):
                st.write(
                    "Make the following resume more concise without sacrificing the quality.  `Attach the resume`")
            with st.expander("**Customize Resume**"):
                st.write(
                    "I am applying for `position and company`, rewrite the following experience, so that I can better fit `company name`'s corporate culture. `Attach the experience`")
    elif add_selectbox == "Copywriting":
        with st.sidebar:
            with st.expander("**Social Media Copywriting**"):
                st.write(
                    "Create a compelling, eye-catching `social media` post for `purpose`. The post should include `keyword 1`, `keyword 2`, and `keyword 3`. Also, it should follow these rules: `rule 1`, `rule 2`, `rule 3`, and `rule 4`.")
            with st.expander("**Write a Product Review**"):
                st.write(
                    "Write a product review for the following product. `Attach the product`")
            with st.expander("**Write a Product Introduction**"):
                st.write(
                    "Write a product introduction for the following product. `Attach the product`")
            with st.expander("**Write a Product Feature**"):
                st.write(
                    "Write a product feature for the following product. `Attach the product`")
            with st.expander("**Write a Product Description**"):
                st.write(
                    "Write a product description for the following product. `Attach the product`")
            with st.expander("**Write a Product Description**"):
                st.write(
                    "Write a product description for the following product. `Attach the product`")

        # todo: add more copywriting prompts
elif language == "中文":
    st.sidebar.info(
        "这里有一些提示，告诉你AI助手的角色是什么。"
    )

    add_selectbox = st.sidebar.selectbox(
        "你想要什么种类的助手？",
        ("写报告", "资料整理", "履历与自传", "编程", "知识学习", "英语学习", "工作生产力", "写作帮手", "日常生活", "有趣好玩", "角色扮演")
    )

    if add_selectbox == "写报告":
        with st.sidebar:
            with st.expander("**报告开头**"):
                st.write(
                    "我现在正在`报告的情境与目的`。我的简报主题是`主题`，请提供`数字`种开头方式，要简单到`目标族群`能听懂，同时要足够能吸引人，让他们愿意专心听下去")
                st.write("例如：我现在正在修中南大学的简报课，其中一项作业是要做一份让小学生能听懂的简报。我的简报主题是机会成本，请提供三种开头方式，要简单到小学生能听懂，同时要足够能吸引人，让他们愿意专心听下去")
            with st.expander("**研究报告**"):
                st.write(
                    "写出一篇有关`知识`的`数字`字研究报告，报告中需引述最新的研究，并引用专家观点")
                st.write("例如：写出一篇有关`自动驾驶`的`300`字研究报告，报告中需引述最新的研究，并引用专家观点")
            with st.expander("**提出反对观点**"):
                st.write(
                    "你是`某个主题`的专家，请针对以下论述`附上论述`，提出`数字`个反驳的论点，每个论点都要有佐证")
                st.write(
                    "例如：你是大数据分析的专家，请针对以下论述「在数据分析中，越多数据越好」，提出 3 个反驳的论点，每个论点都要有佐证")
            with st.expander("**报告总结**"):
                st.write(
                    "你是`某个主题`的专家，请总结以下内容，并针对以下内容提出未来能进一步研究的方向`附上内容`")
                st.write(
                    "例如：你是金融科技专家，请总结以下内容，并针对以下内容提出未来能进一步研究的方向 [附上内容]")
    elif add_selectbox == "资料整理":
        with st.sidebar:
            with st.expander("**搜集资料**"):
                st.write(
                    "给我`数字`篇，有关`领域`的文章")
                st.write(
                    "例如：给我 5 篇，有关 SEO 的文章。")
            with st.expander("**内容总结**"):
                st.write(
                    "用列点的方式总结出这篇文章的`数字`个重点：`附上文章内容/附上文章网址`。")
                st.write(
                    "例如：用列点的方式总结出这篇文章的 5 个重点：[附上文章内容/附上文章网址]。")
            with st.expander("**摘录某领域重点**"):
                st.write(
                    "用列点的方式总结出`数字`个`领域`知识重点")
                st.write(
                    "例如：用列点的方式总结出 10 个量子力学知识重点。")

            # todo: add more prompts



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
