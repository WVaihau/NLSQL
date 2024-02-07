import streamlit as st
import controller as ctrl
from controller import ( generate_questions_cached,
    generate_sql_cached,
    run_sql_cached,
    generate_plotly_code_cached,
    generate_plot_cached,
    generate_followup_cached,
)

ctrl.setup_agent()

question =  st.text_input(
    "Ask a question" , key="my_question"
)

if len(question) >= 10:
    sql = generate_sql_cached(
        question
    )

    st.code(sql, language='sql')

    df = run_sql_cached(sql)    
    st.dataframe(df, use_container_width=True)

    code = generate_plotly_code_cached(
            question=question,
            sql=sql,
            df=df)

    fig = generate_plot_cached(
        code=code, df=df)
    st.plotly_chart(fig, use_container_width=True)
