from unicodedata import name
import streamlit as st
st.set_page_config(layout='wide')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('seaborn')

import plotly.express as px


def main():

    # data
    @st.cache
    def load_data():
        data = pd.read_csv('Anscombe_quartet_data.csv')
        return data

    data = load_data()

    df1 = data[['x123', 'y1']]
    df1.columns=['x', 'y']

    df2 = data[['x123', 'y2']]
    df2.columns=['x', 'y']

    df3 = data[['x123', 'y3']]
    df3.columns=['x', 'y']

    df4 = data[['x4', 'y4']]
    df4.columns=['x', 'y']

    df = pd.concat([df1, df2, df3, df4], axis=1, keys=["I", "II", "III", "IV"])


    # webpage title
    st.title("Anscombe's Quartet")
    st.write("*Illustrating the importance of data viz.* Made with `python` and `streamlit`.")
    st.write('___')


    # overview
    st.write("""
    ### Overview
    
    In 1973, English statistician Francis Anscombe created 'Anscombe's Quartet', a collection of four datasets each comprised of 11 (x,y) points. \
    An article in the *American Statistician* joural featuring this dataset describes Anscombe's intent as a counter to the industry impression at the time that "numerical calculations are exact, but graphs are rough." \n
    His construction of these datasets illustrates both the importance of data visualization as well as the effect of influential observations (such as outliers and duplicates) have on a dataset.""")

    # original data
    st.write("""
    ### Original Data
    The original datasets inclue (x,y) values that share very similar statistical properties. \
    In fact, the x-values for three of the four datasets are identical. \
    See the dataset below:
    """)

    st.dataframe(data, width = 600, height=600)

    st.write("""
    We can get a better idea of the data by splitting the datasets and viewing the summary statistics for each set.""")


    # split datasets
    st.write("##### Datasets")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write('**Dataset I**')
        st.dataframe(df1, height=400)

    with col2:
        st.write('**Dataset II**')
        st.dataframe(df2, height=400)

    with col3:
        st.write('**Dataset III**')
        st.dataframe(df3, height=400)

    with col4:
        st.write('**Dataset IV**')
        st.dataframe(df4, height=400)


    # summary statistics
    st.write('##### Summary Statistics')

    col5, col6, col7, col8 = st.columns(4)
    with col5:
        st.write('**Dataset I**')
        st.dataframe(df1.describe())

    with col6:
        st.write('**Dataset II**')
        st.dataframe(df2.describe())

    with col7:
        st.write('**Dataset III**')
        st.dataframe(df3.describe())

    with col8:
        st.write('**Dataset IV**')
        st.dataframe(df4.describe())


    # data viz
    st.write("""
    ### Data Visualization
    Based on the data and summary statistics, one may mistake these as being similar datasets. \
    However, when we see them visually, we see that they are completely different and tell very different stories.
    """)

    fig, axes = plt.subplots(2, 2)

    axes[0,0].set_title('Dataset I', fontsize=14)
    axes[0,0].scatter(x=df1.x, y=df1.y)

    axes[0,1].set_title('Dataset II', fontsize=14)
    axes[0,1].scatter(x=df2.x, y=df2.y)

    axes[1,0].set_title('Dataset III', fontsize=14)
    axes[1,0].scatter(x=df3.x, y=df3.y)

    axes[1,1].set_title('Dataset IV', fontsize=14)
    axes[1,1].scatter(x=df4.x, y=df4.y)

    fig.tight_layout()
    st.pyplot(fig)


    # summary
    st.write("""
    #### Summary
    At first, the original data looks incredibly similar (remember the x-values are *identical* in three of the four). \
    Even the summary statistics show nearly identical values.\
    It is only when we visualize the data that we see how different the datasets are from one another. \
    It is only then that we see each tells its own very different story.

    """)



if __name__ == '__main__':
    main()