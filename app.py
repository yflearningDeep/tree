import streamlit as st
import plotly.graph_objects as go
import numpy as np
import random  # 修复报错：必须导入 random 模块

# 页面基础设置
st.set_page_config(page_title="送给小姝的3D圣诞树", page_icon="🎄")

# 自定义样式：黑底金字氛围感
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    .title-text {
        text-align: center;
        color: #FFD700;
        font-family: 'serif';
        text-shadow: 0 0 20px #FFD700;
        font-size: 3rem;
        margin-top: -50px;
    }
    .subtitle {
        text-align: center;
        color: #FFFFFF;
        font-size: 1.2rem;
        opacity: 0.8;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='title-text'>Merry Christmas</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>✨ 小姝，这是送给你的专属 3D 圣诞树 ✨</p>", unsafe_allow_html=True)

def create_3d_tree():
    # 1. 创建金色螺旋线（主树体）
    z = np.linspace(0, 10, 500)
    r = 10 - z
    theta = 12 * z
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    tree = go.Scatter3d(
        x=x, y=y, z=z,
        mode='lines',
        line=dict(color='#FFD700', width=8),
        name='Merry Christmas'
    )

    # 2. 创建背景星光（散落的白点）
    star_count = 150
    sz = np.random.uniform(0, 12, star_count)
    sr = np.random.uniform(0, 12, star_count)
    stheta = np.random.uniform(0, 2 * np.pi, star_count)
    sx = sr * np.cos(stheta)
    sy = sr * np.sin(stheta)

    stars = go.Scatter3d(
        x=sx, y=sy, z=sz,
        mode='markers',
        marker=dict(size=2, color='white', opacity=0.5),
        name='星辰'
    )

    # 3. 树上的彩色装饰点（闪烁感）
    light_count = 60
    lz = np.random.uniform(0, 10, light_count)
    lr = 10 - lz
    ltheta = np.random.uniform(0, 20 * np.pi, light_count)
    lx = lr * np.cos(ltheta)
    ly = lr * np.sin(ltheta)
    
    lights = go.Scatter3d(
        x=lx, y=ly, z=lz,
        mode='markers',
        marker=dict(
            size=6,
            color=[random.choice(['#FF0000', '#FFD700', '#FFFFFF', '#00FF00']) for _ in range(light_count)],
            opacity=0.9
        ),
        name='装饰灯'
    )

    # 4. 顶部的星
    top_star = go.Scatter3d(
        x=[0], y=[0], z=[10.5],
        mode='markers',
        marker=dict(size=15, color='#FFD700', symbol='diamond'),
        name='顶星'
    )

    fig = go.Figure(data=[tree, stars, lights, top_star])

    # 布局：全黑背景 + 初始旋转视角
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor='black',
        plot_bgcolor='black',
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            camera=dict(eye=dict(x=1.5, y=1.5, z=0.8)),
            aspectmode='cube'
        ),
        margin=dict(l=0, r=0, b=0, t=0),
        showlegend=False
    )
    return fig

# 自动下雪
st.snow()

# 显示 3D 树
st.plotly_chart(create_3d_tree(), use_container_width=True, config={'displayModeBar': False})

# 底部浪漫语
st.markdown("""
    <div style='text-align: center; color: #FFD700; padding: 20px;'>
        <p>你可以按住这棵树任意旋转，每个角度都是我对你的祝福。</p>
    </div>
    """, unsafe_allow_html=True)

# 音乐
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
