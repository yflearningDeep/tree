import streamlit as st

# 页面配置
st.set_page_config(page_title="Merry Christmas 小姝", layout="centered")

# 核心：纯 HTML + CSS 动画代码
# 这种方式可以直接控制每一条线条的粗细、金色渐变和自动旋转
st.markdown("""
<div class="container">
    <div class="tree-container">
        <h1 class="merry">Merry Christmas</h1>
        <p class="to-who">✨ For 小姝 ✨</p>
        
        <div class="tree">
            <div class="star">⭐</div>
            <div class="spirals">
                <div class="spiral s1"></div>
                <div class="spiral s2"></div>
                <div class="spiral s3"></div>
            </div>
            <div class="trunk"></div>
        </div>
        
        <div class="footer">愿你在这闪烁光芒中，遇见所有的美好。</div>
    </div>
</div>

<style>
/* 纯黑背景 */
[data-testid="stAppViewContainer"] {
    background-color: #000 !important;
}

.container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 80vh;
    flex-direction: column;
}

.merry {
    font-family: 'Times New Roman', serif;
    color: #FFD700;
    text-shadow: 0 0 15px #FFD700;
    font-style: italic;
    font-size: 3.5rem;
    margin-bottom: 0px;
}

.to-who {
    color: #fff;
    font-size: 1.2rem;
    letter-spacing: 5px;
    margin-bottom: 30px;
}

/* 圣诞树主体 */
.tree {
    position: relative;
    width: 200px;
    height: 300px;
    display: flex;
    justify-content: center;
}

.star {
    position: absolute;
    top: -40px;
    font-size: 40px;
    filter: drop-shadow(0 0 10px gold);
    z-index: 10;
}

/* 金色螺旋线核心逻辑 */
.spiral {
    position: absolute;
    top: 0;
    width: 150px;
    height: 250px;
    border-radius: 50%;
    border: 3px solid transparent;
    border-bottom: 5px solid #FFD700; /* 金色边框 */
    box-shadow: 0 5px 15px rgba(255, 215, 0, 0.4);
    animation: rotate 3s linear infinite;
}

/* 不同层次的螺旋实现层次感 */
.s1 { transform: scale(0.2); animation-duration: 2s; top: -50px;}
.s2 { transform: scale(0.6); animation-duration: 3s; top: 0px;}
.s3 { transform: scale(1.0); animation-duration: 4s; top: 50px;}

@keyframes rotate {
    0% { transform: rotateX(70deg) rotateZ(0deg); }
    100% { transform: rotateX(70deg) rotateZ(360deg); }
}

.trunk {
    position: absolute;
    bottom: -20px;
    width: 20px;
    height: 40px;
    background: linear-gradient(to right, #331a00, #663300);
}

.footer {
    margin-top: 100px;
    color: #FFD700;
    font-size: 0.9rem;
    letter-spacing: 2px;
}
</style>
""", unsafe_allow_html=True)

# 雪花特效
st.snow()

# 音乐
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
