import streamlit as st

def load_selected_welfare():
    selected_welfare = []
    for item in st.session_state['welfare']:
        selected_welfare.append(item)
    ####사용자가 입력한 기타 복지를 쉼표로 나눠서 추가
    if st.session_state['other_welfare']:
        other_welfare_list = [w.strip() for w in other_welfare.split(',')]
        for welfare_item in other_welfare_list:
            if welfare_item and welfare_item not in welfare:
                selected_welfare.append(welfare_item)

    return selected_welfare

def load_selected_recruitment():
    selected_recruitment = []
    for item in st.session_state['recruitment']:
        selected_recruitment.append(item)
    ####사용자가 입력한 기타 복지를 쉼표로 나눠서 추가
    if st.session_state['other_recruitment']:
        other_recruitment_list = [w.strip() for w in other_recruitment.split(',')]
        for recruitment_item in other_recruitment_list:
            if recruitment_item and recruitment_item not in recruitment:
                selected_recruitment.append(recruitment_item)
    return selected_recruitment

def generate_checkbox_section(title, session_key, labels):
    st.markdown(f"<h4 style='font-weight: bold;'>{title}</h4>", unsafe_allow_html=True)
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.session_state[session_key][i] = st.checkbox(labels[i], value=st.session_state[session_key][i])
