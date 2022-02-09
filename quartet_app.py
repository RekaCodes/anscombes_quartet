import streamlit as st
st.set_page_config(layout='wide')

import streamlit.components.v1 as cmp

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('seaborn')

import plotly.express as px
import plotly.graph_objects as go


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


    # sidebar
    st.sidebar.header('Version Selector')
    select_version = st.sidebar.selectbox(label='', options=['Select version:', 'Jupyter', 'Basic Viz', 'Advanced Viz'])
    st.sidebar.write("""
    ***Jupyter** with load the original notebook.*\n
    ***Basic Viz** loads a streamlit app using only built-in streamlit and matplotlib visualizations.*\n
    ***Advanced Viz** loads the streamlit app using interactive plotly visualizations.*
    
    """)
    if select_version=='Jupyter':
        # st.write('load jupyter notebook')
        html_file = open("quartet_notebook.html", 'r', encoding='utf-8')
        source_code = html_file.read()
        print(source_code)
        cmp.html(source_code, height=3200)

    elif select_version=='Basic Viz':
        # webpage title
        st.title("Anscombe's Quartet")
        st.write("*Illustrating the importance of data viz.* Made with `python` and `streamlit`.")
        st.write('___')


        # overview
        st.write("""
        ### Overview
        
        In 1973, English statistician Francis Anscombe created 'Anscombe's Quartet', a collection of four datasets each comprised of 11 (x,y) points. \
        The same year, an article in the *American Statistician* journal featuring this dataset describes Anscombe's intent as a counter to the industry impression at the time that "numerical calculations are exact, but graphs are rough." \n
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


    elif select_version=='Advanced Viz':
        # webpage title
        st.title("Anscombe's Quartet")
        st.write("*Illustrating the importance of data viz.* Made with `python` and `streamlit`.")
        st.write('___')


        # overview
        st.write("""
        ### Overview
        
        In 1973, English statistician Francis Anscombe created 'Anscombe's Quartet', a collection of four datasets each comprised of 11 (x,y) points. \
        The same year, an article in the *American Statistician* journal featuring this dataset describes Anscombe's intent as a counter to the industry impression at the time that "numerical calculations are exact, but graphs are rough." \n
        His construction of these datasets illustrates both the importance of data visualization as well as the effect of influential observations (such as outliers and duplicates) have on a dataset.""")


        #original data
        st.write("""
        ### Original Data
        The original datasets include (x,y) values that share very similar statistical properties. \
        In fact, the x-values for three of the four datasets are identical. \
        See the dataset below:""")

        fig_data = go.Figure(data=[go.Table(
            header=dict(values=list(data.columns),
                fill_color='powderblue',
                align='left'),
            cells=dict(values=data.values.T,
                fill_color='linen',
                align='left'))
            ])

        fig_data.update_layout(
            title='Raw Data',
            height=300,
            margin=dict(l=25, r=25, t=25, b=25)
        )
        st.write(fig_data)

        st.write("""
        We can get a better idea of the data by splitting the datasets and viewing the summary statistics for each set.
        
        """)


        # split datasets
        st.write("#### Datasets")

        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            fig_df1_data = go.Figure(data=[go.Table(
                header=dict(values=list(df1.columns),
                    fill_color='powderblue',
                    align='left'),
                cells=dict(values=df1.values.T,
                    fill_color='linen',
                    align='left'))
                ])

            fig_df1_data.update_layout(
                title='Dataset I',
                height=300,
                width=180,
                margin=dict(l=5, r=5, t=30, b=0)
            )
            st.write(fig_df1_data)


        with col2:
            fig_df2_data = go.Figure(data=[go.Table(
                header=dict(values=list(df2.columns),
                    fill_color='powderblue',
                    align='left'),
                cells=dict(values=df2.values.T,
                    fill_color='linen',
                    align='left'))
                ])

            fig_df2_data.update_layout(
                title='Dataset II',
                height=300,
                width=180,
                margin=dict(l=5, r=5, t=30, b=0)
            )
            st.write(fig_df2_data)


        with col3:
            fig_df3_data = go.Figure(data=[go.Table(
                header=dict(values=list(df3.columns),
                    fill_color='powderblue',
                    align='left'),
                cells=dict(values=df3.values.T,
                    fill_color='linen',
                    align='left'))
                ])

            fig_df3_data.update_layout(
                title='Dataset III',
                height=300,
                width=180,
                margin=dict(l=5, r=5, t=30, b=0)
            )
            st.write(fig_df3_data)


        with col4:
            fig_df4_data = go.Figure(data=[go.Table(
                header=dict(values=list(df4.columns),
                    fill_color='powderblue',
                    align='left'),
                cells=dict(values=df4.values.T,
                    fill_color='linen',
                    align='left'))
                ])

            fig_df4_data.update_layout(
                title='Dataset IV',
                height=300,
                width=180,
                margin=dict(l=5, r=5, t=30, b=0)
            )
            st.write(fig_df4_data)



        # summary statistics
        st.write("#### Summary Statistics")

        col5, col6, col7, col8 = st.columns(4)
        
        with col5:
            fig_df1_stats = go.Figure(data=[go.Table(
                header=dict(values=[""] + df1.describe().columns.tolist(),
                    fill_color='powderblue'),
                cells=dict(
                    values=df1.describe().reset_index().T.values,
                    fill_color=[['powderblue'], ['linen'], ['linen']],
                    align='left'
                    ))
                ])

            fig_df1_stats.update_layout(
                title='Dataset I',
                height=250,
                width=180,
                margin=dict(l=5, r=5, t=30, b=0)
            )
            st.write(fig_df1_stats)

        with col6:
            fig_df2_stats = go.Figure(data=[go.Table(
                header=dict(values=[""] + df2.describe().columns.tolist(),
                    fill_color='powderblue'),
                cells=dict(
                    values=df2.describe().reset_index().T.values,
                    fill_color=[['powderblue'], ['linen'], ['linen']],
                    align='left'
                    ))
                ])

            fig_df2_stats.update_layout(
                title='Dataset II',
                height=250,
                width=180,
                margin=dict(l=5, r=5, t=30, b=0)
            )
            st.write(fig_df2_stats) 
        with col7:
            fig_df3_stats = go.Figure(data=[go.Table(
                header=dict(values=[""] + df3.describe().columns.tolist(),
                    fill_color='powderblue'),
                cells=dict(
                    values=df3.describe().reset_index().T.values,
                    fill_color=[['powderblue'], ['linen'], ['linen']],
                    align='left'
                    ))
                ])

            fig_df3_stats.update_layout(
                title='Dataset III',
                height=250,
                width=180,
                margin=dict(l=5, r=5, t=30, b=0)
            )
            st.write(fig_df3_stats) 
        with col8:
            fig_df4_stats = go.Figure(data=[go.Table(
                header=dict(values=[""] + df4.describe().columns.tolist(),
                    fill_color='powderblue'),
                cells=dict(
                    values=df2.describe().reset_index().T.values,
                    fill_color=[['powderblue'], ['linen'], ['linen']],
                    align='left'
                    ))
                ])

            fig_df4_stats.update_layout(
                title='Dataset IV',
                height=250,
                width=180,
                margin=dict(l=5, r=5, t=30, b=0)
            )
            st.write(fig_df4_stats)
        
    
    # data viz
        st.write("""
        ### Data Visualization
        Based on the data and summary statistics, one may mistake these as being similar datasets. \
        However, when we see them visually, we see that they are completely different and tell very different stories.
        """)

        col9, col10 = st.columns(2)

        with col9:

            fig1 = px.scatter(
                    df1, x='x', y='y', trendline='ols', trendline_color_override='red', template='seaborn'
                )
            fig1.update_layout(
                title="Dataset I",
                width=300, 
                height=300,
                margin=dict(l=0, r=0, t=25, b=0),
                # paper_bgcolor='lightsteelblue'
                )
            fig1.update_xaxes(range=(0,20))
            fig1.update_yaxes(range=(0,20))
            st.plotly_chart(fig1)

            fig3 = px.scatter(
                df3, x='x', y='y', trendline='ols', trendline_color_override='red', template='seaborn'
            )
            fig3.update_layout(
                title="Dataset III",
                width=300, 
                height=300,
                margin=dict(l=0, r=0, t=25, b=0),
                )

            fig3.update_xaxes(range=(0,20))
            fig3.update_yaxes(range=(0,20))

            st.plotly_chart(fig3)

        with col10:

            fig2 = px.scatter(
                    df2, x='x', y='y', trendline='ols', trendline_color_override='red', template='seaborn'
                )
            fig2.update_layout(
                title="Dataset II",
                width=300, 
                height=300,
                margin=dict(l=0, r=0, t=25, b=0),
                )

            fig2.update_xaxes(range=(0,20))
            fig2.update_yaxes(range=(0,20))

            st.plotly_chart(fig2)


            fig4 = px.scatter(
                    df4, x='x', y='y', trendline='ols', trendline_color_override='red', template='seaborn'
                )
            fig4.update_layout(
                title="Dataset IV",
                width=300, 
                height=300,
                margin=dict(l=0, r=0, t=25, b=0),
                )

            fig4.update_xaxes(range=(0,20))
            fig4.update_yaxes(range=(0,20))

            st.plotly_chart(fig4)


        # summary
        st.write("""
        #### Summary
        At first glance, the original data looks incredibly similar (remember the x-values are *identical* in three of the four). \
        Even the summary statistics show nearly identical values.\n
        However, when we visualize the data that we see how different the datasets are from one another. \
        It is only then that we see each tells its own very different story.

        """)
    else:
        st.header('Getting Started')
        st.write('Select a version in the sidebar to get started.')

    


if __name__ == '__main__':
    main()