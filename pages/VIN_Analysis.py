import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# CSS Styling for prettier UI
st.markdown("""
    <style>
    /* General Page Styling */
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

    /* Styling for VIN Summary Section */
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

    /* Styling for the Claim Summary Table */
    .claim-summary {
        width: 100%;
        border-collapse: collapse;
        margin-top: 10px;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    }

    .claim-summary th {
        background-color: #002C61;
        color: white;
        padding: 10px;
        text-align: left;
    }

    .claim-summary td {
        padding: 10px;
        border-bottom: 1px solid #ddd;
        background-color: #f9f9f9;
    }

    .claim-summary tr:nth-child(even) td {
        background-color: #e0e7ef;
    }

    .claim-summary tr:hover td {
        background-color: #d1e4fc;
        color: #002C61;
        font-weight: bold;
    }

    .claim-summary-container {
        padding: 20px;
        border-radius: 10px;
        background-color: #fff;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-top: 10px;
    }

    /* Styling for Intelligence Analysis */
    .intelligence-bar {
        background-color: #DAA520;
        border-radius: 8px;
        padding: 10px;
        color: white;
        font-weight: bold;
        font-size: 18px;
        text-align: left;
        margin-top: 20px;
    }

    .intelligence-checkbox {
        display: flex;
        align-items: center;
        gap: 10px;
        font-size: 14px;
        padding: 10px;
        margin-bottom: 10px;
        background-color: #F8F9FA;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
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

    /* Custom styles for expander headers */
    .expander-header {
        background-color: #002C61;
        color: white;
        padding: 15px;
        border-radius: 10px;
        font-size: 18px;
        margin-bottom: 10px;
        cursor: pointer;
    }

    /* Colorful Expander box content */
    .expander-box {
        background-color: #f0f0f5;
        border-radius: 10px;
        margin-bottom: 23px;
        padding: 10px;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# VIN Summary Section
st.markdown("""
    <h2 style='text-align: left;'>VIN Analysis</h2>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <input type="text" class="search-bar" placeholder="Search">
        <div class="controls-section">
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
        </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns([1.25, 1])

# Claim Summary Section with Expander and Checkboxes
with st.expander("Claim Summary", expanded=True):
    st.markdown("""
        <div class="expander-box">
            <table class="claim-summary">
                <thead>
                    <tr>
                        <th></th> <!-- For checkbox -->
                        <th>Claim Number</th>
                        <th>Claim Open Date</th>
                        <th>Part Name</th>
                        <th>Issue Category</th>
                        <th>Supplier Name</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><input type="checkbox"></td>
                        <td>53135105</td>
                        <td>Aug 13, 2024</td>
                        <td>Fuel Tank</td>
                        <td>Filter Issue</td>
                        <td>Decostar</td>
                        <td><button>View</button></td>
                    </tr>
                    <tr>
                        <td><input type="checkbox"></td>
                        <td>46893086</td>
                        <td>Aug 13, 2024</td>
                        <td>Front Wheel</td>
                        <td>Front Wheel Alignment</td>
                        <td>ABC Corp</td>
                        <td><button>View</button></td>
                    </tr>
                    <tr>
                        <td><input type="checkbox"></td>
                        <td>46893237</td>
                        <td>Aug 13, 2024</td>
                        <td>Engine</td>
                        <td>Oil Leak Issue</td>
                        <td>Nissan</td>
                        <td><button>View</button></td>
                    </tr>
                </tbody>
            </table>
        </div>
    """, unsafe_allow_html=True)

# Intelligence Analysis Section with Gold Bar
st.markdown("""
    <div class="intelligence-bar">Intelligence Analysis</div>
""", unsafe_allow_html=True)

# Intelligence Analysis Section content
st.markdown("""
    <div class="expander-box">
        <div class="intelligence-checkbox">
            <input type="checkbox" checked> Summarization: Summarizing Vehicle information & Parts issues related complaints from customer or service advisor and dealer or technician comments
        </div>
        <div class="intelligence-checkbox">
            <input type="checkbox" checked> RCA Classification (Root Cause Category): Identifying Root Cause Category for each part based on customer complaints and dealer comments
        </div>
        <button class="run-button">Run</button>
    </div>
""", unsafe_allow_html=True)

# Parts Summary Section
with st.expander("Parts Summary", expanded=False):
    part_summary_html = """
        <div class="expander-box">
            <div style="width: 100%; border-radius: 10px; padding: 10px; margin-top: 20px; background-color: #f9f9f9;">
                <div style="background-color: #7483a2; color: white; padding: 10px; border-radius: 8px 8px 0 0; display: flex; justify-content: space-between; align-items: center;">
                    <div style="font-size: 16px; font-weight: bold;">01 Parts Name: Fuel Pump</div>
                    <div style="font-size: 16px; font-weight: bold;">Supplier Name: Decostar</div>
                </div>
                <div style="border: 1px solid #ddd; border-radius: 8px; padding: 10px; background-color: white; margin-top: 10px;">
                    <strong style="cursor: pointer;">View Details</strong>
                    <div style="margin-top: 10px;">
                        <div style="padding: 15px; background-color: #f0f5ff; border-radius: 8px;">
                            <strong>Customer/Service Advisor Complaint</strong><br>
                            Filter issue in the fuel pumping system, leading to excess fuel consumption and engine noise over 50 mph.
                        </div>
                        <div style="padding: 15px; background-color: #f0f5ff; border-radius: 8px; margin-top: 10px;">
                            <strong>Dealer/Technician Comments</strong><br>
                            Need to change the filter in the fuel pump due to leakage issues.
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-top: 10px;">
                            <div style="background-color: #e6f7ff; border-radius: 8px; padding: 10px; width: 48%;">
                                <strong>Issue Summary</strong><br>
                                Fuel pump filter issue & change the filter.
                            </div>
                            <div style="background-color: #e6f7ff; border-radius: 8px; padding: 10px; width: 48%;">
                                <strong>Root Cause Category</strong><br>
                                Filter design issue.
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Second Part Summary -->
                <div style="background-color: #7483a2; color: white; padding: 10px; border-radius: 8px; margin-top: 20px; display: flex; justify-content: space-between; align-items: center;">
                    <div style="font-size: 16px; font-weight: bold;">02 Parts Name: Music System</div>
                    <div style="font-size: 16px; font-weight: bold;">Supplier Name: Kasai North America</div>
                </div>

                <div style="border: 1px solid #ddd; border-radius: 8px; padding: 10px; background-color: white; margin-top: 10px;">
                    <strong style="cursor: pointer;">View Details</strong>
                    <div style="margin-top: 10px;">
                        <div style="padding: 15px; background-color: #f0f5ff; border-radius: 8px;">
                            <strong>Customer/Service Advisor Complaint</strong><br>
                            Audio system producing distortion when volume is raised above 70%.
                        </div>
                        <div style="padding: 15px; background-color: #f0f5ff; border-radius: 8px; margin-top: 10px;">
                            <strong>Dealer/Technician Comments</strong><br>
                            Need to replace speakers as sound quality is degraded.
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-top: 10px;">
                            <div style="background-color: #e6f7ff; border-radius: 8px; padding: 10px; width: 48%;">
                                <strong>Issue Summary</strong><br>
                                Speaker malfunction & need replacement.
                            </div>
                            <div style="background-color: #e6f7ff; border-radius: 8px; padding: 10px; width: 48%;">
                                <strong>Root Cause Category</strong><br>
                                Speaker design issue.
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    """
components.html(part_summary_html, height=700)
