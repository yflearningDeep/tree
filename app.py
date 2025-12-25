import streamlit as st
import random
import time

st.set_page_config(page_title="圣诞惊喜", page_icon="🎁")

# 自定义 CSS 让背景变黑，更有氛围
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; }
    .tree-text { font-family: monospace; line-height: 1.2; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌟 远方的圣诞祝福")

placeholder = st.empty()

# 动态生成的圣诞树
def generate_tree():
    colors = ["🔴", "🟡", "🔵", "🟢", "⚪"]
    tree_str = "<div class='tree-text' style='color: #228B22; font-size: 20px;'>"
    tree_str += "✨<br>" # 顶部的星
    
    for i in range(1, 11):
        # 随机在树上挂灯点
        row = "".join([random.choice(colors) if random.random() < 0.2 else "🎄" for _ in range(i)])
        tree_str += row + "<br>"
        
    tree_str += "🤎🤎<br>🤎🤎"
    tree_str += "</div>"
    return tree_str

# 循环刷新模拟闪烁
for _ in range(50):
    with placeholder.container():
        st.markdown(generate_tree(), unsafe_allow_html=True)
        st.snow()
    time.sleep(1)

st.balloons()
st.success("这是送给你的专属圣诞树！")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3") # 自动播放背景音示例
