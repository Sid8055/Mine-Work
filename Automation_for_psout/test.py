# import streamlit as st
# import matplotlib.pyplot as plt
# import pandas as pd
# import mhi.psout
# import tempfile
# import openpyxl

# # --- Page Config ---
# st.set_page_config("PSOUT Path Graph Viewer", layout="wide")

# # --- Custom CSS for Styling ---
# st.markdown("""
#     <style>
#     .title-style {
#         text-align: left;
#         font-size: 2rem;
#         font-weight: 800;
#         color: #FFFFFF;
#         margin-bottom: 10px;
#     }

#     .upload-section {
#         display: flex;
#         gap: 30px;
#         flex-wrap: wrap;
#         justify-content: flex-start;
#         margin-bottom: 20px;
#     }

#     .element-container:has(.uploadedFile) {
#         max-width: 400px !important;
#         margin-bottom: 10px !important;
#     }

#     .stSelectbox {
#         max-width: 300px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # --- Custom Title ---
# st.markdown('<div class="title-style">PSOUT File Path Plotter</div>', unsafe_allow_html=True)

# # --- File Upload Section ---
# st.markdown('<div class="upload-section">', unsafe_allow_html=True)
# psout_file = st.file_uploader("Upload your .psout file", type=["psout"])
# excel_file = st.file_uploader("Upload your Excel file", type=["xlsx"])
# st.markdown('</div>', unsafe_allow_html=True)

# # --- Proceed if both files are uploaded ---
# if psout_file is not None and excel_file is not None:
#     df_sconfg = pd.read_excel(excel_file, sheet_name="SConfig")

#     POI_Parameters = []
#     POI_Parameters_DDL = []

#     for i in range(1, len(df_sconfg)):
#         POI_Parameters.append('Root/' + df_sconfg['Canvas'][i] + '/' + df_sconfg['ParameterName'][i] + '/0')
#         POI_Parameters_DDL.append(df_sconfg['SignalType'][i] + '_' + df_sconfg['ParameterName'][i])

#     selected_path_temp = st.selectbox("Select a trace path to plot", POI_Parameters_DDL)
#     selected_path = POI_Parameters[POI_Parameters_DDL.index(selected_path_temp)]

#     if selected_path:
#         with tempfile.NamedTemporaryFile(delete=False, suffix=".psout") as tmp:
#             tmp.write(psout_file.read())
#             tmp_path = tmp.name

#         try:
#             with mhi.psout.File(tmp_path) as file:
#                 run = file.run(0)
#                 tempchannel = file.call(selected_path)
#                 for call in tempchannel.calls():
#                     trace2 = run.trace(call)
#                     time = trace2.domain

#                 # Plotting
#                 fig, ax = plt.subplots(figsize=(10, 5))
#                 ax.plot(time.data, trace2.data)
#                 ax.set_title(selected_path_temp)
#                 ax.set_xlabel("Time")
#                 ax.set_ylabel("Value")
#                 ax.grid(True)
#                 st.pyplot(fig, use_container_width=True)

#         except Exception as e:
#             st.error(f"Error reading or plotting trace: {e}")




# import streamlit as st
# import matplotlib.pyplot as plt
# import pandas as pd
# import mhi.psout
# import tempfile
# import openpyxl

# st.set_page_config("PSOUT Path Graph Viewer", layout="wide")

# # Custom CSS
# st.markdown("""
#     <style>
#     div.block-container { padding-top: 1rem; }
#     .dashboard-title {
#         font-size: 2rem;
#         font-weight: 700;
#         color: white;
#         margin-bottom: 0.5rem;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Title and Upload Section
# title_col, upload_col = st.columns([3, 2])
# with title_col:
#     st.markdown('<div class="dashboard-title">PSOUT File Path Plotter</div>', unsafe_allow_html=True)

# with upload_col:
#     st.markdown('<div style="font-weight:bold; margin-bottom:0.2rem;">Upload your .psout file</div>', unsafe_allow_html=True)
#     psout_file = st.file_uploader("", type=["psout"], label_visibility="collapsed")

#     st.markdown('<div style="font-weight:bold; margin-top:1rem; margin-bottom:0.2rem;">Upload your .xlsx file</div>', unsafe_allow_html=True)
#     excel_file = st.file_uploader("", type=["xlsx"], label_visibility="collapsed")

# # Process the uploaded Excel file
# if excel_file is not None:
#     df_sconfg = pd.read_excel(excel_file, sheet_name="SConfig")
#     POI_Parameters = []
#     POI_Parameters_DDL = []

#     for i in range(1, len(df_sconfg)):
#         POI_Parameters.append('Root/' + df_sconfg['Canvas'][i] + '/' + df_sconfg['ParameterName'][i] + '/0')
#         POI_Parameters_DDL.append(df_sconfg['SignalType'][i] + '_' + df_sconfg['ParameterName'][i])

#     selected_path_temp = st.selectbox("Select a trace path to plot", POI_Parameters_DDL)
#     selected_path = POI_Parameters[POI_Parameters_DDL.index(selected_path_temp)]

#     if psout_file is not None and selected_path:
#         with tempfile.NamedTemporaryFile(delete=False, suffix=".psout") as tmp:
#             tmp.write(psout_file.read())
#             tmp_path = tmp.name

#         try:
#             with mhi.psout.File(tmp_path) as file:
#                 run = file.run(0)
#                 tempchannel = file.call(selected_path)
#                 for call in tempchannel.calls():
#                     trace2 = run.trace(call)
#                     time = trace2.domain

#                 # Plot
#                 fig, ax = plt.subplots(figsize=(10, 5))
#                 ax.plot(time.data, trace2.data)
#                 ax.set_xlabel("Time")
#                 ax.set_ylabel("Value")
#                 ax.grid(True)
#                 ax.set_title(selected_path_temp)
#                 st.plotly_chart(fig, use_container_width = True)

#         except Exception as e:
#             st.error(f"Error reading or plotting trace: {e}")





# import streamlit as st
# import matplotlib.pyplot as plt
# import pandas as pd
# import mhi.psout
# import tempfile
# import openpyxl

# st.set_page_config("PSOUT Path Graph Viewer", layout="wide")

# # Custom CSS
# st.markdown("""
#     <style>
#     div.block-container { padding-top: 1rem; }
#     .dashboard-title {
#         font-size: 2rem;
#         font-weight: 700;
#         color: white;
#         margin-bottom: 0.5rem;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Title
# st.markdown('<div class="dashboard-title">PSOUT File Path Plotter</div>', unsafe_allow_html=True)

# # Side-by-side Uploaders
# col1, col2 = st.columns(2)

# with col1:
#     st.markdown('<div style="font-weight:bold; margin-bottom:0.2rem;">Upload your .psout file</div>', unsafe_allow_html=True)
#     psout_file = st.file_uploader("", type=["psout"], label_visibility="collapsed")

# with col2:
#     st.markdown('<div style="font-weight:bold; margin-bottom:0.2rem;">Upload your .xlsx file</div>', unsafe_allow_html=True)
#     excel_file = st.file_uploader("", type=["xlsx"], label_visibility="collapsed")

# # Process and plot if files are uploaded
# if psout_file is not None and excel_file is not None:
#     df_sconfg = pd.read_excel(excel_file, sheet_name="SConfig")
#     POI_Parameters = []
#     POI_Parameters_DDL = []

#     for i in range(1, len(df_sconfg)):
#         POI_Parameters.append('Root/' + df_sconfg['Canvas'][i] + '/' + df_sconfg['ParameterName'][i] + '/0')
#         POI_Parameters_DDL.append(df_sconfg['SignalType'][i] + '_' + df_sconfg['ParameterName'][i])

#     selected_path_temp = st.selectbox("Select a trace path to plot", POI_Parameters_DDL)
#     selected_path = POI_Parameters[POI_Parameters_DDL.index(selected_path_temp)]

#     with tempfile.NamedTemporaryFile(delete=False, suffix=".psout") as tmp:
#         tmp.write(psout_file.read())
#         tmp_path = tmp.name

#     try:
#         with mhi.psout.File(tmp_path) as file:
#             run = file.run(0)
#             tempchannel = file.call(selected_path)
#             for call in tempchannel.calls():
#                 trace2 = run.trace(call)
#                 time = trace2.domain

#             # Plot
#             fig, ax = plt.subplots(figsize=(10, 5))
#             ax.plot(time.data, trace2.data)
#             ax.set_xlabel("Time")
#             ax.set_ylabel(f"{selected_path_temp}")
#             ax.grid(True)
#             ax.set_title("Trace Plot for " + selected_path_temp)
#             st.plotly_chart(fig, use_container_width = True)

#     except Exception as e:
#         st.error(f"Error reading or plotting trace: {e}")






# import streamlit as st
# import matplotlib.pyplot as plt
# import pandas as pd
# import mhi.psout
# import tempfile
# # import openpyxl

# st.set_page_config("PSOUT Path Graph Viewer", layout="wide")

# # Custom CSS
# st.markdown("""
#     <style>
#     div.block-container { padding-top: 1rem; }
#     .dashboard-title {
#         font-size: 2rem;
#         font-weight: 700;
#         color: white;
#         margin-bottom: 0.5rem;
#     }
#     .stFileUploader {
#         transform: scale(0.85);
#         width: 95% !important;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Side-by-side Uploaders (now compact)
# col1, col2, col3 = st.columns(3)

# # Title


# with col1:
#     st.markdown('<div class="dashboard-title">PSOUT File Path Plotter</div>', unsafe_allow_html=True)

# with col2:
#     st.markdown('<div style="font-weight:10px; margin-bottom:0.1rem;">Upload your .psout file</div>', unsafe_allow_html=True)
#     psout_file = st.file_uploader("", type=["psout"])

# with col3:
#     st.markdown('<div style="font-weight:10px; margin-bottom:0.1rem;">Upload your .xlsx file</div>', unsafe_allow_html=True)
#     excel_file = st.file_uploader("", type=["xlsx"])



# if psout_file is not None and excel_file is not None:
#     df_sconfg = pd.read_excel(excel_file, sheet_name="SConfig")
#     POI_Parameters = []
#     POI_Parameters_DDL = []

#     for i in range(1, len(df_sconfg)):
#         POI_Parameters.append('Root/' + df_sconfg['Canvas'][i] + '/' + df_sconfg['ParameterName'][i] + '/0')
#         POI_Parameters_DDL.append(df_sconfg['SignalType'][i] + '_' + df_sconfg['ParameterName'][i])


#     selected_path_temp = st.selectbox("Select a trace path to plot", POI_Parameters_DDL)
#     selected_path = POI_Parameters[POI_Parameters_DDL.index(selected_path_temp)]

#     with tempfile.NamedTemporaryFile(delete=False, suffix=".psout") as tmp:
#         tmp.write(psout_file.read())
#         tmp_path = tmp.name

#     try:
#         with mhi.psout.File(tmp_path) as file:
#             run = file.run(0)
#             tempchannel = file.call(selected_path)
#             for call in tempchannel.calls():
#                 trace2 = run.trace(call)
#                 time = trace2.domain

            
#             fig, ax = plt.subplots(figsize=(10, 5))
#             ax.plot(time.data, trace2.data)
#             ax.set_xlabel("Time")
#             ax.set_ylabel("Value")
#             ax.set_title(f"Trace Plot for {selected_path_temp}", fontsize=14, fontweight='bold')
#             ax.grid(True)

#             st.plotly_chart(fig, use_container_width=True)

#     except Exception as e:
#         st.error(f"Error reading or plotting trace: {e}")







# import streamlit as st
# import matplotlib.pyplot as plt
# import pandas as pd
# import mhi.psout
# import tempfile
# import openpyxl

# st.set_page_config("PSOUT Path Graph Viewer", layout="wide")


# st.markdown("""
#     <style>
#     div.block-container { padding-top: 1rem; }
#     .dashboard-title {
#         font-size: 2rem;
#         font-weight: 700;
#         color: white;
#         margin-bottom: 0.5rem;
#     }
#     .stFileUploader {
#         transform: scale(0.85);
#         width: 95% !important;
#     }
#     </style>
# """, unsafe_allow_html=True)




# col1, col2, col3 = st.columns(3)


# with col1:
#     st.markdown('<div class="dashboard-title">PSOUT File Path Plotter</div>', unsafe_allow_html=True)


# with col2:
#     st.markdown('<div style="font-weight:bold; margin-bottom:0.2rem;">Upload your .psout file</div>', unsafe_allow_html=True)
#     psout_file = st.file_uploader("", type=["psout"], label_visibility="collapsed")


# with col3:
#     st.markdown('<div style="font-weight:bold; margin-bottom:0.2rem;">Upload your .xlsx file</div>', unsafe_allow_html=True)
#     excel_file = st.file_uploader("", type=["xlsx"], label_visibility="collapsed")


# if psout_file is not None and excel_file is not None:
#     try:
#         df_sconfg = pd.read_excel(excel_file, sheet_name="SConfig")
#         POI_Parameters = []
#         POI_Parameters_DDL = []


#         for i in range(1, len(df_sconfg)):
#             POI_Parameters.append('Root/' + df_sconfg['Canvas'][i] + '/' + df_sconfg['ParameterName'][i] + '/0')
#             POI_Parameters_DDL.append(df_sconfg['SignalType'][i] + '_' + df_sconfg['ParameterName'][i])

        
#         selected_path_temp = st.multiselect("Select signals to plot", POI_Parameters_DDL)
#         selected_paths = [POI_Parameters[POI_Parameters_DDL.index(name)] for name in selected_path_temp]


#         if selected_paths:
#             with tempfile.NamedTemporaryFile(delete=False, suffix=".psout") as tmp:
#                 tmp.write(psout_file.read())
#                 tmp_path = tmp.name


#             with mhi.psout.File(tmp_path) as file:
#                 run = file.run(0)

                
#                 fig, ax = plt.subplots(figsize=(10, 5))

#                 for i, path in enumerate(selected_paths):
#                     tempchannel = file.call(path)
#                     for call in tempchannel.calls():
#                         trace = run.trace(call)
#                         time = trace.domain
#                         ax.plot(time.data, trace.data, label=selected_path_temp[i])

#                 ax.set_xlabel("Time", color='white', fontsize=18, fontweight='bold')
#                 ax.set_ylabel("Value", color='white', fontsize=18, fontweight='bold')
#                 ax.set_title("Trace Plot Signals", color='white', fontsize=26, fontweight='bold')
#                 ax.grid(True)
#                 # ax.legend()
#                 legend = ax.legend(frameon=True) 
#                 for text in legend.get_texts():
#                     text.set_color("white")
#                     text.set_fontweight("bold")
                    
#                 st.plotly_chart(fig, use_container_width=True)
#         else:
#             st.warning("Please select at least one signal to plot.")


#     except Exception as e:
#         st.error(f"Error reading or plotting trace: {e}")




# import streamlit as st
# import matplotlib.pyplot as plt
# import pandas as pd
# import mhi.psout
# import tempfile
# import openpyxl

# st.set_page_config("PSOUT Path Graph Viewer", layout="wide")

# # Custom CSS
# st.markdown("""
#     <style>
#     div.block-container { padding-top: 1rem; }
#     .dashboard-title {
#         font-size: 2rem;
#         font-weight: 700;
#         color: white;
#         margin-bottom: 0.5rem;
#     }
#     .stFileUploader {
#         transform: scale(0.85);
#         width: 95% !important;
#     }
#     </style>
# """, unsafe_allow_html=True)


# col1, col2, col3 = st.columns(3)


# with col1:
#     st.markdown('<div class="dashboard-title">PSOUT File Path Plotter</div>', unsafe_allow_html=True)


# with col2:
#     st.markdown('<div style="font-weight:bold; margin-bottom:0.2rem;">Upload your .psout file</div>', unsafe_allow_html=True)
#     psout_file = st.file_uploader("", type=["psout"], label_visibility="collapsed")


# with col3:
#     st.markdown('<div style="font-weight:bold; margin-bottom:0.2rem;">Upload your .xlsx file</div>', unsafe_allow_html=True)
#     excel_file = st.file_uploader("", type=["xlsx"], label_visibility="collapsed")


# # Main logic
# if psout_file is not None and excel_file is not None:
#     try:
#         df_sconfg = pd.read_excel(excel_file, sheet_name="SConfig")
#         POI_Parameters = []
#         POI_Parameters_DDL = []

#         for i in range(1, len(df_sconfg)):
#             POI_Parameters.append('Root/' + df_sconfg['Canvas'][i] + '/' + df_sconfg['ParameterName'][i] + '/0')
#             POI_Parameters_DDL.append(df_sconfg['SignalType'][i] + '_' + df_sconfg['ParameterName'][i])

#         selected_path_temp = st.multiselect("Select signals to plot", POI_Parameters_DDL)
#         selected_paths = [POI_Parameters[POI_Parameters_DDL.index(name)] for name in selected_path_temp]

#         if selected_paths:
#             with tempfile.NamedTemporaryFile(delete=False, suffix=".psout") as tmp:
#                 tmp.write(psout_file.read())
#                 tmp_path = tmp.name

#             with mhi.psout.File(tmp_path) as file:
#                 run = file.run(0)

#                 # Get common time domain from first selected path
#                 first_channel = file.call(selected_paths[0])
#                 first_trace = run.trace(next(first_channel.calls()))
#                 time = first_trace.domain

#                 fig, ax = plt.subplots(figsize=(10, 5))
#                 for i, path in enumerate(selected_paths):
#                     tempchannel = file.call(path)
#                     for call in tempchannel.calls():
#                         trace = run.trace(call)
#                         ax.plot(time.data, trace.data, label=selected_path_temp[i])

#                 # Graph formatting
#                 ax.set_facecolor("#111111")
#                 ax.set_xlabel("Time", color='white')
#                 ax.set_ylabel("Value", color='white')
#                 ax.set_title("Trace Plot Signals", fontsize=14, fontweight='bold', color='white')
#                 ax.tick_params(axis='x', colors='white')
#                 ax.tick_params(axis='y', colors='white')
#                 ax.grid(True)

#                 legend = ax.legend(facecolor="#222222", edgecolor="white", framealpha=1)
#                 for text in legend.get_texts():
#                     text.set_color("white")
#                     text.set_fontweight("bold")

#                 st.plotly_chart(fig, use_container_width=True)

#         else:
#             st.warning("Please select at least one signal to plot.")

#     except Exception as e:
#         st.error(f"Error reading or plotting trace: {e}")





import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import mhi.psout
import tempfile
import openpyxl

st.set_page_config("PSOUT Path Graph Viewer", layout="wide")


st.markdown("""
    <style>
    div.block-container { padding-top: 1rem; }
    .dashboard-title {
        font-size: 2rem;
        font-weight: 700;
        color: white;
        margin-bottom: 0.5rem;
    }
    .stFileUploader {
        transform: scale(0.85);
        width: 95% !important;
    }
    </style>
""", unsafe_allow_html=True)




col1, col2, col3 = st.columns(3)


with col1:
    st.markdown('<div class="dashboard-title">PSOUT File Path Plotter</div>', unsafe_allow_html=True)


with col2:
    st.markdown('<div style="font-weight:bold; font-size:10px; margin-bottom:0.1rem;">Upload your .psout file</div>', unsafe_allow_html=True)
    psout_file = st.file_uploader("", type=["psout"], label_visibility="collapsed")


with col3:
    st.markdown('<div style="font-weight:bold; font-size:10px; margin-bottom:0.2rem;">Upload your .xlsx file</div>', unsafe_allow_html=True)
    excel_file = st.file_uploader("", type=["xlsx"], label_visibility="collapsed")


if psout_file is not None and excel_file is not None:
    try:
        df_sconfg = pd.read_excel(excel_file, sheet_name="SConfig")
        POI_Parameters = []
        POI_Parameters_DDL = []


        for i in range(1, len(df_sconfg)):
            POI_Parameters.append('Root/' + df_sconfg['Canvas'][i] + '/' + df_sconfg['ParameterName'][i] + '/0')
            POI_Parameters_DDL.append(df_sconfg['SignalType'][i] + '_' + df_sconfg['ParameterName'][i])

        
        col1, col2, col3, col4, col5, col6 = st.columns(6)

        with col1:
            selected_path_temp = st.multiselect("Select signals to plot", POI_Parameters_DDL)

        with col2:
            selected_paths = [POI_Parameters[POI_Parameters_DDL.index(name)] for name in selected_path_temp]


        if selected_paths:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".psout") as tmp:
                tmp.write(psout_file.read())
                tmp_path = tmp.name


            with mhi.psout.File(tmp_path) as file:
                run = file.run(0)

                
                fig, ax = plt.subplots(figsize=(10, 5))

                for i, path in enumerate(selected_paths):
                    tempchannel = file.call(path)
                    for call in tempchannel.calls():
                        trace = run.trace(call)
                        time = trace.domain
                        ax.plot(time.data, trace.data, label=selected_path_temp[i])

                ax.set_xlabel("Time in Second", color='white', fontsize=18, fontweight='bold')
                ax.set_ylabel(f"{selected_path_temp}", color='white', fontsize=18, fontweight='bold')
                ax.set_title("Trace Plot Signals", color='white', fontsize=26, fontweight='bold')
                ax.grid(True)
                # ax.legend()
                legend = ax.legend(frameon=True) 
                for text in legend.get_texts():
                    text.set_color("white")
                    text.set_fontweight("bold")
                    
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Please select at least one signal to plot.")


    except Exception as e:
        st.error(f"Error reading or plotting trace: {e}")

