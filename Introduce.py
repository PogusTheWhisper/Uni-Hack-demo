import streamlit as st

st.title(":orange[Back To Hometown DEMO]")
st.caption('เป็นเกมแนว simmulation :green[ที่จะให้ผู้เล่นได้เล่นเกมผ่านการขยับร่างกาย] ออกกำลังกาย เซลฟี่กับสิ่งของ \n\n:red[ได้พูดคุยกับสัตว์เลี้ยง Ai สุดน่ารักที่จะคอยถามฮีลใจเราทุกครั้งที่เรา ทำภารกิจเสร็จ] :violet[โดยเกมๆนี้เราต้องการให้ผู้เล่นได้เติบโต]\n\n:violet[ไปพร้อมกันกับเกม]')
st.sidebar.success("Select a page above.")

a, b, c, d, e = st.columns(5)
with c:
    st.markdown(':blue[Member]')
    
st.image('mamber.png', width=640)
st.markdown("")
st.markdown("")

a, b, c, d, e = st.columns(5)
with c:
    st.markdown(':blue[Application]')
    
st.image('ui.png', width=640)