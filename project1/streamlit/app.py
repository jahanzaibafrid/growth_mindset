import streamlit as st

st.set_page_config(page_title="growth mint project",project_icon="★")
st.title("Growth Mindset Challenge: Web app with streamlit")

st.header("Wellcone to your growth journey!")
st.write("Embraced challenges")

# Quote section
st.header("💡 Today,s growth mindset Quote")
st.write("“Failure is simply the opportunity to begin again, this time more intelligently.” – Henry FordFailure is just a stepping stone to success. Keep going! 💪🔥")

st.header("what,s your challenge today")
user_input =st.text_input("describe a challenge your facing:")

# Condation
if user_input:
    st.success(f"you,r facing:{user_input}. keep pushing forword toword your goal!")

else:
    st.warning("Tell us about your challenge to get started!")

    # reflaxing
    st.header("reflect on your learning")
    reflection = st.text_area("write your leflection here:")

    if reflection:
        st.success(f"Great Insight! Your reflection: {reflection}")
    else:
        st.info("reflecting on past experince help you grow! Share your defficulties")

        # achivement
        st.header("Celebrate your Wins")
        achivement = st.text_input("share something you have recently accomplished")

        if achivement:
            st.success(f"Amazing you achived! {achivement}")
        else:
            st.info("Big or small every achivement count! share one now")

            # footer
            st.write("- - -")
            st.write("keep believeng on yourdelf. growth is a journey not a destination")
            st.write("Create by jahanzaib**")






