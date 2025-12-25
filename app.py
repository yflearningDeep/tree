import streamlit as st
import streamlit.components.v1 as components

# 页面基础配置
st.set_page_config(page_title="Merry Christmas for 小姝", layout="wide")

# 强制全屏纯黑背景
st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    header, footer { visibility: hidden !important; }
    </style>
    """, unsafe_allow_html=True)

# 专属标题和祝福
st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <h1 style="color: #FFD700; font-family: 'Times New Roman', serif; font-style: italic; font-size: 3rem; text-shadow: 0 0 15px #FFD700;">Merry Christmas</h1>
        <p style="color: #ffffff; font-size: 1.2rem; letter-spacing: 5px; opacity: 0.8;">✨ For 小姝 ✨</p>
    </div>
    """, unsafe_allow_html=True)

# 核心：使用独立组件渲染自动旋转的金色粒子树
# 这段代码直接在沙盒中运行，100% 能够显示
tree_html = """
<canvas id="treeCanvas"></canvas>
<style>
    body { margin: 0; background: black; overflow: hidden; display: flex; justify-content: center; }
    canvas { background: black; }
</style>
<script>
    const canvas = document.getElementById('treeCanvas');
    const ctx = canvas.getContext('2d');

    // 适配屏幕大小
    canvas.width = 600;
    canvas.height = 500;

    let angle = 0;

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        angle += 0.015; // 自动旋转的速度

        const centerX = canvas.width / 2;
        const centerY = canvas.height - 50;

        // 渲染 1200 颗粒子
        for (let i = 0; i < 1200; i++) {
            let y = i * 0.3; // 粒子高度
            let radius = (400 - y) * 0.3; // 随高度变细
            
            // 核心螺旋算法
            let spiralAngle = angle + (i * 0.1); 
            let x = centerX + Math.cos(spiralAngle) * radius;
            
            // 3D 深度感：利用正弦波模拟近大远小、近亮远暗
            let perspective = Math.sin(spiralAngle);
            let size = perspective * 1.5 + 1.8;
            let alpha = perspective * 0.5 + 0.5;

            ctx.beginPath();
            ctx.fillStyle = `rgba(255, 215, 0, ${alpha})`; // 金粉颜色
            ctx.arc(x, centerY - y, size, 0, Math.PI * 2);
            ctx.fill();

            // 随机星光点缀
            if (i % 60 === 0) {
                ctx.fillStyle = `rgba(255, 255, 255, ${Math.random()})`;
                ctx.fillRect(Math.random() * canvas.width, Math.random() * canvas.height, 1.5, 1.5);
            }
        }

        // 顶部的星
        ctx.fillStyle = '#FFD700';
        ctx.font = '35px serif';
        ctx.textAlign = 'center';
        ctx.fillText('⭐', centerX, centerY - 410);

        requestAnimationFrame(animate);
    }
    animate();
</script>
"""

# 调用组件渲染，设置足够的高度
components.html(tree_html, height=550)

# 底部留言
st.markdown("""
    <div style="text-align: center; color: #FFD700; font-size: 0.9rem; margin-top: 20px;">
        <p>愿这棵不停转动的星光树，带给你整个冬天的温暖。</p>
    </div>
    """, unsafe_allow_html=True)

# 浪漫雪花和背景音
st.snow()
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
