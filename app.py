import streamlit as st
import time

# 设置页面配置
st.set_page_config(page_title="圣诞快乐", page_icon="🎄")

st.title("🎄 圣诞快乐！")

# 这里的代码会生成一个带闪烁效果的文字圣诞树
tree = [
    "⭐",
    "🎄",
    "🎄🎄",
    "🎄🎄🎄",
    "🎄🎄🎄🎄",
    "🎄🎄🎄🎄🎄",
    "🎄🎄🎄🎄🎄🎄",
    "||"
]

placeholder = st.empty()

# 添加一段温馨的音乐（可选，需要你有mp3链接）
# st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

# 循环制作闪烁效果
for i in range(100):
    with placeholder.container():
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        for row in tree:
            # 随机加一点点颜色偏移（模拟闪烁）
            st.write(row)
        st.markdown("</div>", unsafe_allow_html=True)

    st.balloons()  # 撒气球特效
    st.snow()  # 下雪特效
    time.sleep(2)

st.success("愿你的圣诞节充满温暖和欢笑！")