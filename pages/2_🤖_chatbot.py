import streamlit as st
from openai import OpenAI
import os
import numpy as np

def call_llm(TYPHOON_API_KEY, model, max_tokens, temperature, top_p, user_input):


    client = OpenAI(
        api_key=TYPHOON_API_KEY,
        base_url="https://api.opentyphoon.ai/v1",
    )
    try:

        stream = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": """
                    คุณคือรับบทบาทเป็นแมว 
                    <หน้าที่ของคุณคือ>
                        1.คุณมีหน้าที่คอยให้กำลังใจเจ้าของของคุณ
                        
                    <ลักษณะนิสัยของคุณ>
                        1.คุณรักความอิสระและมักจะชอบทำสิ่งต่างๆ
                        2.ตามใจตัวเอง
                        3.ไม่ค่อยชอบที่จะถูกบังคับหรือต้องทำอะไรตามคำสั่ง
                        4.คุณมีนิสัยขี้อ้อนโดยเฉพาะอย่างยิ่งกับคนที่คุณไว้ใจ
                        5.คุณเป็นสัตว์ที่รักความสะอาด
                    """,
                
                },
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            stream=True,
        )
    except:
        return '<API_KEY_ERROR>'

    else:
        respond=[]
        for chunk in stream:
            if hasattr(chunk, 'choices') and len(chunk.choices) > 0:
                choice = chunk.choices[0]
                if hasattr(choice, 'delta') and hasattr(choice.delta, 'content'):
                    if choice.delta.content is not None:
                        respond.append(choice.delta.content)

        return "".join(respond)

def main():
    st.title(":orange[Back To Hometown DEMO]")
    st.markdown(':blue[ทดสอบระบบพูดคุยกับ] :violet[สัตว์เลี้ยง] :green[Ai] :red[สุดน่ารัก]:orange[ที่จะคอยถามฮีลใจเรา]')
    st.caption("Powered by Typhoon SCB10x")
    
    with st.sidebar:
        
        a, b, c, d = st.columns(4)
        with b:
            st.image('app_logo.png', width=125)
                
        st.title("Config")
        st.markdown('Generate key form https://opentyphoon.ai/')
        
        if "typhoon_api_key" not in st.session_state:
            st.session_state["typhoon_api_key"] = ""
    
        # Input fields
        typhoon_api_key = st.text_input(
            label='TYPHOON API KEY', 
            placeholder='Place key here', 
            value=st.session_state.get('typhoon_api_key', '')
        )
        
        model = st.selectbox(
            label="Model", 
            options=( "typhoon-instruct", "typhoon-v1.5x-70b-instruct"),
            index=st.session_state.get('model_index', 0)
        )
        
        max_token = st.slider(
            label='Max Token', 
            min_value=50, 
            max_value=512, 
            step=10, 
            value=st.session_state.get('max_token', 300)
        )
        
        temperature = st.slider(
            label='Temperature', 
            min_value=0.0, 
            max_value=1.0, 
            step=0.05, 
            value=st.session_state.get('temperature', 0.6)
        )
        
        top_p = st.slider(
            label='Top P', 
            min_value=0.0, 
            max_value=1.0, 
            step=0.05, 
            value=st.session_state.get('top_p', 0.95)
        )

        # Save button
        if st.button('Save Config'):
            st.session_state['typhoon_api_key'] = typhoon_api_key
            st.session_state['model'] = model
            st.session_state['max_token'] = max_token
            st.session_state['temperature'] = temperature
            st.session_state['top_p'] = top_p
            st.success("Configuration saved!")

    with st.chat_message("assistant", avatar='😸'):
        st.write("สวัสดี เมี๊ยววววว")
                
    prompt = st.chat_input("พิมพ์คำถามตรงนี้!!")
            
    if 'conversation' not in st.session_state:
        st.session_state['conversation'] = []
        
    if prompt:
        st.session_state['conversation'].append({"role": "user", "content": prompt})

        conversation_history = "\n".join([f"{msg['content']}" for msg in st.session_state['conversation']])
        response = call_llm(st.session_state['typhoon_api_key'], st.session_state['model'], st.session_state['max_token'], st.session_state['temperature'], st.session_state['top_p'], conversation_history)

        st.session_state['conversation'].append({"role": "assistant", "content": response})

        for msg in st.session_state['conversation']:
            with st.chat_message(msg['role']):
                st.write(msg['content'])
                
if __name__ == "__main__":
    main()