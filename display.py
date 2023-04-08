import streamlit as st
import matplotlib.pyplot as plt
import report as rp


def showing_the_chart_at_streamlit():
    # create a bar chart
    plt.bar(rp.brands_dict.keys(), rp.brands_dict.values())
    plt.title("Brand Mentions in Sentences")
    plt.xlabel("Brand Name")
    plt.ylabel("Count")

    # return the plot as a PNG image
    fig = plt.gcf()
    fig.set_size_inches(16, 8)
    plt.close()
    return fig


# create the Streamlit app
st.title("Brand Mentions in Sentences")

if st.button("Show Brand Analytics"):
    st.pyplot(showing_the_chart_at_streamlit())
