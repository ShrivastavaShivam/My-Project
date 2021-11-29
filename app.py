from pandas.io.parsers import read_csv
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


st.title("Indian School Education Analysis")
st.sidebar.header("Analyse...")

# load datasets
@st.cache
def ld_enrol():
    enrolment = read_csv("gross-enrollment-ratio-from-2013-2016.csv")
    return enrolment

@st.cache
def ld_comps():
    comps=pd.read_csv("percentage-of-schools-with-comps-from-2013-2016.csv")
    return comps

@st.cache
def ld_elect():
    electricity=pd.read_csv("percentage-of-schools-with-electricity-from-2013-2016.csv")
    return electricity

@st.cache
def ld_water():
    water=pd.read_csv("percentage-of-schools-with-drinking-water-facility-from-2013-2016.csv")
    return water

@st.cache
def ld_bt():
    boys_toilet=pd.read_csv("schools-with-boys-toilet-from-2013-2016.csv")
    return boys_toilet

@st.cache
def ld_gt():
    girls_toilet=pd.read_csv("schools-with-girls-toilet-from-2013-2014.csv")
    return girls_toilet

# calling function
enrolment = ld_enrol()
elec = ld_elect()
wtr = ld_water()
com  = ld_comps()
b_t = ld_bt()
g_t = ld_gt()


options = st.sidebar.selectbox('Choose Attribute', ['About Project', 'Gross Dropout Ratio (State-wise)',
                                 'Gross Enrolment Ratio', 'Facilities (in percentge)'])

if options == 'About Project':
    st.image("about_img.jpg")
    st.header("About the project")
    st.markdown('''This dataset contains information about Indian School Education Statistics of the 
    year 2013-2014 to 2015-2016. Many public datasets from Indian Government are scattered and 
    the goal here is to have all those datasets under one umbrella so that it is easy for beginners 
    to find important datasets like this to start their Data Science journey.
    ''')
if options == 'Gross Dropout Ratio (State-wise)':
    GDRatio = st.sidebar.selectbox('Choose Facility', ["Electricity", "Water", 
                                            "Computers", "Boys Toilet", "Girls Toilet"])
    color = st.sidebar.color_picker("Select Graph Color..")

    if GDRatio == 'Electricity':
        fig,ax = plt.subplots()
        elec.groupby('State_UT')['All Schools'].mean().plot(kind='bar',color = color,
                                                            figsize=(10,5),ylabel= 'Mean')
        st.pyplot(fig)
    if GDRatio == 'Water':
        fig,ax = plt.subplots()
        wtr.groupby('State/UT')['All Schools'].mean().plot(kind='bar',color = color,
                                                            figsize=(10,5),ylabel= 'Mean')
        st.pyplot(fig)
    if GDRatio == 'Computers':
        fig,ax = plt.subplots()
        com.groupby('State_UT')['Primary_Only'].mean().plot(kind='bar',color = color,
                                                            figsize=(10,5),ylabel= 'Mean')
        st.pyplot(fig)
    if GDRatio == 'Boys Toilet':
        fig,ax = plt.subplots()
        b_t.groupby('State_UT')['All Schools'].mean().plot(kind='bar',color = color,
                                                            figsize=(10,5),ylabel= 'Mean')
        st.pyplot(fig)
    if GDRatio == 'Girls Toilet':
        fig,ax = plt.subplots()
        g_t.groupby('State_UT')['All Schools'].mean().plot(kind='bar',color = color,
                                                            figsize=(10,5),ylabel= 'Mean')
        st.pyplot(fig)

if options == 'Gross Enrolment Ratio':
    GERatio = st.sidebar.selectbox('Choose Option', ["Boys in India", "Girls in India", 
                                            "Highest GER in Primary", "Highest GER in Secondary", 
                                            "Lowest GER in Primary", "Lowest GER in Secondary"])
    color = st.sidebar.color_picker("Select Graph Color..")
    if GERatio == 'Boys in India':
        enrolment.sort_values(by='Year',inplace=True)
        filt1 = enrolment.index =='All India'
        df_gre_total = enrolment.loc[filt1]
        boys_col = ['Primary_Boys','Upper_Primary_Boys','Secondary_Boys','Higher_Secondary_Boys']
        #girls_col = ['Primary_Girls','Upper_Primary_Girls','Secondary_Gistreamlit run frontend_2rls','Higher_Secondary_Girls']
        df_gre_total.loc[:,'Higher_Secondary_Boys'] = df_gre_total.loc[:,'Higher_Secondary_Boys'].astype('float')
        df_gre_total.loc[:,'Higher_Secondary_Girls'] = df_gre_total.loc[:,'Higher_Secondary_Girls'].astype('float')
        sns.set(font_scale = 1.11)
        sns.set_style("white")
        fig, ax = plt.subplots(figsize=(15,6))
        df_gre_total[boys_col].plot.bar(ax=ax)
        sns.despine(left=True, bottom=True)
        ax.set_xticklabels(np.arange(3))
        ax.set_title('Gross Enrollment Ratio of Boys in India',size=18)
        ax.set_xticklabels(list(df_gre_total['Year']))
        for tick in ax.get_xticklabels():
            tick.set_rotation(-0)
        for p in ax.patches:
            ax.annotate(format(p.get_height(), '.2f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   xytext = (0, 9), 
                   textcoords = 'offset points')
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),ncol=4)
        st.pyplot(fig)
    
    if GERatio == 'Girls in India':
        enrolment.sort_values(by='Year',inplace=True)
        filt1 = enrolment.index =='All India'
        df_gre_total = enrolment.loc[filt1]
        #boys_col = ['Primary_Boys','Upper_Primary_Boys','Secondary_Boys','Higher_Secondary_Boys']
        girls_col = ['Primary_Girls','Upper_Primary_Girls','Secondary_Girls','Higher_Secondary_Girls']
        df_gre_total.loc[:,'Higher_Secondary_Boys'] = df_gre_total.loc[:,'Higher_Secondary_Boys'].astype('float')
        df_gre_total.loc[:,'Higher_Secondary_Girls'] = df_gre_total.loc[:,'Higher_Secondary_Girls'].astype('float')
        sns.set(font_scale = 1.11)
        sns.set_style("white")
        fig, ax = plt.subplots(figsize=(15,6))
        df_gre_total[girls_col].plot.bar(ax=ax)
        sns.despine(left=True, bottom=True)
        ax.set_xticklabels(np.arange(3))
        ax.set_title('Gross Enrollment Ratio of Girls in India',size=18)
        ax.set_xticklabels(list(df_gre_total['Year']))
        for tick in ax.get_xticklabels():
            tick.set_rotation(-0)
        for p in ax.patches:
            ax.annotate(format(p.get_height(), '.2f'), 
                        (p.get_x() + p.get_width() / 2., p.get_height()), 
                        ha = 'center', va = 'center', 
                        xytext = (0, 9), 
                        textcoords = 'offset points')
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),ncol=4)
        st.pyplot(fig)
        
    if GERatio == 'Highest GER in Primary':
        filt_year = enrolment['Year'] =='2015-16'
        df_enroll_latest = enrolment[filt_year]
        df_enroll_latest.sort_values(by='Higher_Secondary_Total',ascending=False,inplace=True)
        df_enroll_latest['Higher_Secondary_Total'] = df_enroll_latest['Higher_Secondary_Total'].astype('float')
        #st.write(df_enroll_latest)
        sns.set_style("white")
        fig,ax = plt.subplots(figsize=(20,6))
        ax = sns.barplot(x= df_enroll_latest.index, y="Primary_Total",palette='Purples_r',
                        data=df_enroll_latest.sort_values(by='Primary_Total',ascending=False))
        sns.despine(left=True, bottom=True)
        for item in ax.get_xticklabels():
            item.set_rotation(90)
            item.set_fontsize(12)
        ax.set_xlabel('')
        ax.set_ylabel('Higher Secondary GRE')
        for p in ax.patches:
            ax.annotate(format(p.get_height(), '.2f'), 
                        (p.get_x() + p.get_width() / 2., p.get_height()), 
                        ha = 'center', va = 'center', 
                        xytext = (0, 9), 
                        textcoords = 'offset points')


        fig.suptitle('Sates with highest Gross Enrolment Ratio in Primary', fontsize=18)
        st.pyplot(fig)

    if GERatio == 'Highest GER in Secondary':
        filt_year = enrolment['Year'] =='2015-16'
        df_enroll_latest = enrolment[filt_year]
        df_enroll_latest.sort_values(by='Higher_Secondary_Total',ascending=False,inplace=True)
        df_enroll_latest['Higher_Secondary_Total'] = df_enroll_latest['Higher_Secondary_Total'].astype('float')
        fig,ax = plt.subplots(figsize=(15,6))
        sns.set_style("white")
        ax = sns.barplot(x= df_enroll_latest.index, y="Higher_Secondary_Total",palette='Reds_r',
                        data=df_enroll_latest)
        sns.despine(left=True, bottom=True)
        for item in ax.get_xticklabels():
            item.set_rotation(90)
            item.set_fontsize(12)
        ax.set_xlabel('')
        ax.set_ylabel('Higher Secondary GRE')
        for p in ax.patches:
            ax.annotate(format(p.get_height(), '.2f'), 
                        (p.get_x() + p.get_width() / 2., p.get_height()), 
                        ha = 'center', va = 'center', 
                        xytext = (0, 9), 
                        textcoords = 'offset points')
        fig.suptitle('Sates with highest GER in Higher Secondary', fontsize=22)
        st.pyplot(fig)
    
    if GERatio == 'Lowest GER in Primary':
        filt_year = enrolment['Year'] =='2015-16'
        df_enroll_latest = enrolment[filt_year]
        df_enroll_latest.sort_values(by='Higher_Secondary_Total',ascending=False,inplace=True)
        df_enroll_latest['Higher_Secondary_Total'] = df_enroll_latest['Higher_Secondary_Total'].astype('float')
        fig,ax = plt.subplots(figsize=(15,6))
        sns.set_style("white")
        ax = sns.barplot(x= df_enroll_latest.index, y="Primary_Total",palette='Purples',
                        data=df_enroll_latest.sort_values(by='Primary_Total',ascending=False)[::-1])
        sns.despine(left=True, bottom=True)

        for item in ax.get_xticklabels():
            item.set_rotation(90)
            item.set_fontsize(12)
        ax.set_xlabel('')
        ax.set_ylabel('Higher Secondary GRE')

        for p in ax.patches:
            ax.annotate(format(p.get_height(), '.2f'), 
                        (p.get_x() + p.get_width() / 2., p.get_height()), 
                        ha = 'center', va = 'center', 
                        xytext = (0, 9), 
                        textcoords = 'offset points')

        fig.suptitle('Sates with lowest Gross Enrolment Ratio in Primary', fontsize=22)
        st.pyplot(fig)

    if GERatio == 'Lowest GER in Secondary':    
        filt_year = enrolment['Year'] =='2015-16'
        df_enroll_latest = enrolment[filt_year]
        df_enroll_latest.sort_values(by='Higher_Secondary_Total',ascending=False,inplace=True)
        df_enroll_latest['Higher_Secondary_Total'] = df_enroll_latest['Higher_Secondary_Total'].astype('float')
        fig,ax = plt.subplots(figsize=(15,6))
        sns.set_style("white")
        ax = sns.barplot(x= df_enroll_latest.index, y="Higher_Secondary_Total",palette='Reds',
                        data=df_enroll_latest[::-1])
        sns.despine(left=True, bottom=True)
        for item in ax.get_xticklabels():
            item.set_rotation(90)
            item.set_fontsize(12)
        ax.set_xlabel('')
        ax.set_ylabel('Higher Secondary GRE')
        for p in ax.patches:
            ax.annotate(format(p.get_height(), '.2f'), 
                        (p.get_x() + p.get_width() / 2., p.get_height()), 
                        ha = 'center', va = 'center', 
                        xytext = (0, 9), 
                        textcoords = 'offset points')
        fig.suptitle('Sates with lowest Gross Enrolment Ratio in Higher Secondary', fontsize=22 ) 
        st.pyplot(fig)

if options == 'Facilities (in percentge)':
    Faci = st.sidebar.selectbox('Choose Option', ["Water", "Electricity", 
                                            "Computers", "Boys/Girls Toilet"])
    
    if Faci == 'Water':
        water_columns = ['State/UT','Year','Primary_Only','U_Primary_Only','Sec_Only','HrSec_Only']
        water_ai = wtr.loc[:,water_columns]
        tidy_water = pd.melt(water_ai,id_vars=['Year','State/UT']).rename(columns=str.title)
        sns.set(style="ticks",context="talk")
        plt.style.use('seaborn-deep')
        f, axes = plt.subplots(1, 1, figsize=(20, 10))
        # barplot for water facility
        water_bplot = sns.barplot(x="Year",y='Value',hue='Variable',data=tidy_water,palette = 'ocean',edgecolor='black',ax=axes)
        water_bplot.set(ylim=(0, 150))
        for p in water_bplot.patches:
            water_bplot.annotate(format(p.get_height(), '.1f'), 
                        (p.get_x() + p.get_width() / 2., p.get_height()), 
                        ha = 'center', va = 'center', fontsize = 13,
                        xytext = (0, 9), 
                        textcoords = 'offset points')
        # highlighting the title
        axes.set_title('Percentage of Schools with Water Facility in India',size = 18 , pad = 16, color='black',bbox=dict(facecolor='white', alpha=1.0))
        axes.set_ylabel('Percentage',size=13)
        axes.set_xlabel('Year',size=13)
        water_bplot.legend(fancybox=True, framealpha=1, borderpad=0.5)
        st.pyplot(f)

    if Faci == 'Electricity':
        elec_columns = ['State_UT','year','Primary_Only','U_Primary_Only','Sec_Only','HrSec_Only']
        elec_ai = elec.loc[:,elec_columns]
        tidy_elec = pd.melt(elec_ai,id_vars=['year','State_UT']).rename(columns=str.title)

        # setting the plot styles and backgrounds
        sns.set(style="ticks",context="talk")
        plt.style.use('seaborn-deep')
        f, axes = plt.subplots(1, 1, figsize=(20, 10))
        # barplot for electricity facility
        elec_bplot = sns.barplot(x="Year",y='Value',hue='Variable',data=tidy_elec,palette = 'CMRmap',edgecolor='black',ax=axes)
        elec_bplot.set(ylim=(0, 125))
        for p in elec_bplot.patches:
            elec_bplot.annotate(format(p.get_height(), '.1f'), 
                        (p.get_x() + p.get_width() / 2., p.get_height()), 
                        ha = 'center', va = 'center', fontsize = 13,
                        xytext = (0, 9), 
                        textcoords = 'offset points')
        # highlighting the title
        axes.set_title('Percentage of Schools with Electricity Facility in India',size = 18 , pad = 16, color='black',bbox=dict(facecolor='white', alpha=1.0))
        axes.set_ylabel('Percentage',size=13)
        axes.set_xlabel('Year',size=13)
        elec_bplot.legend(fancybox=True, framealpha=1, borderpad=0.5)
        st.pyplot(f)

    if Faci == 'Computers':
        comps_columns = ['State_UT','year','Primary_Only','U_Primary_Only','Sec_Only','HrSec_Only']
        comps_ai = com.loc[:,comps_columns]
        tidy_comps = pd.melt(comps_ai,id_vars=['year','State_UT']).rename(columns=str.title)
                # setting the plot styles and backgrounds
        sns.set(style="ticks",context="talk")
        plt.style.use('seaborn-deep')
        f, axes = plt.subplots(1, 1, figsize=(20, 10))
        # barplot for computer facility
        comps_bplot = sns.barplot(x="Year",y='Value',hue='Variable',data=tidy_comps,palette = 'Pastel2',edgecolor='black',ax=axes)
        comps_bplot.set(ylim=(0, 80))
        for p in comps_bplot.patches:
            comps_bplot.annotate(format(p.get_height(), '.1f'), 
                        (p.get_x() + p.get_width() / 2., p.get_height()), 
                        ha = 'center', va = 'center', fontsize = 13,
                        xytext = (0, 9), 
                        textcoords = 'offset points')

        # highlighting the title
        axes.set_title('Percentage of Schools with Computer Facility in India',size = 18 , pad = 16, color='black',bbox=dict(facecolor='white', alpha=1.0))
        axes.set_ylabel('Percentage',size=13)
        axes.set_xlabel('Year',size=13)
        comps_bplot.legend(fancybox=True, framealpha=1, borderpad=0.5)
        st.pyplot(f)

    if Faci == 'Boys/Girls Toilet':
        gbt_columns = ['State_UT','year','Primary_Only','U_Primary_Only','Sec_Only','HrSec_Only']
        gt_ai = g_t.loc[:,gbt_columns]
        bt_ai = b_t.loc[:,gbt_columns]
        tidy_gt = pd.melt(gt_ai,id_vars=['year','State_UT']).rename(columns=str.title)
        tidy_bt = pd.melt(bt_ai,id_vars=['year','State_UT']).rename(columns=str.title)
                # setting the plot styles and backgrounds
        sns.set(style="ticks",context="talk")
        plt.style.use('seaborn-deep')
        # creating two subplots: girls and boys
        f, axes = plt.subplots(1, 2, figsize=(20, 10))
        # -------------------------------------------------------------- #
        # barplot for girls
        t_girls_bplot = sns.barplot(x="Year",y='Value',hue='Variable',data=tidy_gt,palette='rainbow',edgecolor='black',ax=axes[0])
        t_girls_bplot.set(ylim=(40, 130))
        for p in t_girls_bplot.patches:
            t_girls_bplot.annotate(format(p.get_height(), '.1f'), 
                        (p.get_x() + p.get_width() / 2., p.get_height()), 
                        ha = 'center', va = 'center', fontsize = 13,
                        xytext = (0, 9), 
                        textcoords = 'offset points')

        # highlighting the title
        axes[0].set_title('Percentage of Toilet Facilities for Girls in India',size = 18 )#, pad = 16, color='white',bbox=dict(facecolor='black', alpha=1.0))

        axes[0].set_ylabel('Percentage',size=13)
        axes[0].set_xlabel('Year',size=13)

        t_girls_bplot.legend(fancybox=True, framealpha=1, borderpad=0.5)

        # ------------------------------------------------------------------- #
        # barplot for boys
        t_boys_bplot = sns.barplot(x="Year",y='Value',hue='Variable',data=tidy_bt,palette='rainbow',edgecolor='black',ax=axes[1])
        t_boys_bplot.set(ylim=(40, 130))
        for p in t_boys_bplot.patches:
            t_boys_bplot.annotate(format(p.get_height(), '.1f'), 
                        (p.get_x() + p.get_width() / 2., p.get_height()), 
                        ha = 'center', va = 'center', fontsize = 13,
                        xytext = (0, 9), 
                        textcoords = 'offset points')
        # highlighting the title
        axes[1].set_title('Percentage of Toilet Facilities for Boys in India',size = 18) #, pad = 16, color='white',bbox=dict(facecolor='black', alpha=1.0))
        axes[1].set_ylabel('Percentage',size=13)
        axes[1].set_xlabel('Year',size=13)
        t_boys_bplot.legend(fancybox=True, framealpha=1, borderpad=0.5)
        st.pyplot(f)