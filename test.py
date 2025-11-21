import streamlit as st
import os
from openai import OpenAI

# ---------------- 页面配置 ----------------
st.set_page_config(
    page_title="京剧关羽问答助手",
    page_icon="🎭",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------- 样式美化 ----------------
st.markdown("""
<style>
body {
    background-color: #fdf6e3; /* 宣纸米黄色背景 */
}
h1 {
    color: #b22222;
    font-family: "STKaiti", "KaiTi", serif;
    text-align: center;
}
div.stTextInput > label {
    font-size: 18px;
    color: #333333;
}
div.stMarkdown {
    font-size: 18px;
    color: #444444;
    font-family: "STKaiti", "KaiTi", serif;
}
.answer-box {
    background-color: #fff8dc;
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #e0c097;
    font-size: 18px;
    font-family: "STKaiti", "KaiTi", serif;
}
</style>
""", unsafe_allow_html=True)

# ---------------- API 配置 ----------------
# 建议在系统环境变量中设置 DEEPSEEK_API_KEY
os.environ["DEEPSEEK_API_KEY"] = "sk-2bae2305f5a748b9a1f8a641274244f9"
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# ---------------- 页面内容 ----------------
st.markdown("<h1>京剧关羽问答助手 🎭</h1>", unsafe_allow_html=True)
st.markdown("#### 👇 请输入你想问的问题（关于京剧中的关羽角色）")

question = st.text_input("")

if question:
    with st.spinner("正在请关羽大人答复中，请稍候..."):
        try:
            response = client.chat.completions.create(
                model="deepseek-chat",  # 或 deepseek-reasoner
                messages=[
                    {"role": "system", "content": "你是京剧专家，只回答京剧中关羽相关的问题。"},
                    {"role": "user", "content": question}
                ],
                stream=False
            )
            answer = response.choices[0].message.content
            st.markdown("#### 🎤 回答如下：")
            st.markdown(f"<div class='answer-box'>{answer}</div>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"请求失败：{e}")
