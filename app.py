import streamlit as st
import plotly.graph_objects as go
import numpy as np
import time

# 页面基础设置
st.set_page_config(page_title="送给小姝的3D圣诞树", page_icon="🎄")

st.markdown("""
    <style>
    .stApp { background-color: #0E1117; }
    h1 { text-align: center; color: #FF4B4B; font-family: 'Microsoft YaHei'; }
    .wish { text-align: center; color: #FFD700; font-size: 1.5rem; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>✨ 小姝，圣诞快乐 ✨</h1>", unsafe_allow_html=True)
st.markdown("<p class='wish'>这是一个可以旋转、缩放的专属圣诞树 🎁</p>", unsafe_allow_html=True)

# --- 核心：构建 3D 圣诞树数据 ---
def create_3d_tree():
    # 生成螺旋上升的树体
    z = np.linspace(0, 10, 1000)
    r = 10 - z  # 越往上半径越小
    theta = 15 * z  # 旋转角度

    x = r * np.cos(theta)
    y = r * np.sin(theta)

    # 树主体（绿色螺旋）
    tree = go.Scatter3d(
        x=x, y=y, z=z,
        mode='lines',
        line=dict(color='green', width=10),
        name='圣诞树'
    )

    # 随机生成彩色装饰灯
    num_lights = 100
    lz = np.random.uniform(0, 10, num_lights)
    lr = 10 - lz
    ltheta = np.random.uniform(0, 2 * np.pi * 15, num_lights)
    lx = lr * np.cos(ltheta)
    ly = lr * np.sin(ltheta)
    
    # 彩色灯泡
    lights = go.Scatter3d(
        x=lx, y=ly, z=lz,
        mode='markers',
        marker=dict(
            size=random.sample(range(5, 12), 1)[0],
            color=random.sample(['red', 'yellow', 'blue', 'white', 'magenta', 'cyan'], 1)[0],
            symbol='circle'
        ),
        name='彩灯'
    )

    # 顶部的星星
    star = go.Scatter3d(
        x=[0], y=[0], z=[10.5],
        mode='markers',
        marker=dict(size=15, color='gold', symbol='diamond'),
        name='星光'
    )

    fig = go.Figure(data=[tree, lights, star])

    # 设置布局，隐藏坐标轴
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, b=0, t=0),
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            aspectmode='cube'
        ),
        showlegend=False
    )
    return fig

# 动态闪烁效果
placeholder = st.empty()

# 自动撒雪花
st.snow()

# 显示 3D 图像
fig = create_3d_tree()
st.plotly_chart(fig, use_container_width=True)

# 底部留言板
st.info(f"💡 提示小姝：可以用手指或鼠标按住这棵树旋转查看哦！")

# 增加一个温馨的文本区
with st.expander("点击开启给小姝的悄悄话"):
    st.write("""
    小姝：
    希望这棵会旋转的圣诞树能给你带来一点点惊喜。
    愿你的生活像这些彩灯一样，永远灿烂夺目！
    """)

st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
