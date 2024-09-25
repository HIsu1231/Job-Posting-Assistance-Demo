import streamlit as st
from PIL import Image
from datetime import datetime

st.title(st.session_state['job_title'])


# HTML과 CSS를 사용하여 텍스트 상자 모양 구현
keywords_html = f"""
    <style>
    .review-box {{
        display: inline-block;
        background-color: #f1f3f5;
        color: #4d4d4d;
        padding: 10px 15px;
        border-radius: 15px;
        margin: 1px 5px 10px 1px;
        font-size: 16px;
        font-weight: bold;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
    }}
    .emoji {{
        margin-right: 8px;
    }}
    </style>
"""

certification_html = f"""
    <style>
    .review-box {{
        display: inline-block;
        background-color: #f1f3f5;
        color: #4d4d4d;
        padding: 10px 15px;
        border-radius: 15px;
        margin: 1px 5px 10px 1px;
        font-size: 16px;
        font-weight: bold;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
    }}
    .emoji {{
        margin-right: 8px;
    }}
    </style>
"""
custom_css = """
<style>
h2 {
    margin-bottom: 0px; /* "혜택 및 복지" 제목과 박스들 사이 간격 */
}
.box {
    display: inline-block;
    padding: 10px 20px;
    margin: 1px 5px 10px 1px;
    border-radius: 15px;
    background-color: #f1f3f5;
    font-size: 16px;
    font-weight: bold;
    color: #333;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}
.box-container {
    margin-bottom: 20px; /* 박스들과 그다음 제목 사이 간격 넓힘 */
}
.box span {
    margin-right: 10px;
}
</style>
"""

keywords_html += "<div>"
selected_keywords = [selected for i, selected in enumerate(st.session_state['job_keyword']) if selected]

# selected_keywords 리스트에서 값을 가져와서 HTML로 추가
emoji_list = ['🤘', '⏱️', '📣', '⚙️', '💡']  # 필요시 더 추가 가능
for i, keyword in enumerate(selected_keywords):
    emoji = emoji_list[i % len(emoji_list)]  # 리스트 길이를 넘어가면 다시 첫 번째 이모티콘으로 순환
    keywords_html += f'<div class="review-box"><span class="emoji">{emoji}</span> {keyword}</div>'

keywords_html += "</div>"

st.markdown(keywords_html, unsafe_allow_html=True)

col1, col2 = st.columns([4.6, 1])
with col2:
    # 공고 게시일 출력
    if st.session_state['publication'] == "직접 설정":
        publication_date = datetime.strptime(st.session_state["date_of_publication"], "%Y-%m-%d").strftime("%Y-%m-%d")
        st.write("공고 게시일: ", publication_date)
    else:
        today_date = datetime.today().strftime("%Y-%m-%d")
        st.write("공고 게시일: ", today_date)

    # 공고 마감일 출력
    if st.session_state['Deadline'] == "직접 설정":
        deadline_date = datetime.strptime(st.session_state['deadline_date'], "%Y-%m-%d").strftime("%Y-%m-%d")
        st.write("공고 마감일: ", deadline_date)
    else:
        deadline_date = datetime.strptime(st.session_state['Deadline'], "%Y-%m-%d").strftime("%Y-%m-%d")
        st.write("공고 마감일: ", deadline_date)

container1 = st.container(border=True)
with container1:
    if st.session_state['business_registration_number'] == "111-11-11111":
        st.subheader('회사 소개')
        st.write(st.session_state['braincore'])
    elif st.session_state['business_registration_number'] == "222-22-22222":
        st.subheader('회사 소개')
        st.write(st.session_state['neotech'])
    elif st.session_state['business_registration_number'] == "333-33-33333":
        st.subheader('회사 소개')
        st.write(st.session_state['green'])

    st.subheader('직군')
    selected_job_category = [selected for i, selected in enumerate(st.session_state['job_category']) if selected]
    #selected_job_role = [selected for i, selected in enumerate(st.session_state['job_role']) if selected]
    keywords_html = f'<div class="review-box">{selected_job_category[0]}</div>'
    st.markdown(keywords_html, unsafe_allow_html=True)
    st.write('')
    st.subheader('직무 소개')
    st.write(st.session_state['company_introduction_text'])

container2 = st.container(border=True)
with container2:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('주요 업무')
        st.write(st.session_state['major_task_text'])
    with col2:
        st.subheader('우대 사항')
        st.write(st.session_state['qualification_requirements_text'])
    st.subheader('자격 면허')
    certification_html += "<div>"
    selected_certification = [selected for i, selected in enumerate(st.session_state['job_certification']) if selected]
    for i, certification in enumerate(selected_certification):
        certification_html += f'<div class="review-box">{certification}</div>'
    certification_html += "</div>"
    st.markdown(certification_html, unsafe_allow_html=True)
    st.write('')
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('기술 스택')
        st.write(st.session_state['skill_text'])
    with col2:
        st.subheader('경력')
        if st.session_state['experience'] == "경력":
            st.write(st.session_state['year_of_experience_min'], '년 이상', st.session_state['year_of_experience_max'], '년 이하')
        else:
            st.write(st.session_state['experience'])


container3 = st.container(border=True)
with container3:
    st.markdown(custom_css, unsafe_allow_html=True)
    st.subheader('혜택 및 복지')
    boxes = '<div class="box-container">'
    for i, item in enumerate(st.session_state['selected_welfare']):
        boxes += f'<div class="box">{item}</div>'
    boxes += '</div>'
    st.markdown(boxes, unsafe_allow_html=True)

    st.subheader('채용 전형')
    boxes = '<div class="box-container">'
    for i, item in enumerate(st.session_state['selected_recruitment']):
        if item == "최종 합격":
            continue
        else:
            boxes += f'<div class="box">{item}</div>'

    boxes += f'<div class="box">최종 합격</div>'
    boxes += '</div>'
    st.markdown(boxes, unsafe_allow_html=True)





    st.subheader('근무지')
    st.write(st.session_state['work_place'])

    if st.session_state['business_registration_number'] == "111-11-11111":
        image_path = "./pages/브레인코어.png"
        image = Image.open(image_path)
        st.image(image, width=600)
    elif st.session_state['business_registration_number'] == "222-22-22222":
        image_path = "./pages/네오텍.png"
        image = Image.open(image_path)
        st.image(image, width=600)
    elif st.session_state['business_registration_number'] == "333-33-33333":
        image_path = "./pages/green.png"
        image = Image.open(image_path)
        st.image(image, width=600)


