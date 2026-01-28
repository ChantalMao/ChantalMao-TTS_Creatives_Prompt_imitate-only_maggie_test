import streamlit as st

st.set_page_config(page_title="Prompt Generator Demo", layout="wide")
st.title("提示词生成器 Demo")

with st.sidebar:
    st.header("素材与参数")
    image_file = st.file_uploader("上传商品图片 (png/jpg/webp)", type=["png", "jpg", "jpeg", "webp"])
    video_file = st.file_uploader("上传参考视频 (mp4,mov)", type=["mp4", "mov"], help="可选")
    product_name = st.text_input("商品名称")
    selling_points = st.text_area("商品卖点（每行一条）")
    target_market = st.selectbox("投放市场", ["US", "China", "Japan", "EU", "Other"])
    target_language = st.selectbox("投放语言", ["English", "中文", "日本語"])
    output_count = st.number_input("输出条数 (1-5)", min_value=1, max_value=5, value=3)
    audio_option = st.selectbox("音频选项", ["TTS", "Human voice", "None"])
    bgm_style = st.text_input("BGM 风格 (例如: energetic pop)")
    generate_btn = st.button("生成提示词")

st.write("这里会显示素材审计与生成结果（示例）")
if image_file:
    st.image(image_file, caption="上传的商品图片预览", use_column_width=True)

if generate_btn:
    st.info("已提交生成请求（本 demo 不调用 Gemini）。在实际项目中这里会调用后端 API。")
    st.write({
        "product_name": product_name,
        "selling_points": selling_points,
        "target_market": target_market,
        "target_language": target_language,
        "output_count": output_count,
        "audio_option": audio_option,
        "bgm_style": bgm_style,
    })
