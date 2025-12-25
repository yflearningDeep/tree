import streamlit as st

st.set_page_config(page_title="Merry Christmas for 小姝", layout="wide")

# 强制隐藏 Streamlit 默认的白边和菜单，打造沉浸式纯黑背景
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] { background-color: #000000 !important; }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    .stAudio { margin-top: 20px; filter: invert(100%); } /* 音乐播放器适配黑夜模式 */
</style>
""", unsafe_allow_html=True)

# 核心代码：使用 Canvas + JS 绘制高精度自动旋转金色粒子树
st.markdown("""
<div style="text-align: center; margin-top: 50px;">
    <h1 style="color: #FFD700; font-family: 'Times New Roman', serif; font-style: italic; font-size: 3.5rem; text-shadow: 0 0 20px #FFD700; margin-bottom: 0;">Merry Christmas</h1>
    <p style="color: #ffffff; font-size: 1.2rem; letter-spacing: 5px; opacity: 0.8;">✨ For 小姝 ✨</p>
    <canvas id="treeCanvas" style="background: #000; width: 100%; max-width: 600px; height: 500px;"></canvas>
    <p style="color: #FFD700; font-size: 0.9rem; margin-top: 30px; letter-spacing: 2px;">愿你在闪烁的光芒中，遇见所有的美好</p>
</div>

<script>
    const canvas = document.getElementById('treeCanvas');
    const ctx = canvas.getContext('2d');
    canvas.width = 600;
    canvas.height = 500;

    let angle = 0;

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        angle += 0.02; // 旋转速度

        const centerX = canvas.width / 2;
        const centerY = canvas.height - 50;

        // 绘制数千颗金色粒子形成螺旋
        for (let i = 0; i < 1500; i++) {
            // 粒子的高度
            let y = i * 0.25;
            // 越往上半径越小
            let radius = (500 - y) * 0.35;
            
            // 螺旋旋转算法
            let currentAngle = angle + i * 0.15;
            let x = centerX + Math.cos(currentAngle) * radius;
            
            // 模拟 3D 透视：近大远小，近亮远暗
            let scale = Math.sin(currentAngle) * 0.5 + 0.5;
            let size = scale * 1.5 + 0.5;
            let alpha = scale * 0.5 + 0.2;

            ctx.fillStyle = `rgba(255, 215, 0, ${alpha})`;
            ctx.beginPath();
            ctx.arc(x, centerY - y, size, 0, Math.PI * 2);
            ctx.fill();
            
            // 随机加一点点闪烁的星星作为背景
            if (i % 50 === 0) {
                ctx.fillStyle = `rgba(255, 255, 255, ${Math.random()})`;
                ctx.fillRect(Math.random()*canvas.width, Math.random()*canvas.height, 1, 1);
            }
        }
        
        // 顶部的星
        ctx.fillStyle = '#FFD700';
        ctx.font = '30px serif';
        ctx.fillText('⭐', centerX - 15, centerY - 400);

        requestAnimationFrame(draw);
    }

    draw();
</script>
""", unsafe_allow_html=True)

# 撒雪花
st.snow()

# 音乐
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
