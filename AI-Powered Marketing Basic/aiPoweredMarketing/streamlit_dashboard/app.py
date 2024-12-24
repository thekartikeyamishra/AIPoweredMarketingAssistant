import streamlit as st
from utils.content_generation import generate_content
from utils.campaign_analysis import analyze_campaign_performance
from utils.audience_segmentation import segment_audience
from utils.strategy_recommendation import generate_strategy
from utils.visualization import plot_campaign_performance

st.title("AI-Powered Marketing Assistant")

st.subheader("Generate Marketing Content")
prompt = st.text_input("Enter a prompt for the content.")
content_type = st.selectbox("Select content type", ["social media", "blog", "email"])
if st.button("Generate Content"):
    content = generate_content(prompt, content_type)
    st.text_area("Generated Content", content)

# Campaign Analysis
st.subheader("Analyze Campaign Performance")
uploaded_campaign_data = st.file_uploader("Upload Campaign Data (CSV)", type=["csv"])
if uploaded_campaign_data:
    metrics = analyze_campaign_performance(uploaded_campaign_data)
    st.write(metrics)
    plot_campaign_performance(uploaded_campaign_data)
    st.image("output/analytics_reports/performance.png")

# Audience Segmentation
st.subheader("Segment Audience")
uploaded_audience_data = st.file_uploader("Upload Audience Data (CSV)", type=["csv"])
if uploaded_audience_data:
    segment_data = segment_audience(uploaded_audience_data)
    st.write(segment_data)

# Strategy Recommandations
st.subheader("Generate Strategy Recommendations")
if st.button("Generate Strategy:"):
    strategy = generate_strategy(metrics)
    st.text_area("Strategy Recommendations", strategy)
