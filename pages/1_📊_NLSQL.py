import streamlit as st
import controller as ctrl
from random import randint
from controller import ( generate_questions_cached,
    generate_sql_cached,
    run_sql_cached,
    generate_plotly_code_cached,
    generate_plot_cached,
    generate_followup_cached,
)

ctrl.setup_agent()

"# Query showcase"

"Example questions :"
all_questions = ctrl.md.default_questions

# questions  = [all_questions[randint(0, len(all_questions)-1)] for _ in range(3)]

for i, quest in enumerate(all_questions):
    if st.button(quest, key=f"btn_question_exp{i}"):
        st.session_state["my_question"] = quest

question =  st.text_input(
    "Ask a personalized question" , key="my_question"
)

if st.session_state["my_question"]:
    sql = generate_sql_cached(
        question
    )
    "## SQL Query"
    st.code(sql, language='sql')

    "## Query output"
    df = run_sql_cached(sql)    
    st.dataframe(df, use_container_width=True)

    code = generate_plotly_code_cached(
            question=question,
            sql=sql,
            df=df)

    "## Charts based on query result"

    try:
        fig = generate_plot_cached(
            code=code,
            df=df)
        st.plotly_chart(fig, use_container_width=True)
    except ValueError:
        st.write("**[No chart can be rendered with this query result]**")
