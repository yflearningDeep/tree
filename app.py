import streamlit as st

st.set_page_config(page_title="Merry Christmas for 小姝", layout="wide")

# 使用 HTML/CSS/JavaScript 构建高级 Three.js 动画
st.markdown("""
<div id="tree-canvas-container">
    <div class="overlay">
        <h1 class="glow-text">Merry Christmas</h1>
        <p class="name-tag">✨ For 小姝 ✨</p>
    </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
    const container = document.getElementById('tree-canvas-container');
    const scene = new THREE.Scene();
    const camera = new THREE.Camera();
    camera.position.z = 1;

    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setPixelRatio(window.devicePixelRatio);
    renderer.setSize(window.innerWidth, window.innerHeight);
    container.appendChild(renderer.domElement);

    // Three.js 着色器逻辑：模拟你图中那种金色粒子螺旋
    const geometry = new THREE.PlaneGeometry(2, 2);
    const material = new THREE.ShaderMaterial({
        uniforms: {
            time: { value: 1.0 },
            resolution: { value: new THREE.Vector2(window.innerWidth, window.innerHeight) }
        },
        vertexShader: `
            void main() {
                gl_Position = vec4(position, 1.0);
            }
        `,
        fragmentShader: `
            uniform float time;
            uniform vec2 resolution;

            void main() {
                vec2 uv = (gl_FragCoord.xy - 0.5 * resolution.xy) / min(resolution.y, resolution.x);
                vec3 finalColor = vec3(0.0);
                
                // 模拟金色螺旋线
                for(float i=0.0; i<40.0; i++) {
                    float t = time * 0.5 + i * 0.15;
                    float r = 0.45 * (1.0 - i/40.0); // 向上收缩形成尖顶
                    vec2 p = vec2(cos(t), sin(t)) * r;
                    p.y += i * 0.02 - 0.4; // 树的高度分布
                    
                    float dist = length(uv - p);
                    float glow = 0.0015 / dist; // 辉光效果
                    finalColor += vec3(1.0, 0.85, 0.4) * glow; // 金色调
                }
                
                // 添加背景星光
                float stars = fract(sin(dot(uv, vec2(12.9898, 78.233))) * 43758.5453);
                if(stars > 0.998) finalColor += vec3(0.5);

                gl_FragColor = vec4(finalColor, 1.0);
            }
        `
    });

    const mesh = new THREE.Mesh(geometry, material);
    scene.add(mesh);

    function animate(t) {
        material.uniforms.time.value = t / 1000;
        renderer.render(scene, camera);
        requestAnimationFrame(animate);
    }
    animate();

    window.addEventListener('resize', () => {
        renderer.setSize(window.innerWidth, window.innerHeight);
        material.uniforms.resolution.value.set(window.innerWidth, window.innerHeight);
    });
</script>

<style>
    /* 强制全屏黑底 */
    [data-testid="stAppViewContainer"] {
        background-color: #000 !important;
    }
    #tree-canvas-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: 1;
    }
    .overlay {
        position: absolute;
        top: 15%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
        z-index: 10;
        width: 100%;
    }
    .glow-text {
        font-family: 'Georgia', serif;
        color: #FFD700;
        font-size: 3.5rem;
        font-style: italic;
        text-shadow: 0 0 20px rgba(255, 215, 0, 0.8);
        margin: 0;
    }
    .name-tag {
        color: white;
        font-size: 1.2rem;
        letter-spacing: 4px;
        margin-top: 10px;
    }
    /* 隐藏所有多余的 Streamlit 元素 */
    header, footer, [data-testid="stToolbar"] { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# 雪花
st.snow()
# 音乐
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
