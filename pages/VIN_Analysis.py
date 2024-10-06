import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
    <style>
    .search-bar {
        width: 75%;
        padding: 10px;
        border-radius: 4px;
        border: 1px solid #ddd;
        font-size: 14px;
        margin-bottom: 20px;
        margin-right: 20px;
    }

    .controls-section {
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .control-item button {
        background-color: #002C61;
        border: 1px solid #E0E0E0;
        padding: 6px 12px;
        border-radius: 4px;
        color: white;
        cursor: pointer;
        font-size: 14px;
    }

    .control-item button:hover {
        background-color: #002C61;
    }

    .vin-summary-header {
        background-color: #7483a2;
        color: white;
        padding: 10px;
        border-radius: 8px;
        margin-top: 10px;
        font-weight: bold;
    }

    .vin-summary-content {
        background-color: white;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #ddd;
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;
    }

    .vin-item {
        background-color: #f7f7f7;
        padding: 12px;
        border-radius: 8px;
        text-align: left;
    }

    .claim-summary-container, .intelligence-container-title {
        background-color: #7483a2;
        border-radius: 8px;
        padding: 10px;
        color: white;
        margin-top: 10px;
    }

    .claim-summary, .intelligence-container {
        width: 100%;
        border-collapse: collapse;
        margin-top: 10px;
    }

    .claim-summary th, .claim-summary td {
        padding: 10px;
        text-align: left;
        border-bottom: 1px solid #ddd;
    }

    .claim-summary th {
        background-color: #7483a2;
        color: white;
    }

    .intelligence-item {
        background-color: #f7f7f7;
        border-radius: 8px;
        padding: 10px;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .intelligence-item span {
        font-size: 14px;
        color: #333;
    }

    .intelligence-item input {
        margin-right: 10px;
    }

    .run-button {
        background-color: #002C61;
        color: white;
        padding: 10px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        width: 100%;
        margin-bottom: 23px;
        font-size: 16px;
        font-weight: bold;
    }

    .details-box {
        background-color: #f7f7f7;
        border-radius: 8px;
        padding: 15px;
        margin-top: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    .details-header {
        background-color: #002C61;
        color: white;
        padding: 10px;
        font-size: 16px;
        border-radius: 8px 8px 0 0;
    }

    .details-content {
        padding: 15px;
        border-radius: 0 0 8px 8px;
        background-color: white;
        margin: 10px 0 0 0;
        border: 1px solid #ddd;
    }

    .expander-content {
        margin-top: 30px;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #ddd;
    }

    .st-expander {
        margin-top: 30px !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <h2 style='text-align: left;'>VIN Analysis</h2>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <input type="text" class="search-bar" placeholder="Search">
        <div class="controls-section">
            <div class="control-item">
                <button>Custom Date Range</button>
            </div>
            <div class="control-item">
                <button>Filter</button>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

with st.expander("VIN Summary", expanded=True):
    st.markdown("""
        <div class="vin-summary-content">
            <div class="vin-item">
                <strong>VIN Number:</strong><br>224567894
            </div>
            <div class="vin-item">
                <strong>Model Year:</strong><br>2020
            </div>
            <div class="vin-item">
                <strong>Color:</strong><br>Blue
            </div>
            <div class="vin-item">
                <strong>Country:</strong><br>United States
            </div>
            <div class="vin-item">
                <strong>Engine Model Code:</strong><br>VQ37
            </div>
            <div class="vin-item">
                <strong>Engine Serial Number:</strong><br>246897457
            </div>
            <div class="vin-item">
                <strong>Miles Driven:</strong><br>24
            </div>
            <div class="vin-item">
                <strong>KM Driven:</strong><br>40
            </div>
            <div class="vin-item">
                <strong>Mfg Date:</strong><br>13 August 2024
            </div>
            <div class="vin-item">
                <strong>Purchase Date:</strong><br>13 November 2024
            </div>
            <div class="vin-item">
                <strong>Shipment Date:</strong><br>24 November 2024
            </div>
        </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns([1.25, 1])

with col1:
    st.markdown("""
    <div class="claim-summary-container">Claim Summary</div>
    <table class="claim-summary">
        <thead>
            <tr>
                <th>Claim Number</th>
                <th>Claim Type</th>
                <th>Claim Reported Date</th>
                <th>Part Name</th>
                <th>Supplier Name</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>76089911</td>
                <td>76089911</td>
                <td>2024-01-01</td>
                <td>Fuel Tank</td>
                <td>Deca Motors</td>
            </tr>
            <tr>
                <td>76089911</td>
                <td>76089911</td>
                <td>2024-01-01</td>
                <td>Front Wheel</td>
                <td>ABC Corp</td>
            </tr>
            <tr>
                <td>76089911</td>
                <td>76089911</td>
                <td>2024-01-01</td>
                <td>Engine</td>
                <td>ADC Motors Inc.</td>
            </tr>
        </tbody>
    </table>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="intelligence-container-title">Intelligence Analysis</div>
    <div class="intelligence-container">
        <div class="intelligence-item">
            <div>
                <input type="checkbox" checked>
                <span>Summary: Summarizing Vehicle information & Parts issues related complaints from customer or service advisor and dealer or technician comments parts level</span>
            </div>
        </div>
        <div class="intelligence-item">
            <div>
                <input type="checkbox" checked>
                <span>Root Cause Analysis: Summarizing Vehicle information & Parts issues related complaints from customer or service advisor and dealer or technician comments parts level</span>
            </div>
        </div>
        <button class="run-button">Run</button>
    </div>
    """, unsafe_allow_html=True)

with st.expander("Parts Summary", expanded=True):
    selected_part = st.selectbox(
        "Show Details for the following parts:",
        ["Fuel Pump", "Music System"],
        key="parts-summary"
    )

    if selected_part == "Fuel Pump":
        st.markdown("""
            <div class="details-box">
                <div class="details-header">Parts Name: Fuel Pump</div>
                <div class="details-content">
                    <strong>Supplier Name:</strong> Decostar<br>
                    <strong>Customer/Service Advisor Complaint:</strong> Filter issue in fuel pumping system which leads to excess fuel consumption and producing engine noise when crossing speed limit more than 50mph.<br>
                    <strong>Dealer/Technician Comments:</strong> Need to change the filter in fuel pump as it’s leaking.<br>
                    <strong>Issue Summary:</strong> Fuel pump filter issue & change the filter.<br>
                    <strong>Root Cause Category:</strong> Filter design issue.
                </div>
            </div>
        """, unsafe_allow_html=True)

    elif selected_part == "Music System":
        st.markdown("""
            <div class="details-box">
                <div class="details-header">Parts Name: Music System</div>
                <div class="details-content">
                    <strong>Supplier Name:</strong> Kasai North America<br>
                    <strong>Customer/Service Advisor Complaint:</strong> Audio system producing distortion when volume is raised above 70%.<br>
                    <strong>Dealer/Technician Comments:</strong> Need to replace speakers as sound quality is degraded.<br>
                    <strong>Issue Summary:</strong> Speaker malfunction & need replacement.<br>
                    <strong>Root Cause Category:</strong> Speaker design issue.
                </div>
            </div>
        """, unsafe_allow_html=True)
