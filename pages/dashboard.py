import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Stellar Population Discovery",
    page_icon="🌟",
    layout="wide"
)

st.markdown("""
    <style>
    [data-testid="stSidebar"] [data-testid="stPageLink"] {
        font-size: 25px !important;
        font-weight: 700 !important;
        padding: 10px !important;
        margin-bottom: -45px !important;
    }

    [data-testid="stSidebar"] [data-testid="stPageLink"] p {
        font-size: 25px !important;
        font-weight: 700 !important;
    }
         
    [data-testid="stSidebar"] {
        background-color: #2D1B69 !important;
    }

    [data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }

    [data-testid="stSidebar"] h1 {
        font-size: 32px !important;
        font-weight: 800 !important;
    }

    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        font-size: 18px !important;
        font-weight: 700 !important;
        color: #E0C4FF !important;
    }

    [data-testid="stSidebar"] label {
        font-size: 18px !important;
        font-weight: 600 !important;
        color: #E0C4FF !important;
    }

    [data-testid="stSidebar"] hr {
        border: 1px solid #7B5FBE !important;
        opacity: 1 !important;
    }

    [data-testid="stSidebar"] [data-testid="stMetricLabel"] {
        color: #E0C4FF !important;
        font-size: 16px !important;
    }

    [data-testid="stSidebar"] [data-testid="stMetricValue"] {
        color: #FFFFFF !important;
        font-size: 28px !important;
        font-weight: 800 !important;
    }

    [data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] {
        background-color: #3D2B89 !important;
        border: 1px solid #7B5FBE !important;
        border-radius: 8px !important;
    }

    [data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] div {
        background-color: #3D2B89 !important;
        color: #FFFFFF !important;
        font-size: 16px !important;
    }

    [data-testid="stSidebar"] .stSelectbox svg {
        fill: #000000 !important;
        color: #000000 !important;
    }
    [data-baseweb="popover"] {
        background-color: #3D2B89 !important;
    }

    [data-baseweb="popover"] li {
        background-color: #3D2B89 !important;
        color: #FFFFFF !important;
        font-size: 16px !important;
    }

    [data-baseweb="popover"] li:hover {
        background-color: #6C63FF !important;
    }

    [data-testid="stSidebar"] code {
        background-color: #3D2B89 !important;
        color: #E0C4FF !important;
        border: none !important;
    }
            
    [data-testid="stSidebarNav"] {
        display: none !important;
    }

    /* ===== Fix Selectbox Text Color ===== */

[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] span {
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
}

[data-testid="stSidebar"] .stSelectbox input {
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
}

[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] {
    color: #000000 !important;
}
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    df_kmeans = pd.read_csv('data/gaia_kmeans.csv')
    df_dbscan = pd.read_csv('data/gaia_dbscan.csv')
    df_hierarchical = pd.read_csv('data/gaia_hierarchical.csv')
    df_cleaned = pd.read_csv('data/gaia_cleaned.csv')
    return df_kmeans, df_dbscan, df_hierarchical, df_cleaned

df_kmeans, df_dbscan, df_hierarchical, df_cleaned = load_data()


st.sidebar.page_link("home.py", label="🪐 Home", use_container_width=True)
st.sidebar.markdown("---")
st.sidebar.title("🔭 Observatory")

algorithm = st.sidebar.selectbox(
    "Select Algorithm",
    ["KMeans", "DBSCAN", "Hierarchical"]
)

show_noise = False
if algorithm == "DBSCAN":
    show_noise = st.sidebar.toggle("Show Noise Points", value=True)

if algorithm == "KMeans":
    df = df_kmeans.copy()
    cluster_col = 'kmeans_cluster'
elif algorithm == "DBSCAN":
    df = df_dbscan.copy()
    cluster_col = 'dbscan_cluster'
    if not show_noise:
        df = df[df[cluster_col] != -1]
else:
    df = df_hierarchical.copy()
    cluster_col = 'hierarchical_cluster'

st.sidebar.markdown("---")
st.sidebar.subheader("📊 2D Plot Axes")
x_axis = st.sidebar.selectbox("X Axis", ["PC1", "PC2", "PC3", "PC4"], 
                               index=0, key="x_axis_select")
y_axis = st.sidebar.selectbox("Y Axis", ["PC1", "PC2", "PC3", "PC4"], 
                               index=1, key="y_axis_select")

st.sidebar.markdown("---")
st.sidebar.metric("Stars Displayed", f"{len(df):,}")
st.sidebar.metric("Clusters Found", f"{df[cluster_col].nunique()}")

st.sidebar.markdown("---")
st.sidebar.subheader("📌 About")
st.sidebar.markdown("""
Discovering stellar populations from  
**50,000 Gaia DR3** stars using  
unsupervised ML.

**Best Score:** KMeans (0.4823)  
**Anomalous Stars:** 367 (DBSCAN)  
**Variance Retained:** 83.87%  
""")

st.sidebar.markdown("---")
st.sidebar.subheader("🛠️ Tech Stack")
st.sidebar.markdown("""
Python • Pandas • NumPy  
Scikit-learn • SciPy  
Plotly • Streamlit  
""")

st.sidebar.markdown("---")
st.sidebar.subheader("🔗 Links")
st.sidebar.markdown("""
[![GitHub](https://img.shields.io/badge/GitHub-Repo-black?logo=github)](https://github.com/parthshelar-dev/stellar-population-discovery)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Parth_Shelar-blue?logo=linkedin)](https://www.linkedin.com/in/parth-shelar)
""")

st.title("🌟 Stellar Population Discovery")
st.markdown("Unsupervised ML on 50,000 Gaia DR3 Stars")
st.markdown("---")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🔭 3D Visualization",
    "📊 2D Visualization", 
    "📈 Algorithm Comparison",
    "📋 Cluster Statistics",
    "🌌 Dataset Overview"
])

with tab1:
    st.subheader(f"3D Cluster Visualization — {algorithm}")
    
    if algorithm == "KMeans":
        cluster_names = {0: "Cluster 0", 1: "Cluster 1", 2: "Cluster 2", 3: "Cluster 3"}
    elif algorithm == "DBSCAN":
        cluster_names = {-1: "Noise/Anomalies", 0: "Main Population", 4: "Second Population"}
    else:
        cluster_names = {0: "Cluster 0", 1: "Cluster 1", 2: "Cluster 2"}

    df['cluster_name'] = df[cluster_col].map(cluster_names).fillna("Tiny Cluster")

    fig_3d = px.scatter_3d(
        df.sample(min(15000, len(df)), random_state=42),
        x='PC1', y='PC2', z='PC3',
        color='cluster_name',
        title=f'{algorithm} Clustering — 3D PCA Space',
        opacity=0.5,
        size_max=2,
        hover_data={'PC1': ':.2f', 'PC2': ':.2f', 'PC3': ':.2f', 'cluster_name': True}
    )
    fig_3d.update_traces(marker=dict(size=2))
    fig_3d.update_layout(
    height=600,
    paper_bgcolor='#F8F9FA',
    plot_bgcolor='#F8F9FA',
    legend=dict(
        font=dict(size=16),
        itemsizing='constant',
        itemwidth=40
        )
    )
    st.plotly_chart(fig_3d, use_container_width=True)

with tab2:
    st.subheader(f"2D Cluster Visualization — {algorithm}")
    
    fig_2d = px.scatter(
        df.sample(min(15000, len(df)), random_state=42),
        x=x_axis,
        y=y_axis,
        color='cluster_name',
        title=f'{algorithm} Clustering — {x_axis} vs {y_axis}',
        opacity=0.5,
        hover_data={'cluster_name': True, x_axis: ':.2f', y_axis: ':.2f'}
    )
    fig_2d.update_traces(marker=dict(size=3))
    fig_2d.update_layout(
        height=550,
        paper_bgcolor='#F8F9FA',
        plot_bgcolor='#F8F9FA',
        legend=dict(
            font=dict(size=16),
            itemsizing='constant',
            itemwidth=40
        )
    )
    st.plotly_chart(fig_2d, use_container_width=True)
        
with tab3:
    st.subheader("Algorithm Comparison")

    silhouette_data = {
        'Algorithm': ['KMeans', 'DBSCAN', 'Hierarchical'],
        'Silhouette Score': [0.4823, 0.4060, 0.4687]
    }
    df_scores = pd.DataFrame(silhouette_data)

    fig_sil = px.bar(
        df_scores,
        x='Algorithm',
        y='Silhouette Score',
        color='Algorithm',
        title='Silhouette Score Comparison',
        text='Silhouette Score',
        color_discrete_sequence=['steelblue', 'tomato', 'green']
    )
    fig_sil.update_traces(texttemplate='%{text:.4f}', textposition='outside')
    fig_sil.update_layout(
        height=400,
        yaxis_range=[0, 0.6],
        showlegend=False
    )

    kmeans_sizes = df_kmeans['kmeans_cluster'].value_counts().reset_index()
    kmeans_sizes.columns = ['Cluster', 'Count']
    kmeans_sizes['Algorithm'] = 'KMeans'

    dbscan_sizes = df_dbscan['dbscan_cluster'].value_counts().reset_index()
    dbscan_sizes.columns = ['Cluster', 'Count']
    dbscan_sizes['Algorithm'] = 'DBSCAN'

    hier_sizes = df_hierarchical['hierarchical_cluster'].value_counts().reset_index()
    hier_sizes.columns = ['Cluster', 'Count']
    hier_sizes['Algorithm'] = 'Hierarchical'

    df_sizes = pd.concat([kmeans_sizes, dbscan_sizes, hier_sizes])
    df_sizes['Cluster'] = df_sizes['Cluster'].astype(str)

    fig_sizes = px.bar(
        df_sizes,
        x='Cluster',
        y='Count',
        color='Algorithm',
        barmode='group',
        title='Cluster Size Comparison Across Algorithms',
        color_discrete_sequence=['steelblue', 'tomato', 'green']
    )
    fig_sizes.update_layout(height=400)

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig_sil, use_container_width=True)
    with col2:
        st.plotly_chart(fig_sizes, use_container_width=True)

with tab4:
    st.subheader(f"Cluster Statistics — {algorithm}")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Stars", f"{len(df):,}")
    with col2:
        st.metric("Clusters Found", f"{df[cluster_col].nunique()}")
    with col3:
        if algorithm == "DBSCAN":
            noise_count = (df_dbscan['dbscan_cluster'] == -1).sum()
            st.metric("Anomalous Stars", f"{noise_count}")
        else:
            st.metric("Algorithm", algorithm)

    st.markdown("---")

    st.subheader("Cluster Size Breakdown")
    cluster_stats = df[cluster_col].value_counts().reset_index()
    cluster_stats.columns = ['Cluster', 'Star Count']
    cluster_stats['Percentage'] = (
        cluster_stats['Star Count'] / cluster_stats['Star Count'].sum() * 100
    ).round(2)
    cluster_stats['Cluster'] = cluster_stats['Cluster'].astype(str)
    cluster_stats['Percentage'] = cluster_stats['Percentage'].astype(str) + '%'
    st.dataframe(cluster_stats, use_container_width=True)

    st.markdown("---")

    st.subheader("Key Findings")
    st.markdown("""
    - ✅ **Two distinct stellar populations** discovered consistently across all three algorithms
    - 🔴 **367 anomalous stars** identified by DBSCAN — potential outliers or rare stellar objects
    - 📊 **KMeans** achieved highest silhouette score (0.4823) — best cluster separation
    - 🌟 **All algorithms** scored above 0.40 — indicating good cluster quality
    - 🔭 **4 PCA components** retained 83.87% variance — used for all clustering
    """)

with tab5:
    st.subheader("Dataset Overview — Gaia DR3")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Stars", "50,000")
    with col2:
        st.metric("Features", "9")
    with col3:
        st.metric("PCA Components", "4")
    with col4:
        st.metric("Variance Retained", "83.87%")

    st.markdown("---")

    st.subheader("Hertzsprung-Russell Diagram")
    fig_hr = px.scatter(
        df_cleaned.sample(min(10000, len(df_cleaned)), random_state=42),
        x='bp_rp',
        y='phot_g_mean_mag',
        color='teff_gspphot',
        color_continuous_scale='RdYlBu_r',
        title='HR Diagram — Color Index vs Magnitude',
        labels={
            'bp_rp': 'BP-RP Color Index (Blue → Red)',
            'phot_g_mean_mag': 'G Magnitude (Brightness)',
            'teff_gspphot': 'Surface Temp (K)'
        },
        opacity=0.5
    )
    fig_hr.update_traces(marker=dict(size=2))
    fig_hr.update_yaxes(autorange='reversed')
    fig_hr.update_layout(height=500)
    st.plotly_chart(fig_hr, use_container_width=True)

    st.markdown("---")

    st.subheader("Stellar Proper Motion")
    fig_pm = px.scatter(
        df_cleaned.sample(min(10000, len(df_cleaned)), random_state=42),
        x='pmra',
        y='pmdec',
        color='teff_gspphot',
        color_continuous_scale='RdYlBu_r',
        title='Proper Motion Colored by Surface Temperature',
        labels={
            'pmra': 'Proper Motion RA (mas/yr)',
            'pmdec': 'Proper Motion Dec (mas/yr)',
            'teff_gspphot': 'Surface Temp (K)'
        },
        opacity=0.5,
        range_x=[-50, 50],
        range_y=[-50, 50]
    )
    fig_pm.update_traces(marker=dict(size=2))
    fig_pm.update_layout(height=500)
    st.plotly_chart(fig_pm, use_container_width=True)

