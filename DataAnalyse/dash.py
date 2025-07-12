  

# import pandas as pd
# import streamlit as st
# import plotly.express as px
# import io


# st.set_page_config(page_title="Inject Solar Analyser", page_icon=":chart:")


# st.markdown("<style>div.block-container { padding-top: 6rem; }</style>", unsafe_allow_html=True)

# st.markdown(
#     """
#     <style>
#     .dashboard-title {
#         position: fixed;
#         top: 1rem;
#         left: 1rem;
#         font-size: 2.2rem;
#         font-weight: 700;
#         color: white;
#         z-index: 1000;
#     }
#     </style>
#     <div class="dashboard-title">Data Analyser</div>
#     """,
#     unsafe_allow_html=True
# )


# # Upload CSV
# uploaded_file = st.file_uploader("Upload your CSV file", type="csv")
# if uploaded_file is not None:
#     df = pd.read_csv(uploaded_file)

#     # Convert to datetime
#     df['received_at'] = pd.to_datetime(df['received_at'], errors='coerce')
#     df = df.dropna(subset=['received_at'])
#     df['DateOnly'] = df['received_at'].dt.date.astype(str)
#     df['DateTime'] = df['received_at'] 

#     # Sort
#     df_sorted = df.sort_values("DateTime")

#     # Date filter dropdowns
#     date_options = sorted(df_sorted['DateOnly'].unique())
#     col1, col2 = st.columns(2)
#     with col1:
#         start_date_str = st.selectbox("From Date", date_options, index=0)
#     with col2:
#         end_date_str = st.selectbox("To Date", date_options, index=len(date_options) - 1)

    
#         # Time range selection
#     time_options = sorted(df_sorted['DateTime'].dt.strftime("%H:%M").unique())
#     col1, col2 = st.columns(2)
#     with col1:
#         start_time_str = st.selectbox("Select Start Time", time_options, index=0)
#     with col2:
#         end_time_str = st.selectbox("Select End Time", time_options, index=len(time_options) - 1)
#     start_date = pd.to_datetime(start_date_str)
#     end_date = pd.to_datetime(end_date_str)

#     # Filter by selected date range
#     df_filtered = df_sorted[
#         (df_sorted['DateTime'] >= start_date) &
#         (df_sorted['DateTime'] <= end_date + pd.Timedelta(days=1))
#     ]

#     start_time = pd.to_datetime(start_time_str, format="%H:%M").time()
#     end_time = pd.to_datetime(end_time_str, format="%H:%M").time()

#     df_filtered = df_sorted[
#         (df_sorted['DateTime'].dt.time >= start_time) &
#         (df_sorted['DateTime'].dt.time <= end_time)
#     ]

    
#     param_options = [col for col in df.columns if col.startswith("") and col not in ['param_41', 'param_42']]
#     selected_param = st.selectbox("Select Parameter to Plot", param_options)

    
#     fig = px.line(df_filtered, x='DateTime', y=selected_param,
#                   title=f"{selected_param} VS Time",
#                   labels={'DateTime': 'Time', selected_param: selected_param},
#                   template="plotly_white")

#     fig.update_traces(line=dict(color='red'))
#     fig.update_layout(xaxis_title="Time", yaxis_title=selected_param, hovermode='x unified')

#     st.plotly_chart(fig, use_container_width=True)
#     #st.savefig("graph.png", fig)
    
#     buffer = io.BytesIO()
#     fig.write_image(buffer, format='png')
#     st.download_button(
#         label="⬇️ Download Graph as PNG",
#         data=buffer.getvalue(),
#         file_name=f"{selected_param}_graph.png",
#         # mime="image/png"
#     )
  


#     st.markdown("---")
#     st.subheader("Custom Graph")

#     numeric_columns = df.select_dtypes(include='number').columns.tolist()
#     all_columns = df.columns.tolist()

#     col_x, col_y = st.columns(2)
#     with col_x:
#         selected_x = st.selectbox("Select X-axis", options=all_columns)
#     with col_y:
#         selected_y = st.selectbox("Select Y-axis", options=numeric_columns)

#     # Plot second graph
#     custom_fig = px.line(df, x=selected_x, y=selected_y,
#                          title=f"{selected_y} vs {selected_x}",
#                          labels={selected_x: selected_x, selected_y: selected_y},
#                          template="plotly_white")

#     custom_fig.update_traces(line=dict(color='blue'))
#     custom_fig.update_layout(xaxis_title=selected_x, yaxis_title=selected_y, hovermode='x unified')

#     st.plotly_chart(custom_fig, use_container_width=True)

#     # Download for second graph
#     custom_buffer = io.BytesIO()
#     custom_fig.write_image(custom_buffer, format='png')
#     st.download_button(
#         label="⬇️ Download Custom Graph",
#         data=custom_buffer.getvalue(),
#         file_name=f"{selected_y}_vs_{selected_x}.png",
#     )



import pandas as pd
import streamlit as st
import plotly.express as px
import io




st.set_page_config(page_title="Inject Solar Analyser", page_icon=":chart:", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    div.block-container { padding-top: 1rem; }
    .dashboard-title {
        font-size: 2rem;
        font-weight: 700;
        color: white;
        margin-bottom: 0.5rem;
    }
    .compact-uploader .stFileUploader {
        padding: 0;
        margin-top: -0.3rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title and Uploader
title_col, upload_col = st.columns([3, 2])
with title_col:
    st.markdown('<div class="dashboard-title">Data Analyser</div>', unsafe_allow_html=True)
with upload_col:
    st.markdown('<div class="compact-uploader">', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("", type="csv", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

# Main App
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Preprocess
    df['received_at'] = pd.to_datetime(df['received_at'], errors='coerce')
    df = df.dropna(subset=['received_at'])
    df['DateOnly'] = df['received_at'].dt.date.astype(str)
    df['DateTime'] = df['received_at']
    df_sorted = df.sort_values("DateTime")


    tab1, tab2 = st.tabs(["Time Graph", "Custom Graph"])
        
    with tab1:
        df['received_at'] = pd.to_datetime(df['received_at'], errors='coerce')
        df = df.dropna(subset=['received_at'])
        df['DateOnly'] = df['received_at'].dt.date.astype(str)
        df['DateTime'] = df['received_at']
        df_sorted = df.sort_values("DateTime")

        date_options = sorted(df_sorted['DateOnly'].unique())
        time_options = sorted(df_sorted['DateTime'].dt.strftime("%H:%M").unique())
        param_options = [col for col in df.columns if col.startswith("") and col not in ['param_41', 'param_42']]

        col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1.5])
        with col1:
            start_date_str = st.selectbox("From Date", date_options, index=0, key="start_date")
        with col2:
            end_date_str = st.selectbox("To Date", date_options, index=len(date_options) - 1, key="end_date")
        with col3:
            start_time_str = st.selectbox("Start Time", time_options, index=0, key="start_time")
        with col4:
            end_time_str = st.selectbox("End Time", time_options, index=len(time_options) - 1, key="end_time")
        with col5:
            selected_param = st.selectbox("Parameter", param_options, key="param")

        start_datetime = pd.to_datetime(f"{start_date_str} {start_time_str}")
        end_datetime = pd.to_datetime(f"{end_date_str} {end_time_str}")

        df_filtered = df_sorted[
            (df_sorted['DateTime'] >= start_datetime) &
            (df_sorted['DateTime'] <= end_datetime)
        ]

        fig = px.line(df_filtered, x='DateTime', y=selected_param,
                      title=f"{selected_param} VS Time",
                      labels={'DateTime': 'Time', selected_param: selected_param},
                      template="plotly_white")
        fig.update_traces(line=dict(color='red'))
        fig.update_layout(xaxis_title="Time", yaxis_title=selected_param, hovermode='x unified')
        st.plotly_chart(fig, use_container_width=True)

        buffer = io.BytesIO()
        fig.write_image(buffer, format='png')
        st.download_button(
            label="⬇️ Download Graph as PNG",
            data=buffer.getvalue(),
            file_name=f"{selected_param}_graph.png",
        )


    with tab2:
        st.subheader("Custom Graph")
        st.markdown("---")

        # Row 1: Serial No., SubDeviceID, pkt_type
        col1, col2, col3 = st.columns(3)

        with col1:
            selected_serial = st.selectbox("Select Serial No.", df_sorted['Serial_No.'].dropna().unique(), key="serial")
            filtered_serial_df = df_sorted[df_sorted['Serial_No.'] == selected_serial]

        with col2:
            subdevice_options = filtered_serial_df['SubDeviceID'].dropna().unique()
            selected_subdevice = st.selectbox("Select SubDeviceID", subdevice_options, key="subdev")

        with col3:
            pkt_options = filtered_serial_df[filtered_serial_df['SubDeviceID'] == selected_subdevice]['pkt_type'].dropna().unique()
            selected_pkt = st.selectbox("Select Packet Type", pkt_options, key="pkt")

        # Filter by all 3
        filtered_df = filtered_serial_df[
            (filtered_serial_df['SubDeviceID'] == selected_subdevice) &
            (filtered_serial_df['pkt_type'] == selected_pkt)
        ]

        if filtered_df.empty:
            st.warning("No data for this Serial No. + SubDeviceID + pkt_type combination.")
        else:
            # Row 2: Dates & Axes
            available_dates = sorted(filtered_df['DateOnly'].unique())

            col4, col5, col6, col7 = st.columns(4)
            with col4:
                start_date = st.selectbox("From Date", available_dates, index=0, key="start")
            with col5:
                end_date = st.selectbox("To Date", available_dates, index=len(available_dates)-1, key="end")
            with col6:
                selected_x = st.selectbox("Select X-axis", filtered_df.columns, key="xaxis")
            with col7:
                selected_y = st.selectbox("Select Y-axis", filtered_df.columns, key="yaxis")

            # Final date filtering
            start_dt = pd.to_datetime(start_date)
            end_dt = pd.to_datetime(end_date) + pd.Timedelta(days=1) - pd.Timedelta(seconds=1)

            df_final = filtered_df[
                (filtered_df["DateTime"] >= start_dt) &
                (filtered_df["DateTime"] <= end_dt)
            ].dropna(subset=[selected_x, selected_y])

            if df_final.empty:
                st.warning("No data in selected date range.")
            else:
                fig = px.line(df_final, x=selected_x, y=selected_y,
                              title=f"{selected_y} vs {selected_x}",
                              labels={selected_x: selected_x, selected_y: selected_y},
                              template="plotly_white")
                fig.update_traces(line=dict(color='blue'))
                fig.update_layout(xaxis_title=selected_x, yaxis_title=selected_y, hovermode='x unified')
                st.plotly_chart(fig, use_container_width=True)

                # Download
                buffer = io.BytesIO()
                fig.write_image(buffer, format='png')
                st.download_button(
                    label="⬇️ Download Custom Graph",
                    data=buffer.getvalue(),
                    file_name=f"{selected_y}_vs_{selected_x}.png"
                )
