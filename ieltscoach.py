import streamlit as st
import openai
import random

# Step 1: Obtain OpenAI API key
api_keys = st.secrets["API_KEYS"]
user_keys = st.secrets["USER_KEYS"]
openai.api_key = api_keys[random.randint(0, 4)]


def generate_result(prompt, model, temperature, max_tokens):
    completions = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        # top_p=1,
        # frequency_penalty=0,
        # presence_penalty=0
    )
    message = completions.choices[0].text
    return message


def main():
    st.set_page_config(page_title="GPT 雅思教练 OpenAI GPT IELTS Essay Coach", page_icon=":guardsman:", layout="wide")
    st.title("GPT 雅思教练\nOpenAI GPT IELTS Essay Coach")
    st.markdown(
        "使用OpenAI GPT为你的雅思作文评分并给出修改建议\n\n OpenAI GPT scores your IELTS essay and gives suggestions for revision")

    # Get user input
    user_key = st.text_input("输入激活码 Input your activation code")
    question = st.text_area("输入作文题目 Your Essay Question:")
    essay = st.text_area("输入你的作文 Your Essay:")
    prompt = (f"Now you are an IELTS essay coach. Please evaluate my essay \
        according to the grading requirements of IELTS essay, give my essay \
        score, and correct my mistakes and give specific suggestions for improvement. \
        If the input is too short, not like an article, give me 0 point. \
        Finally, please give me a whole polished article. \
        Give detailed scoring reasons and improvement suggestions as far as possible.\
        Please list your suggestions in sections, at least three and at most ten. \
        Please answer me in chinese and use English if necessary. \n \
        The format of your output is: \n \
        [作文得分]: write score here and a linefeed\n  \
        [改进建议]: \n \
        [润色后]: \n \
        The question of the essay is:\n{question}\n \
        My essay is:\n{essay}\n")

    model = "text-davinci-003"
    # 随机值越高则GPT越有可能探索新的可能性（即，生成更多可能的结果），而不是仅局限于已知的结果。
    # 如果设置的随机值太低，GPT就可能会陷入安全区域中，导致它会生成大量相似的结果。
    temperature = st.slider("选择教练醉酒程度 Choose Degree of intoxication:", 0.0, 1.0, 0.5)
    st.text("模拟真人环境，分数和建议会有一定随机性。醉酒程度低的教练回答风格稳健，反之更具有创造性和随机性。")
    st.text(
        "Simulate the real environment, and the scores and suggestions will have some randomness. Coaches with low "
        "degree of drunkenness have a stable response style, and on the contrary, they are more creative and random.")
    # temperature = 0.1
    max_tokens = 3000

    if st.button("确认/Submit"):
        if user_key in user_keys:
            with st.spinner('教练阅读中... \t In progress...'):
                result = generate_result(prompt, model, temperature, max_tokens)
                st.success("大功告成！\n Success!")
                st.balloons()
                st.text(result)
                st.markdown("**点击以下按钮下载教练反馈 Click the Button to Download**")

            st.download_button(
                label="下载记录 Download",
                data=result,
                file_name='result.txt',
            )
        else:
            st.error("请输入有效的激活码")


if __name__ == "__main__":
    main()
