import streamlit as st
import pandas as pd
import re
import os

# =========================
# Page Config
# =========================
st.set_page_config(page_title="📐 Land Area Calculator", layout="wide")
st.title("📐 Land Area Calculator")
st.markdown("Easily calculate **total land area** from your Excel file in **Acres and Guntas**.")

# =========================
# Tabs
# =========================
tab1, tab2 = st.tabs(["🔹 Single Column (Delimited)", "🔹 Separate Acres & Guntas Columns"])

# =========================
# TAB 1: Single Column
# =========================
with tab1:
    st.markdown("""
    ### 📌 Method 1: Single Column with Delimiter  
    Example: `5-20` (5 Acres, 20 Guntas) or `10:15`.
    """)

    uploaded_file = st.file_uploader("📂 Upload your Excel file", type=["xls", "xlsx", "xlsm", "xlsb"], key="file1")

    if uploaded_file:
        try:
            # Step 0: List all sheets
            excel_file = pd.ExcelFile(uploaded_file)
            sheet_name = st.selectbox("📑 Select Sheet", excel_file.sheet_names, key="sheet1")

            # Step 1: Ask user for header row number
            temp_df = pd.read_excel(uploaded_file, sheet_name=sheet_name, header=None)
            st.subheader("🗂 Select Header Row")
            header_row = st.number_input(
                "Select which row contains column names (1 = first row)",
                min_value=1,
                max_value=len(temp_df),
                value=1,
                key="hdr1"
            ) - 1

            # Step 2: Read Excel with chosen header row & sheet
            df = pd.read_excel(uploaded_file, sheet_name=sheet_name, header=header_row)
            df.index = df.index + 1  # start index from 1

            col_preview, col_controls = st.columns([4, 1])

            with col_preview:
                st.subheader(f"The number of row(s) are {df.shape[0]}, column(s) are {df.shape[1]}")
                st.subheader("📄 File Preview (First 5 Rows)")
                st.dataframe(df.head(), use_container_width=True)

            with col_controls:
                st.subheader("⚙️ Settings")
                column_name = st.selectbox("Select the Area Column", df.columns, key="col1")

                # Auto-detect delimiters
                possible_delimiters = []
                if column_name:
                    sample_values = df[column_name].dropna().astype(str).head(50).tolist()
                    delimiter_pattern = r"[^0-9\s]"  # non-digit, non-space
                    delimiters_found = set()

                    for val in sample_values:
                        matches = re.findall(delimiter_pattern, val)
                        delimiters_found.update(matches)

                    possible_delimiters = sorted(list(delimiters_found))

                selected_delimiter = st.selectbox(
                    "Select the delimiter (if any)",
                    options=[""] + possible_delimiters,
                    key="sel_delim"
                )

                manual_delimiter = st.text_input("Or enter a delimiter manually", "", key="man_delim")

                if st.button("📏 Calculate Total Area", key="calc1"):
                    try:
                        delimiter = manual_delimiter.strip() if manual_delimiter else selected_delimiter.strip()

                        if delimiter:  # If delimiter is provided
                            split_df = df[column_name].astype(str).str.split(delimiter, expand=True)
                            split_df[0] = pd.to_numeric(split_df[0], errors='coerce').fillna(0).astype(int)
                            split_df[1] = pd.to_numeric(split_df[1], errors='coerce').fillna(0).astype(int)

                            total_acres = split_df[0].sum()
                            total_guntas = split_df[1].sum()
                            total_acres += total_guntas // 40
                            remaining_guntas = total_guntas % 40
                        else:  # No delimiter, treat as numeric value in acres
                            total_acres = pd.to_numeric(df[column_name], errors='coerce').fillna(0).sum()
                            remaining_guntas = 0

                        st.success(f"📐 **Total Area:** {total_acres} Acres and {remaining_guntas} Guntas")

                    except Exception as e:
                        st.error(f"❌ Error while processing: {e}")

        except Exception as e:
            st.error(f"❌ Failed to read file: {e}")
    else:
        st.info("👆 Please upload an Excel file to start.")

# =========================
# TAB 2: Separate Acres & Guntas Columns
# =========================
with tab2:
    st.markdown("""
    ### 📌 Method 2: Separate Columns for Acres & Guntas  
    Example: One column for **Acres** and another for **Guntas**.
    """)

    uploaded_file2 = st.file_uploader("📂 Upload Excel File", type=["xlsx", "xls", "xlsm", "xlsb"], key="file2")

    def load_excel(file, header_row, sheet_name):
        """Load Excel with chosen header row & sheet."""
        file_ext = os.path.splitext(file.name)[-1].lower()
        try:
            if file_ext in [".xlsx", ".xls", ".xlsm"]:
                return pd.read_excel(file, sheet_name=sheet_name, header=header_row, engine="openpyxl" if file_ext == ".xlsx" else None)
            elif file_ext == ".xlsb":
                try:
                    return pd.read_excel(file, sheet_name=sheet_name, header=header_row, engine="pyxlsb")
                except ImportError:
                    st.error("❌ Please install `pyxlsb` to read .xlsb files.\nRun: `pip install pyxlsb`")
                    return None
            else:
                st.error(f"❌ Unsupported file format: {file_ext}")
                return None
        except Exception as e:
            st.error(f"❌ Error reading file: {e}")
            return None

    if uploaded_file2 is not None:
        # Step 0: List sheets
        excel_file2 = pd.ExcelFile(uploaded_file2)
        sheet_name2 = st.selectbox("📑 Select Sheet", excel_file2.sheet_names, key="sheet2")

        st.subheader("📌 Step 1: Header Row Selection (Optional)")
        header_row_ui = st.number_input(
            "Row number containing column headers (1 = first row in file)",
            min_value=1, value=1, step=1, key="hdr2"
        )

        header_row = header_row_ui - 1
        df2 = load_excel(uploaded_file2, header_row, sheet_name2)

        if df2 is not None:
            st.subheader(f"The number of row(s) are {df2.shape[0]}, column(s) are {df2.shape[1]}")
            st.success(f"✅ File loaded successfully (Sheet '{sheet_name2}', Row {header_row_ui} as header).")

            left_col, right_col = st.columns([4, 1])
            
            with left_col:
                st.subheader("📊 Data Preview (First 5 Rows)")
                st.dataframe(df2.head(), use_container_width=True)

            with right_col:
                st.subheader("⚙️ Step 2: Select Columns")
                acre_col = st.selectbox("Select Acres Column", options=df2.columns, key="acre_col")
                gunta_col = st.selectbox("Select Guntas Column", options=df2.columns, key="gunta_col")

                if st.button("📏 Calculate Area", key="calc2"):
                    df2[acre_col] = pd.to_numeric(df2[acre_col], errors='coerce').fillna(0)
                    df2[gunta_col] = pd.to_numeric(df2[gunta_col], errors='coerce').fillna(0)

                    total_acres = df2[acre_col].sum()
                    total_guntas = df2[gunta_col].sum()

                    extra_acres = total_guntas // 40
                    remaining_guntas = total_guntas % 40
                    total_acres += extra_acres

                    st.success(f"📐 **Total Area:** {total_acres} Acres and {remaining_guntas} Guntas")
    else:
        st.info("📥 Please upload an Excel file to begin.")
