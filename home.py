import streamlit as st

st.set_page_config(
    page_title="Stellar Population Discovery",
    page_icon="🌟",
    layout="wide"
)

st.markdown("""
    <style> 
    .main {
        background-color: #1A0A2E;
    }
    
    .stApp {
        background-color: #1A0A2E;
    }

    h1, h2, h3, p, li {
        color: #FFFFFF !important;
    }

    .hero-title {
        font-size: 64px;
        font-weight: 900;
        color: #FFFFFF;
        text-align: center;
        margin-bottom: 10px;
    }

    .hero-subtitle {
        font-size: 22px;
        color: #C4A8FF;
        text-align: center;
        margin-bottom: 40px;
    }

    .stat-card {
        background-color: #2D1B69;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        border: 1px solid #6C63FF;
    }

    .stat-number {
        font-size: 42px;
        font-weight: 900;
        color: #FFFFFF;
    }

    .stat-label {
        font-size: 16px;
        color: #FFFFFF;
    }

    .section-title {
        font-size: 32px;
        font-weight: 800;
        color: #FFFFFF;
        margin-top: 40px;
        margin-bottom: 20px;
    }

    .info-card {
        background-color: #2D1B69;
        border-radius: 12px;
        padding: 25px;
        border-left: 4px solid #6C63FF;
        margin-bottom: 20px;
    }

    .divider {
        border: 1px solid #3D2B89;
        margin: 40px 0;
    }
            
    [data-testid="stSidebar"] {
        display: none !important;
    }

    [data-testid="collapsedControl"] {
        display: none !important;
    }
            
    header[data-testid="stHeader"] {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div style='text-align: center; padding: 60px 0 40px 0;'>
        <div class='hero-title'>🌟 Stellar Population Discovery</div>
        <div class='hero-subtitle'>
            Unsupervised Machine Learning on 50,000 Real Stars from Gaia DR3
        </div>
    </div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
        <div class='stat-card'>
            <div class='stat-number'>50K</div>
            <div class='stat-label'>Stars Analyzed</div>
        </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
        <div class='stat-card'>
            <div class='stat-number'>3</div>
            <div class='stat-label'>ML Algorithms</div>
        </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
        <div class='stat-card'>
            <div class='stat-number'>367</div>
            <div class='stat-label'>Anomalous Stars</div>
        </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown("""
        <div class='stat-card'>
            <div class='stat-number'>84%</div>
            <div class='stat-label'>Variance Retained</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

st.markdown("<div class='section-title'>🔭 What is Gaia DR3?</div>", unsafe_allow_html=True)
st.markdown("""
    <div class='info-card'>
        <p>
        Gaia is a space observatory launched by the European Space Agency (ESA) 
        in 2013. Its mission is to create the most precise 3D map of the Milky Way 
        by measuring the positions, distances, and motions of over 1 billion stars.
        </p>
        <p>
        <b>Gaia Data Release 3 (DR3)</b> is the third major data release containing 
        astrometric, photometric, and spectroscopic measurements of 1.8 billion stars. 
        This project uses a carefully filtered sample of <b>50,000 high-quality stars</b> 
        from this dataset.
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

st.markdown("<div class='section-title'>🌌 Why Do Engineers Classify Stars?</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
        <div class='info-card'>
            <h3>🔬 Scientific Discovery</h3>
            <p>Classifying stars helps astronomers understand the life cycles 
            of stars — from their birth in nebulae to their death as white dwarfs, 
            neutron stars, or black holes.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class='info-card'>
            <h3>🌠 Galactic Evolution</h3>
            <p>Different stellar populations reveal the formation history of 
            our galaxy. Older stars have different chemical compositions than 
            younger ones — grouping them uncovers the Milky Way's past.</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class='info-card'>
            <h3>🚀 Finding Rare Objects</h3>
            <p>Anomaly detection in stellar data helps identify rare and unusual 
            objects — runaway stars, binary systems, variable stars, and 
            potential exoplanet host candidates.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class='info-card'>
            <h3>🤖 Handling Big Data</h3>
            <p>Gaia DR3 contains 1.8 billion stars — far too many to classify 
            manually. Machine learning automates this process, finding hidden 
            patterns that humans cannot detect at this scale.</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

st.markdown("<div class='section-title'>🎯 Project Purpose</div>", unsafe_allow_html=True)
st.markdown("""
    <div class='info-card'>
        <p>
        This project applies <b>unsupervised machine learning</b> to discover 
        naturally occurring stellar populations in real Gaia DR3 data — without 
        any predefined labels or human guidance.
        </p>
        <p>Three clustering algorithms are compared:</p>
        <ul>
            <li><b>KMeans</b> — finds compact spherical clusters (Score: 0.4823)</li>
            <li><b>DBSCAN</b> — detects density-based clusters and anomalies (Score: 0.4060)</li>
            <li><b>Agglomerative Hierarchical</b> — builds a tree of star relationships (Score: 0.4687)</li>
        </ul>
        <p>
        PCA reduces 9 stellar features to 4 components retaining <b>83.87% variance</b>, 
        enabling effective clustering and 3D visualization.
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
        <div style='text-align: center; padding: 20px;'>
            <p style='font-size: 20px; color: #C4A8FF;'>
                Ready to explore the stellar populations?
            </p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div style='text-align: center;'>
            <a href='/dashboard' target='_self'>
                <button style='
                    background-color: #6C63FF;
                    color: white;
                    font-size: 20px;
                    font-weight: 700;
                    padding: 15px 40px;
                    border: none;
                    border-radius: 12px;
                    cursor: pointer;
                    letter-spacing: 1px;
                '>🚀 Explore Dashboard</button>
            </a>
        </div>
    """, unsafe_allow_html=True)