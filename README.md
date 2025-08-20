# 📐 Agri-Extent Calsi: The Smart Land Area Calculator

Tired of manually adding up land areas from messy spreadsheets? 😫 This handy Streamlit web app automates the process, letting you calculate the total land area in **Acres and Guntas** directly from your Excel files. No more manual math, no more errors\!



## ✨ Live Demo

### [🚀 Launch the Land Area Calculator\!](https://agri-extent-calsi.streamlit.app/)



-----

## 🌟 Key Features

  * **Two Convenient Modes:** Whether your data is in a single column (e.g., `5-20`) or in separate 'Acres' and 'Guntas' columns, this app has you covered.
  * **Smart Delimiter Detection:** Automatically finds common delimiters like `-`, `:`, or `.` in your single-column data. You can also specify one manually.
  * **Flexible Excel Support:** Upload your data in various formats, including `.xlsx`, `.xls`, `.xlsm`, and `.xlsb`.
  * **User-Friendly Interface:** Clean, simple, and intuitive. Select your sheet, header row, and columns with ease.
  * **Instant & Accurate Results:** Get the total area calculated in seconds.

-----

## 📖 How It Works

The app offers two simple methods based on how your Excel file is structured.

### 📌 Method 1: Single Column (Delimited)

Perfect for files where Acres and Guntas are combined in one column.

**Example Excel Data:**

> | Survey\_No | Extent\_Ac-G |
> | :--- | :--- |
> | 101 | 5-20 |
> | 102 | 10.15 |
> | 103 | 2:05 |

**Steps:**

1.  Go to the **"🔹 Single Column (Delimited)"** tab.
2.  📂 **Upload** your Excel file.
3.  📑 Select the correct **Sheet** and the **Header Row** number.
4.  ⚙️ Choose the column containing the area (e.g., `Extent_Ac-G`).
5.  The app will try to auto-detect the delimiter (`-`, `.`, `:`). If needed, select the correct one or enter it manually.
6.  Click **"📏 Calculate Total Area"** to get your result\!

### 📌 Method 2: Separate Acres & Guntas Columns

Ideal for files where Acres and Guntas have their own dedicated columns.

**Example Excel Data:**

> | Survey\_No | Acres | Guntas |
> | :--- | :--- | :--- |
> | 101 | 5 | 20 |
> | 102 | 10 | 15 |
> | 103 | 2 | 5 |

**Steps:**

1.  Go to the **"🔹 Separate Acres & Guntas Columns"** tab.
2.  📂 **Upload** your Excel file.
3.  📑 Select the correct **Sheet** and the **Header Row** number.
4.  ⚙️ Select the **Acres Column** and the **Guntas Column** from the dropdowns.
5.  Click **"📏 Calculate Area"** and you're done\!

-----

## 🛠️ Technology Stack

This project is built with a simple but powerful stack:

  * **🐍 Python:** The core programming language.
  * **🎈 Streamlit:** For creating the interactive web application.
  * **🐼 Pandas:** For powerful and fast data manipulation from your Excel files.

-----

## 🚀 How to Run Locally

Want to run this app on your own machine? It's easy\!

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/apkanisandeep01/Agri-extent-calsi.git
    cd Agri-extent-calsi
    ```

2.  **Install the required libraries:**

    ```bash
    pip install streamlit pandas openpyxl pyxlsb
    ```

3.  **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

    Your web browser will automatically open with the application running.

-----

## 🤝 Feedback & Contributions

Have an idea to make this better? Found a bug? Feel free to open an issue or submit a pull request. All contributions are welcome\!
