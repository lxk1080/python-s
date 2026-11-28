import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="streamlit入门",
    page_icon="🧊",
    # layout="wide", # 全屏宽度显示，不写的话默认在屏幕中间显示
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.baidu.com',
        'Report a bug': "https://www.baidu.com/s?wd=报告一个bug",
        'About': "一个很nb的app！"
    }
)

st.title('Streamlit 简易学习！')

st.write('随便说一句话，就是一个段落！')

image_path = Path(__file__).parent / 'imgs' / '01.jpg'
st.image(image_path, width=500)
# st.audio()
# st.video()

st.logo(Path(__file__).parent / 'imgs' / 'logo.png')

student_data = {
    '姓名': ['诸葛亮', '刘备', '孙权', '曹操'],
    '学号': ['10011', '10012', '10013', '10014'],
    '下属': ['诸葛瑾', '张飞', '周瑜', '许褚']
}
st.table(student_data)

name = st.text_input('你的名字：', 'whatever')
st.write(f'您的名字是：{name}')
psd = st.text_input('你的名字：', type='password')

gender = st.radio('请输入您的性别：', ['男', '女', '未知'])
st.write('您的性别是：', gender)
