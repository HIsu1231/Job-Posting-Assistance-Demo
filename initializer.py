from datetime import datetime
import streamlit as st

def initialize_session_state():
    if 'job_title' not in st.session_state:
        st.session_state['job_title'] = ""
    if "job_description" not in st.session_state:
        st.session_state.job_description = ""
    if "job_description_result" not in st.session_state:
        st.session_state.job_description_result = ""
    if 'job_role' not in st.session_state:
        st.session_state.job_role = [False, False, False, False, False]
    if 'job_certification' not in st.session_state:
        st.session_state.job_certification = [False, False, False, False, False]
    if 'job_category' not in st.session_state:
        st.session_state.job_category = [False, False, False, False, False]
    if 'job_keyword' not in st.session_state:
        st.session_state.job_keyword = [False, False, False, False, False]
    if 'license' not in st.session_state:
        st.session_state.license = [False, False, False, False, False]
    if 'search_word' not in st.session_state:
        st.session_state.search_word = [False, False, False, False, False]
    if 'welfare' not in st.session_state:
        st.session_state.welfare = []
    if 'other_welfare' not in st.session_state:
        st.session_state.other_welfare = ""
    if 'selected_welfare' not in st.session_state:
        st.session_state.selected_welfare = []
    if 'recruitment' not in st.session_state:
        st.session_state.recruitment = []
    if 'other_recruitment' not in st.session_state:
        st.session_state.other_recruitment = ""
    if 'selected_recruitment' not in st.session_state:
        st.session_state.selected_recruitment = []
    if 'keyword_generation' not in st.session_state:
        st.session_state.keyword_generation = False
    if 'business_registration_number' not in st.session_state:
        st.session_state.business_registration_number = ""
    if 'job_description' not in st.session_state:
        st.session_state.job_description = ""
    if 'draft_generation' not in st.session_state:
        st.session_state.draft_generation = False
    if 'work_place' not in st.session_state:
        st.session_state['work_place'] = ""
    if 'salary_min' not in st.session_state:
        st.session_state['salary_min'] = 0
    if 'salary_max' not in st.session_state:
        st.session_state['salary_max'] = 0
    if 'experience' not in st.session_state:
        st.session_state['experience'] = "신입"
    if 'year_of_experience_min' not in st.session_state:
        st.session_state['year_of_experience_min'] = 0
    if 'year_of_experience_max' not in st.session_state:
        st.session_state['year_of_experience_max'] = 0
    if 'publication' not in st.session_state:
        st.session_state['publication'] = "바로 게시"
    if 'date_of_publication' not in st.session_state:
        st.session_state['date_of_publication'] = ""
    if 'Deadline' not in st.session_state:
        st.session_state['Deadline'] = "상시"
    if 'deadline_date' not in st.session_state:
        st.session_state['deadline_date'] = datetime.now().date()
    if 'braincore' not in st.session_state:
        st.session_state['braincore'] = ""
    if 'text' not in st.session_state:
        st.session_state['text'] = ""
        st.session_state["job_category_text"] = ""
        st.session_state['job_role_text'] = ""
        st.session_state['company_introduction_text'] = ""
        st.session_state['major_task_text'] = ""
        st.session_state['qualification_requirements_text'] = ""
        st.session_state['benefits_and_welfare_text'] = ""
        st.session_state['recruitment_text'] = ""
        st.session_state['skill_text'] = ""

    # Define lists as well
    welfare_list = ["자율출퇴근제", "유연 근무제", "건강 검진 및 의료 지원", "자기 개발 지원 프로그램", "사내 동호회 및 문화 활동 지원"]
    recruitment_list = ["서류 전형", "1차 면접", "2차 면접", "실무진 면접", "입원 면접", "코딩테스트", "최종 합격"]

    return welfare_list, recruitment_list

def load_custom_styles():
    styles = """
    <style> 
        .custom-button {
            background-color: white; /* 버튼 배경색 */ 
            color: #007BFF; /* 버튼 글자색 (파란색) */
            border: 2px solid #007BFF; /* 테두리 색상 및 두께 */ 
            padding: 4px 18px; /* 버튼 안쪽 여백 */
            border-radius: 8px; /* 테두리 둥글기 정도 */  
            cursor: pointer; /* 마우스 커서 모양 */
            font-size: 12px; /* 글자 크기 */ 
        }
        .custom-button:hover {
            background-color: #007BFF; /* 호버 시 배경색 (파란색) */  
            color: white; /* 호버 시 글자색 (흰색) */ 
        }
        .custom-label {
            font-size: 14px;  /* 폰트 크기 */ 
            font-weight: 400; /* 폰트 굵기 */
            color: #6e6e6e;   /* 기본 Streamlit 레이블 색상 */ 
            margin-bottom: 2px; /* 아래쪽 마진을 줄여서 간격을 조정 (2px) */
            display: block;   /* 블록 레벨 요소로 변경 */ 
        }
        div.stButton > button {
            font-size: 100px;
            padding: 10px 20px;
            width: 100%; /* 버튼을 가로로 꽉 채움 */  
        }
        .small-text {
            font-size: 12px; /* 글자 크기 조정 */
            white-space: nowrap; /* 줄바꿈 방지 */
            color: #666666; /* 필요시 글자 색상 변경 */
        }
    </style>
    """
    return styles

def load_braincore1():
    st.session_state['braincore'] = """                주식회사 브레인코어는 AI 교육과 에듀테크 분야에서 앞서 나가는 혁신적인 기업입니다. 
                우리는 성인과 청소년을 대상으로 인공지능 교육 프로그램을 개발하고 제공하며, 이를 통해 AI 기술의 대중화를 촉진하고 있습니다.

                * 인공지능 교육 프로그램 개발: 다양한 연령대의 학습자를 위한 맞춤형 AI 교육 콘텐츠를 제공합니다.
                * 에듀테크 솔루션 제공: 기술 기반의 교육 솔루션을 통해 학습 효율성을 극대화합니다.
                * 유연한 근무 환경: 자율출퇴근제를 포함한 직원 복지를 강화하여 창의적이고 자율적인 업무 환경을 조성합니다."""
    st.session_state["job_title"] = "AI 교육의 미래를 이끌어갈 초·중등 인공지능 강사 모집"
    job_categories = ['AI 교육 강사', '에듀테크 콘텐츠 개발자', '교육 프로그램 기획자', 'AI 튜터/멘토', '교육 솔루션 개발자']
    job_roles = ['교육사업 기획.운영', '이러닝교육과정운영', '교육서비스운영', '인재교육', '교육과정 개발ㆍ강의']
    job_certification = ['인공지능산업기사', '빅데이터분석기사', '정보처리기사', '코딩지도사', 'GTQ 자격증']
    job_keywords = ['인공지능 교육', '초·중등 교육', '강사 모집', '교통비 및 교재 지원', '수업 시연 전형']
    return job_categories, job_roles, job_certification, job_keywords

def load_braincore2():
    st.session_state['company_introduction_text'] = """            주식회사 브레인코어는 초·중등 학생들을 대상으로 인공지능(AI) 교육을 기획하고 진행할 유능한 강사를 모집하고 있습니다.
            이 직무는 학생들이 인공지능 기술을 이해하고 실생활에 응용할 수 있도록 돕는 역할을 담당합니다. 
            주 강의 대상은 초·중등 학생으로, AI 기초 개념부터 실제 프로그래밍까지 체계적인 교육을 진행하며,
            교육 커리큘럼에 맞춘 수업 자료, 교재, 교구재를 준비하게 됩니다. 
            학생들의 학습 수준을 고려하여 맞춤형 수업을 설계하고, 학습 성과를 평가해 효과적인 피드백을 제공합니다.  
            인공지능 교육 트렌드에 맞춰 최신 기술을 반영하여 학생들이 보다 쉽게 AI에 접근할 수 있도록 돕습니다. 
            교육 경력 및 AI 도구 사용 경험을 보유한 분을 우대하며, 창의적인 수업 방식과 원활한 소통 능력도 중요한 자질입니다. 
            다양한 혜택으로는 교통비 지원, 교재 제공, 자율적인 수업 준비 시간, 그리고 교육 관련 세미나 및 워크숍 참여 기회 등이 제공됩니다."""
    st.session_state['major_task_text'] = """            * 초·중등 학생을 대상으로 한 인공지능 교육 기획 및 진행
            * 교육 커리큘럼에 맞춘 수업 자료, 교재 및 교구재 준비
            * 학생들의 이해도를 고려한 맞춤형 수업 설계 및 운영
            * 학생들의 학습 성과에 대한 평가 및 피드백 제공
            * 인공지능 관련 최신 기술 및 교육 트렌드에 대한 정보 업데이트 및 반영"""
    st.session_state['qualification_requirements_text'] = """            * 교육 관련 경력 및 초·중등 학생 대상 수업 경험
            * 인공지능 또는 컴퓨터 과학 분야 전공자 또는 관련 자격증 보유자
            * 파이썬(Python) 및 AI 도구를 활용한 수업 경험
            * 창의적이고 학생 중심의 수업 방식에 대한 이해
            * 원활한 소통 및 협업 능력"""
    st.session_state['benefits_and_welfare_text'] = """            * 강의장까지 교통비 지원: 강의 장소와 거리에 상관없이 교통비 전액 지원
            * 교재 및 교구재 지원: 강의에 필요한 모든 교재 및 교구재 제공
            * 자율적인 수업 준비 시간 및 유연한 일정 조정 가능
            * 교육 관련 세미나 및 워크숍 참여 기회 제공 """
    st.session_state['recruitment_text'] = """            * 서류 전형: 제출된 이력서 및 자기소개서를 기반으로 평가
            * 면접: 직무 적합성 및 인성 면접
            * 수업 시연: 실제 교육을 진행하는 방식에 대한 시연 및 피드백 제공
            * 최종 합격: 조건 협의 후 입사"""
    st.session_state['skill_text'] = """            * 프로그래밍 언어: Python (기본 AI 프로그래밍)
            * 교육 도구: 다양한 AI 교육 플랫폼 및 도구 (Scratch, 구글 Colab 등)
            * 협업 및 관리 도구: Slack, Google Drive, Zoom (원격 교육 시) """