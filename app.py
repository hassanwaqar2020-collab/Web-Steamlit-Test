import streamlit as st

st.title("Weather AI Agent")
st.write("Step 1: Streamlit loaded")

try:
    from weather_agent import agent
    st.success("Step 2: weather_agent imported successfully")
except Exception as e:
    st.error(f"Import error: {e}")
    st.stop()

st.write("Step 3: Agent is ready")

question = st.text_input(
    "Enter your question",
    placeholder="What is the weather in Lahore?"
)

if st.button("Ask Weather Agent"):
    if question:
        st.write("Calling agent...")

        try:
            result = agent.invoke({
                "messages": [
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            })

            response = result["messages"][-1]

            for block in response.content:
                if block["type"] == "text":
                    st.write(block["text"])

        except Exception as e:
            st.error(f"Agent error: {e}")