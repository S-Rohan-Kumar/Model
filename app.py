import streamlit as st
import preprocess
import helper
import matplotlib.pyplot as plt

# Upload the file through the Streamlit sidebar
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # Read files as bytes
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")

    # Show the uploaded data as text


    # Process the data using the prepros function
    df = preprocess.prepros(data)
    user=df["sender"].unique().tolist()
    user.remove("Meta AI")
    user.sort()
    user.insert(0,"Overall")
    selected=st.sidebar.selectbox("show analysis wrt",user)
    if st.sidebar.button("SHOW ANALYSIS"):
        number_msg,num_words,num_media,num_link=helper.help_to_fetch(selected,df)
        total_words=len(num_words)
        col1,col2,col3,col4=st.columns(4)
        with col1:
            st.header("TOTAL MESSAGES")
            st.title(number_msg)
        with col2:
            st.header("TOTAL WORDS")
            st.title(total_words)
        with col3:
            st.header("TOTAL MEDIA")
            st.title(num_media)
        with col4:
            st.header("TOTAL LINK")
            st.title(num_link)
        st.dataframe(df)

        # if selected=="Overall":
        st.title("MOST BUSY USERS")
        graph, newtabel = helper.most_busy_users(df)

        col1, col2 = st.columns(2)
        with col1:
            fig = plt.figure()
            plott = fig.add_axes([0, 0, 1, 1])
            plott.bar(graph.index, graph.values, color="red")
            plt.xticks(rotation="vertical")
            st.pyplot(fig)

        with col2:
            st.dataframe(newtabel)

        # if selected=="Overall":
        st.title("WORDCLOUD")
        col1, = st.columns(1)
        with col1:
            pic = helper.create_word_cloud(selected, df)
            fig = plt.figure()
            plott = fig.add_axes([0, 0, 1, 1])
            plott.imshow(pic)
            st.pyplot(fig)







    # Display the processed DataFrame in Streamlit
