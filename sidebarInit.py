import streamlit as st

def sidebarInit(language):
    if language == "English":
        st.sidebar.info(
            "Here are some prompts on what role you want the AI assistant to be."
        )

        add_selectbox = st.sidebar.selectbox(
            "What kind of assistant do you want?",
            ("Resume", "Copywriting", "Role Playing", "Programming", "Useful Prompts", "Daily Life", "Marketing",
             "Writing", "Learning New Things", "Language Learning")
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


    elif language == "中文":
        st.sidebar.info(
            "这里有一些提示，告诉你AI助手的角色是什么。"
        )

        add_selectbox = st.sidebar.selectbox(
            "你想要什么种类的助手？",
            ("写报告", "资料整理", "履历与自传", "编程", "知识学习", "英语学习", "工作生产力", "写作帮手", "日常生活",
             "有趣好玩", "角色扮演")
        )

        if add_selectbox == "写报告":
            with st.sidebar:
                with st.expander("**报告开头**"):
                    st.write(
                        "我现在正在`报告的情境与目的`。我的简报主题是`主题`，请提供`数字`种开头方式，要简单到`目标族群`能听懂，同时要足够能吸引人，让他们愿意专心听下去")
                    st.write(
                        "例如：我现在正在修中南大学的简报课，其中一项作业是要做一份让小学生能听懂的简报。我的简报主题是机会成本，请提供三种开头方式，要简单到小学生能听懂，同时要足够能吸引人，让他们愿意专心听下去")
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
        elif add_selectbox == "履历与自传":
            with st.sidebar:
                with st.expander("**寻求履历的反馈**"):
                    st.write(
                        "这份`职位`的履历，有哪边可以写更好? 请以专业面试官的角度，提出具体改进建议。接着以你提出的建议来改写这段经历，改写时请维持列点的形式。`附上履历`")
                    st.write(
                        "例如：这份 UIUX 设计师的履历，有哪边可以写更好? 请以专业面试官的角度，提出具体改进建议。接着以你提出的建议来改写这段经历，改写时请维持列点的形式。")
                with st.expander("**为履历加上量化数据**"):
                    st.write(
                        "改写以下履历，为每一点加上量化的数据，改写时请维持列点的形式。`附上履历`")
                with st.expander("**把经历修精简**"):
                    st.write(
                        "把这段经历写得更精简一点，让别人可以马上看到重点，同时维持生动的描述。`附上经历`")
                with st.expander("**为不同公司客制化撰写履历**"):
                    st.write(
                        "我今天要申请`公司`的`职位`，改写以下经历，让我能更符合`公司`的企业文化。`附上经历`")
                    st.write(
                        "例如：我今天要申请 Google 的前端工程师，改写以下经历，让我能更符合 Google 的企业文化。[附上经历]")
        elif add_selectbox == "准备面试":
            with st.sidebar:
                with st.expander("**汇整面试题目**"):
                    st.write(
                        "你现在是`公司`的`职位`面试官，请分享在`职位`面试时最常会问的`数字`个问题。")
                    st.write(
                        "例如：你现在是 Google 的产品经理面试官，请分享在 Google 产品经理面试时最常会问的 5 个问题。")
                with st.expander("**给予回馈**"):
                    st.write(
                        "我针对`问题`的回答，有哪些可以改进的地方?`附上回答`")
                    st.write(
                        "例如：我针对「你会如何排定不同产品功能优先顺序?」的回答，有哪些可以改进的地方? [附上回答]")
                with st.expander("**提供追问的问题**"):
                    st.write(
                        "针对`问题`这个面试问题，请提供一些常见的追问面试题。")
                    st.write(
                        "例如：针对「你会如何排定不同产品功能优先顺序?」这个面试问题，请提供一些常见的追问面试题。")
                with st.expander("**用 STAR 原则回答面试问题**"):
                    st.write(
                        "我在准备`问题`这个面试问题，请用 STAR 原则帮我回答这个问题。针对这个问题，我有的经历如下`附上经历`。")
                    st.write(
                        "例如：我在准备「请分享一个你在急迫的期限中完成专案的经验」这个面试问题，请用 STAR 原则帮我回答这个问题。针对这个问题，我有的经历如下 [附上经历]。")
        elif add_selectbox == "编程":
            with st.sidebar:
                with st.expander("**写程式**"):
                    st.write(
                        "你现在是一个`程式语言`专家，请帮我用`程式语言`写一个函式，它需要做到`某个功能`")
                    st.write(
                        "例如：你现在是一个 JavaScript 专家，请帮我用 JavaScript 写一个函式，它需要做到 输入一个一维阵列，把这个一维阵列转换成二维阵列。同时我要能够自由地决定二维阵列中的子阵列长度是多少")
                with st.expander("**解读代码**"):
                    st.write(
                        "你现在是一个`程式语言`专家，请告诉我以下的程式码在做什么。`附上程式码`")
                    # st.write(
                    #     "例如：我针对「你会如何排定不同产品功能优先顺序?」的回答，有哪些可以改进的地方? [附上回答]")
                with st.expander("**重构代码**"):
                    st.write(
                        "你现在是一个 Clean Code 专家，我有以下的程式码，请用更干净简洁的方式改写，让我的同事们可以更容易维护程式码。另外，也解释为什么你要这样重构，让我能把重构的方式的说明加到 Pull Request 当中。`附上程式码`")
                    # st.write(
                    #     "例如：针对「你会如何排定不同产品功能优先顺序?」这个面试问题，请提供一些常见的追问面试题。")
                with st.expander("**解 bug**"):
                    st.write(
                        "你现在是一个`程式语言`专家，我有一段程式码，我预期这段程式码可以`做到某个功能`，只是它通过不了 `测试案例`这个测试案例。请帮我找出我哪里写错了，以及用正确的方式改写。`附上程式码`")
                    st.write(
                        "例如：你现在是一个 python 专家，我有一段程式码，我预期这段程式码可以判断一个字串是不是镜像回文，只是它通过不了 aacdeedcc 这个测试案例。请帮我找出我哪里写错了，以及用正确的方式改写。[附上程式码]")
                with st.expander("**写测试**"):
                    st.write(
                        "你现在是一个`程式语言`专家，我有一段程式码`附上程式码`，请帮我写一个测试，请至少提供五个测试案例，同时要包含到极端的状况，让我能够确定这段程式码的输出是正确的。")
                    # st.write(
                    #     "例如：你现在是一个 python 专家，我有一段程式码，我预期这段程式码可以判断一个字串是不是镜像回文，只是它通过不了 aacdeedcc 这个测试案例。请帮我找出我哪里写错了，以及用正确的方式改写。[附上程式码]")
                with st.expander("**写 Regex**"):
                    st.write(
                        "你现在是一个 Regex 专家，请帮我写一个 Regex ，它能够把`需求`")
                    st.write(
                        "例如：你现在是一个 Regex 专家，请帮我写一个 Regex ，它能够把输入一个字串，把这个字串中的所有数字都取出。")
