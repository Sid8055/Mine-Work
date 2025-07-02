  

import pandas as pd
import streamlit as st
import plotly.express as px
import io


st.set_page_config(page_title="Inject Solar Analyser", page_icon=":chart:")


st.markdown("<style>div.block-container { padding-top: 6rem; }</style>", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .dashboard-title {
        position: fixed;
        top: 1rem;
        left: 1rem;
        font-size: 2.2rem;
        font-weight: 700;
        color: white;
        z-index: 1000;
    }
    </style>
    <div class="dashboard-title">Data Analyser</div>
    """,
    unsafe_allow_html=True
)


# Upload CSV
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Convert to datetime
    df['received_at'] = pd.to_datetime(df['received_at'], errors='coerce')
    df = df.dropna(subset=['received_at'])
    df['DateOnly'] = df['received_at'].dt.date.astype(str)
    df['DateTime'] = df['received_at'] 

    # Sort
    df_sorted = df.sort_values("DateTime")

    # Date filter dropdowns
    date_options = sorted(df_sorted['DateOnly'].unique())
    col1, col2 = st.columns(2)
    with col1:
        start_date_str = st.selectbox("From Date", date_options, index=0)
    with col2:
        end_date_str = st.selectbox("To Date", date_options, index=len(date_options) - 1)

    
        # Time range selection
    time_options = sorted(df_sorted['DateTime'].dt.strftime("%H:%M").unique())
    col1, col2 = st.columns(2)
    with col1:
        start_time_str = st.selectbox("Select Start Time", time_options, index=0)
    with col2:
        end_time_str = st.selectbox("Select End Time", time_options, index=len(time_options) - 1)
    start_date = pd.to_datetime(start_date_str)
    end_date = pd.to_datetime(end_date_str)

    # Filter by selected date range
    df_filtered = df_sorted[
        (df_sorted['DateTime'] >= start_date) &
        (df_sorted['DateTime'] <= end_date + pd.Timedelta(days=1))
    ]

    start_time = pd.to_datetime(start_time_str, format="%H:%M").time()
    end_time = pd.to_datetime(end_time_str, format="%H:%M").time()

    df_filtered = df_sorted[
        (df_sorted['DateTime'].dt.time >= start_time) &
        (df_sorted['DateTime'].dt.time <= end_time)
    ]

    
    param_options = [col for col in df.columns if col.startswith("") and col not in ['param_41', 'param_42']]
    selected_param = st.selectbox("Select Parameter to Plot", param_options)

    
    fig = px.line(df_filtered, x='DateTime', y=selected_param,
                  title=f"{selected_param} VS Time",
                  labels={'DateTime': 'Time', selected_param: selected_param},
                  template="plotly_white")

    fig.update_traces(line=dict(color='red'))
    fig.update_layout(xaxis_title="Time", yaxis_title=selected_param, hovermode='x unified')

    st.plotly_chart(fig, use_container_width=True)
    #st.savefig("graph.png", fig)
    
    buffer = io.BytesIO()
    fig.write_image(buffer, format='png')
    st.download_button(
        label="⬇️ Download Graph as PNG",
        data=buffer.getvalue(),
        file_name=f"{selected_param}_graph.png",
        # mime="image/png"
    )
  


    st.markdown("---")
    st.subheader("Custom Graph")

    numeric_columns = df.select_dtypes(include='number').columns.tolist()
    all_columns = df.columns.tolist()

    col_x, col_y = st.columns(2)
    with col_x:
        selected_x = st.selectbox("Select X-axis", options=all_columns)
    with col_y:
        selected_y = st.selectbox("Select Y-axis", options=numeric_columns)

    # Plot second graph
    custom_fig = px.line(df, x=selected_x, y=selected_y,
                         title=f"{selected_y} vs {selected_x}",
                         labels={selected_x: selected_x, selected_y: selected_y},
                         template="plotly_white")

    custom_fig.update_traces(line=dict(color='blue'))
    custom_fig.update_layout(xaxis_title=selected_x, yaxis_title=selected_y, hovermode='x unified')

    st.plotly_chart(custom_fig, use_container_width=True)

    # Download for second graph
    custom_buffer = io.BytesIO()
    custom_fig.write_image(custom_buffer, format='png')
    st.download_button(
        label="⬇️ Download Custom Graph",
        data=custom_buffer.getvalue(),
        file_name=f"{selected_y}_vs_{selected_x}.png",
    )



