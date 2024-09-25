import streamlit as st
import pyperclip
from datetime import datetime
from initializer import *
from func import *

# 세션 상태 초기화 및 리스트 가져오기
welfare_list, recruitment_list = initialize_session_state()
custom_styles = load_custom_styles()
st.markdown(custom_styles, unsafe_allow_html=True)

#################################사이드바######################################
#사업자 등록 번호
st.session_state['business_registration_number'] = st.sidebar.text_input("사업자 등록 번호", placeholder = "사업자 등록 번호를 입력해 주세요.",value=st.session_state['business_registration_number'])
#공고 내용
st.session_state['job_description'] = st.sidebar.text_area("공고 내용", placeholder = "구인 공고에 들어갈 필수적인 내용을 작성해주세요.", height=100, value=st.session_state['job_description'])
#복지 입력
st.session_state['welfare'] = st.sidebar.multiselect("혜택 및 복지", welfare_list, default=st.session_state['welfare'])
welfare = st.session_state['welfare']
st.session_state['other_welfare'] = st.sidebar.text_input("기타 복지 입력 (쉼표로 구분해서 입력 후 Enter)", value=st.session_state['other_welfare'])
selected_welfare = load_selected_welfare()
st.session_state['selected_welfare'] = selected_welfare

#채용 전형 입력
st.session_state['recruitment'] = st.sidebar.multiselect("채용 전형", recruitment_list, default=st.session_state['recruitment'])
recruitment = st.session_state['recruitment']
st.session_state['other_recruitment'] = st.sidebar.text_input("기타 채용 전형 입력 (쉼표로 구분해서 입력 후 Enter)", value=st.session_state['other_recruitment'])
selected_recruitment = load_selected_recruitment()
st.session_state['selected_recruitment'] = selected_recruitment

# 톤 선택 라디오 버튼 (사이드바)
tone = st.sidebar.radio("톤 선택", ("격식있게", "친근하게"))

if st.sidebar.button('✨ 직무/직종/키워드 생성', key='keyword_generation_btn'):
    st.session_state['keyword_generation'] = True


#####################################################직무/직종/키워드 (1. 브레인코어)####################################################
if st.session_state.keyword_generation:
    if st.session_state['business_registration_number'] == "111-11-11111":
        job_categories, job_roles, job_certification, job_keywords = load_braincore1()
        load_braincore2()


    st.text_area("회사 소개", st.session_state['braincore'], height=165)
    generate_checkbox_section("1. 추천 직종", 'job_category', job_categories)
    #generate_checkbox_section("2. 추천 직무", 'job_role', job_roles)
    generate_checkbox_section("2. 직종 키워드", 'job_keyword', job_keywords)
    generate_checkbox_section("3. 추천 자격증", 'job_certification', job_certification)

    for i in range(5):
        if st.session_state.job_category[i]:
            st.session_state.job_category[i] = job_categories[i]
        if st.session_state.job_certification[i]:
            st.session_state.job_certification[i] = job_certification[i]
        if st.session_state.job_keyword[i]:
            st.session_state.job_keyword[i] = job_keywords[i]

    col1, col2, col3, col4 = st.columns(4)
    with col2:
        if st.button('✨ 초안 생성', key='draft_generation_btn'):
            st.session_state['draft_generation'] = True
    with col3:
        st.button("🚿 초기화 ")

st.write()
st.write()


#####################################################초안 생성####################################################

if st.session_state['draft_generation']:

    container1 = st.container(border=True)
    container2 = st.container(border=True)
    container3 = st.container(border=True)
    with container1:
        #st.subheader("채용 정보 입력 1")
        ## 모집 직종
        st.session_state["job_title"] = st.text_input("공고 제목", value=st.session_state["job_title"])
        col1, col2, col3 = st.columns([3, 1, 4])
        with col1:
            selected_category_role = [selected for i, selected in enumerate(st.session_state['job_category']) if selected]
            st.session_state['job_category_text'] = st.text_input('모집 직종', value=selected_category_role[0])
        with col2:
            st.write("")
            st.write("")
            st.markdown('<button class="custom-button">직종 찾기</button>', unsafe_allow_html=True)
        with col3:
            selected_job_certification = [selected for i, selected in enumerate(st.session_state['job_certification']) if selected]
            s = ""
            for i in range(len(selected_job_certification)):
                if i == len(selected_job_certification) - 1:
                    s +=  selected_job_certification[i]
                else:
                    s += selected_job_certification[i]
                    s += ', '

            st.session_state['job_role_certification'] = st.text_input('자격면허', value=s)
        #with col4:
        #    st.write("")
        #    st.write("")
        #    st.markdown('<button class="custom-button">직무 찾기</button>', unsafe_allow_html=True)

        ## 직종 키워드
        st.markdown('<div class="custom-label">선택 키워드</div>', unsafe_allow_html=True)
        keywords_html = f"""
            <style>
            .review-box {{ display: inline-block; background-color: #f1f3f5; color: #4d4d4d; padding: 10px 15px; border-radius: 15px; margin: 4px;
                           font-size: 16px; font-weight: bold; box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1); margin-bottom: 20px; /* 아래쪽 마진을 줄여서 간격을 조정 (2px) */}}
            .emoji {{margin-right: 8px;}} </style> """
        keywords_html += "<div>"
        selected_keywords = [selected for i, selected in enumerate(st.session_state['job_keyword']) if selected]
        emoji_list = ['🤘', '⏱️', '📣', '⚙️', '💡']  # 필요시 더 추가 가능\

        for i, keyword in enumerate(selected_keywords):
            emoji = emoji_list[i % len(emoji_list)]  # 리스트 길이를 넘어가면 다시 첫 번째 이모티콘으로 순환
            keywords_html += f'<div class="review-box"><span class="emoji">{emoji}</span> {keyword}</div>'
        keywords_html += "</div>"
        st.markdown(keywords_html, unsafe_allow_html=True)

    with container2:
        #st.subheader("채용 정보 입력 2")
        ## 직무 소개
        st.markdown('<div class="custom-label">직무 소개</div>', unsafe_allow_html=True)
        st.session_state['company_introduction_text'] = st.text_area('직무 소개', value=st.session_state['company_introduction_text'], height=183, label_visibility='collapsed')

        ## 주요 업무
        st.markdown('<div class="custom-label">주요 업무</div>', unsafe_allow_html=True)
        st.session_state['major_task_text'] = st.text_area('주요 업무', value=st.session_state['major_task_text'], height=142, label_visibility='collapsed')

        ## 우대 사항
        st.markdown('<div class="custom-label">우대 사항</div>', unsafe_allow_html=True)
        st.session_state['qualification_requirements_text'] = st.text_area('우대사항', value=st.session_state['qualification_requirements_text'], height=140, label_visibility='collapsed')

        ## 혜택 및 복지
        st.markdown('<div class="custom-label">혜택 및 복지</div>', unsafe_allow_html=True)
        st.session_state['benefits_and_welfare_text'] = st.text_area('혜택 및 복지', value=st.session_state['benefits_and_welfare_text'], height=120, label_visibility='collapsed')

        ## 채용 전형
        st.markdown('<div class="custom-label">채용 전형</div>', unsafe_allow_html=True)
        st.session_state['recruitment_text'] = st.text_area('채용 전형', value=st.session_state['recruitment_text'], height=120, label_visibility='collapsed')

        ## 기술 스택
        st.markdown('<div class="custom-label">기술 스택</div>', unsafe_allow_html=True)
        st.session_state['skill_text'] = st.text_area('기술 스택', value=st.session_state['skill_text'], height=100, label_visibility='collapsed')


        with container3:
            #st.subheader("채용 정보 입력 3")
            col1, col2 = st.columns(2)
            with col1:
                st.session_state['work_place'] = st.text_area('근무지', value=st.session_state['work_place'])
            with col2:
                st.markdown('<p class="small-text">· 연봉정보는 통계 자료로만 쓰이며 절대 공개되지 않습니다.</p>', unsafe_allow_html=True)
                col3, col4, col5 = st.columns([2, 0.2, 2])
                with col3:
                    st.session_state['salary_min'] = st.number_input('최소 연봉 (만원)', min_value=0, max_value=10000, step=10, value=st.session_state['salary_min'])
                with col4:
                    st.write("~")
                with col5:
                    st.session_state['salary_max'] = st.number_input('최대 연봉 (만원)', min_value=0, max_value=10000, step=10, value=st.session_state['salary_max'])
            col1, col2 = st.columns(2)
            with col1:
                st.session_state['experience'] = st.radio("경력", options=["신입", "경력"], index=["신입", "경력"].index(st.session_state['experience']), horizontal=True)
            with col2:
                if st.session_state['experience'] == "경력":
                    col3, col4, col5 = st.columns([2, 0.2, 2])
                    with col3:
                        st.session_state['year_of_experience_min'] = st.number_input('최소 경력 (년)', min_value=0, max_value=35, step=1, value=st.session_state['year_of_experience_min'])
                    with col4:
                        st.write("~")
                    with col5:
                        st.session_state['year_of_experience_max'] = st.number_input('최대 경력 (년)', min_value=0, max_value=35, step=1, value=st.session_state['year_of_experience_max'])
                    st.write(
                        f"경력: {st.session_state['year_of_experience_min']}년 이상 {st.session_state['year_of_experience_max']}년 이하")
            col1, col2 = st.columns(2)
            with col1:
                st.session_state['publication'] = st.radio("게시일", options=["바로 게시", "직접 설정"], index=["바로 게시", "직접 설정"].index(st.session_state['publication']), horizontal=True)
            with col2:
                # 경력 연수 선택 (만약 경력을 선택한 경우만)
                if st.session_state['publication'] == "직접 설정":
                    st.session_state['date_of_publication'] = st.date_input("게시일 입력")
            col1, col2 = st.columns(2)
            with col1:
                st.session_state['Deadline'] = st.radio("마감일", options=["상시", "직접 설정"], index=["상시", "직접 설정"].index(st.session_state['Deadline']), horizontal=True)
            with col2:
                if st.session_state['Deadline'] == "직접 설정":
                    st.session_state['deadline_date'] = st.date_input("마감일 입력", value=st.session_state['deadline_date'])

    col1, col2, col3 = st.columns(3)
    with col2:
        st.link_button("👀 미리 보기", url='https://job-posting-assistance-demo-7vdkgrkgvzuq87jtcxlfsp.streamlit.app/%EB%AF%B8%EB%A6%AC%EB%B3%B4%EA%B8%B0')






    # st.markdown("<h4 style='font-weight: bold;'>4. 직무 내용</h4>", unsafe_allow_html=True)
    # st.session_state['job_description_result'] = st.text_area(
    #     '직무 내용', value=st.session_state['job_description_result'], height=200, label_visibility='collapsed')
    #
    # col1, col2, col3 = st.columns([10, 2.8, 2])
    # # 회사/직무 소개 전체 삭제 버튼을 누른 경우 텍스트를 삭제
    # with col2:
    #     if st.button("🗑️ 전체 삭제", key='delete_company_intro'):
    #         st.session_state['job_description_result'] = ""  # 텍스트 상자 내용을 빈 문자열로 설정
    #         st.rerun()
    # with col3:
    #     # 복사 버튼을 누른 경우, 복사 알림 메시지 출력
    #     if st.button("📄 복사", key='copy_company_intro'):
    #         pyperclip.copy(st.session_state['job_description_result'])  # 텍스트 복사
    #
    # st.markdown("<h5 style='font-weight: bold;'>5. 추천 자격증</h4>", unsafe_allow_html=True)
    # col1, col2, col3, col4, col5 = st.columns(5)
    # # 각 직종 키워드 선택 상태를 체크박스로 표시
    # with col1:
    #     st.session_state['license'][0] = st.checkbox('추천 자격증 1', value=st.session_state['license'][0])
    # with col2:
    #     st.session_state['license'][1] = st.checkbox('추천 자격증 2', value=st.session_state['license'][1])
    # with col3:
    #     st.session_state['license'][2] = st.checkbox('추천 자격증 3', value=st.session_state['license'][2])
    # with col4:
    #     st.session_state['license'][3] = st.checkbox('추천 자격증 4', value=st.session_state['license'][3])
    # with col5:
    #     st.session_state['license'][4] = st.checkbox('추천 자격증 5', value=st.session_state['license'][4])
    #
    # st.markdown("<h5 style='font-weight: bold;'>6. 채용 정보 검색어</h4>", unsafe_allow_html=True)
    # col1, col2, col3, col4, col5 = st.columns(5)
    # # 각 직종 키워드 선택 상태를 체크박스로 표시
    # with col1:
    #     st.session_state['search_word'][0] = st.checkbox('검색어 1', value=st.session_state['search_word'][0])
    # with col2:
    #     st.session_state['search_word'][1] = st.checkbox('검색어 2', value=st.session_state['search_word'][1])
    # with col3:
    #     st.session_state['search_word'][2] = st.checkbox('검색어 3', value=st.session_state['search_word'][2])
    # with col4:
    #     st.session_state['search_word'][3] = st.checkbox('검색어 4', value=st.session_state['search_word'][3])
    # with col5:
    #     st.session_state['search_word'][4] = st.checkbox('검색어 5', value=st.session_state['search_word'][4])