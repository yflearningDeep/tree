import streamlit as st
import time
import random

# 页面配置：设置标题和图标
st.set_page_config(page_title="小姝的专属圣诞礼物", page_icon="🎄", layout="centered")

# --- 豪华视觉样式 (CSS) ---
st.markdown("""
    <style>
    /* 全局背景设为深邃夜空黑 */
    .stApp {
        background: linear-gradient(to bottom, #000428, #004e92);
        color: white;
    }
    
    /* 标题动画：流光溢彩效果 */
    .title-text {
        font-family: 'Microsoft YaHei', sans-serif;
        font-size: 3rem !important;
        text-align: center;
        background: linear-gradient(90deg, #ff0000, #ffff00, #00ff00, #00ffff, #ff00ff, #ff0000);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradient 5s ease infinite;
        font-weight: bold;
        text-shadow: 2px 2px 10px rgba(255,255,255,0.3);
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* 树体居中 */
    .tree-container {
        font-family: 'Courier New', Courier, monospace;
        text-align: center;
        line-height: 1.1;
        font-size: 22px;
    }
    
    /* 底部祝福语样式 */
    .wish-text {
        font-size: 1.2rem;
        text-align: center;
        color: #FFD700;
        margin-top: 20px;
        font-style: italic;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 顶层内容 ---
st.markdown('<h1 class="title-text">✨ 小姝 圣诞快乐 ✨</h1>', unsafe_allow_html=True)
st.snow() # 持续下雪特效

# --- 动态圣诞树逻辑 ---
placeholder = st.empty()

def create_luxury_tree():
    # 装饰物和色彩
    decorations = ["🔴", "🟡", "🔵", "💖", "❄️", "🎁", "✨"]
    tree_layers = 15
    tree_output = "<div class='tree-container'>"
    tree_output += "<span style='font-size: 40px;'>⭐</span><br>" # 顶部的星
    
    for i in range(1, tree_layers):
        # 每一行随机生成装饰物和绿叶
        row = ""
        for j in range(i * 2 - 1):
            if random.random() < 0.2: # 20% 概率出现装饰物
                row += random.choice(decorations)
            else:
                row += "🎄"
        tree_output += f"{row}<br>"
    
    # 树干
    tree_output += "<span style='font-size: 25px;'>🤎🤎🤎</span><br>"
    tree_output += "<span style='font-size: 25px;'>🤎🤎🤎</span>"
    tree_output += "</div>"
    return tree_output

# --- 交互动画循环 ---
for i in range(20): # 循环刷新让灯光“闪烁”
    with placeholder.container():
        st.markdown(create_luxury_tree(), unsafe_allow_html=True)
        
        # 专属小姝的浪漫文字（随机切换）
        wishes = [
            "小姝，愿你的眼中总有光，心中总有爱。🎁",
            "在这个冬日，希望这棵树能带给你温暖。🌟",
            "叮叮当，叮叮当，小姝的礼物在身旁。💖",
            "愿这闪烁的灯火，照亮你新的一年。❄️"
        ]
        st.markdown(f'<p class="wish-text">{random.choice(wishes)}</p>', unsafe_allow_html=True)
        time.sleep(1.2)

# --- 底部彩蛋 ---
st.balloons() # 刷出气球
st.markdown("---")
st.write("特别定制版 | 仅献给小姝")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3") # 背景音乐
