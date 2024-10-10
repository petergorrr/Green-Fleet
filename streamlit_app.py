import time
import streamlit as st
import pandas as pd

# Set the page configuration
st.set_page_config(
    page_title="Fleet Decarbonization & Carbon Accounting", page_icon="🌍", layout="wide")

# Sidebar for Navigation
st.sidebar.markdown("# Navigation", unsafe_allow_html=True)
page = st.sidebar.radio(
    "Explore", ["Home", "Fleet Optimizer", "About Me"], index=0)

# Sidebar Footer
st.sidebar.markdown("<hr style='border:1px solid #007bff;'>",
                    unsafe_allow_html=True)
st.sidebar.info(" Green Fleet © Malaysia 2024")

# Streamlit Styling
st.markdown("""
    <style>
        .main-header { font-size: 32px; color: #007bff; text-align: center; font-weight: bold; }
        .sub-header { font-size: 24px; color: #0056b3; margin-top: 20px; margin-bottom: 10px; }
        .text-content { font-size: 18px; line-height: 1.6; }
        .highlight { color: #ff5722; font-weight: bold; }
        .data-section { margin-top: 30px; padding: 20px; background-color: #f9f9f9; border-radius: 10px; }
        .button-style { background-color: #28a745; color: white; font-size: 18px; padding: 10px 20px; }
        .budget-box { background-color: #1F3B4D; padding: 30px; border-radius: 15px; margin-top: 30px; text-align: center; color: white;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3); max-width: 500px; margin-left: auto; margin-right: auto; }
        .budget-text { font-size: 26px; font-weight: bold; color: #2ECC71; margin-bottom: 10px; }
        .budget-value { font-size: 40px; font-weight: bold; color: #3498DB; }
        .csv-button { display: block; margin-top: 15px; }
        .emission-status { font-size: 22px; margin-top: 10px; padding: 15px; border-radius: 8px; color: white; text-align: center; }
        .within-limit { background-color: #2ECC71; }
        .exceed-limit { background-color: #E74C3C; }
    </style>
""", unsafe_allow_html=True)

# Page Content
if page == "Home":
    st.markdown('<div class="main-header">🚚 Green Fleet 🌿</div>',
                unsafe_allow_html=True)
    st.markdown("""
        <div class="text-content">
        Welcome to Green Fleet—an advanced <span class="highlight">Fleet Decarbonization Optimizer</span> designed to empower Malaysian businesses 
        to achieve their sustainability goals. Our solution seamlessly integrates <span class="highlight">Carbon Accounting</span> with cutting-edge 
        <span class="highlight">Fleet Optimization</span> strategies to reduce greenhouse gas emissions and operational costs.
        <br><br>By leveraging <span class="highlight">Computational Intelligence</span>, we provide data-driven insights and optimizations, 
        aligning your fleet's efficiency with Malaysia's renewable energy goals.
        This platform facilitates a smooth transition to a greener, more sustainable future.
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sub-header">Key Technologies</div>',
                unsafe_allow_html=True)
    st.markdown("""
        - 🤖 **AI Analytics**: Leverages machine learning to analyze fleet performance and predict optimal strategies.
        - 🌿 **Carbon Accounting**: Calculates GHG emissions and identifies reduction opportunities.
        - 🧠 **Computational Intelligence**: Uses evolutionary algorithms to optimize fleet configurations.
        - 🚗 **Sustainable Fleet Management**: Promotes the adoption of electric and low-emission vehicles.
    """, unsafe_allow_html=True)

elif page == "Fleet Optimizer":
    st.markdown('<div class="main-header">Optimize Your Fleet for a Sustainable Future</div>',
                unsafe_allow_html=True)

    st.markdown("""
        <style>
        .optimizer-info {
            background-color: #2C3E50; padding: 15px; border-radius: 8px; color: white; margin-bottom: 20px;
        }
        .file-upload-section {
            background-color: #f9f9f9; padding: 20px; border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); margin-bottom: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="optimizer-info">Please upload a CSV file containing your fleet information. The file should include columns such as "ID", "Vehicle Type", "Size", "Year", "Cost", "Yearly Range", and "Distance".</div>', unsafe_allow_html=True)

    fleet_file = st.file_uploader("Upload Fleet Information Dataset (CSV)", type=[
                                  "csv"], key="fleet_csv")

    if fleet_file:
        df = pd.read_csv(fleet_file)
        st.markdown('<div class="file-upload-section">',
                    unsafe_allow_html=True)
        if st.button("View Uploaded Dataset"):
            st.dataframe(df)

    # Input fields for emission limits for each year
    st.markdown("<h3>Carbon Emission Limit for 5 Years</h3>",
                unsafe_allow_html=True)
    emission_limits = [st.text_input(
        f"Carbon Emission Limit for Year {i+1} (kg CO2)", value="100,000") for i in range(5)]

    # Placeholder for optimization status
    status_placeholder = st.empty()

    if st.button("Optimize Fleet 🚀", key="optimize_button"):
        status_placeholder.markdown(
            "Running optimization... Please wait.", unsafe_allow_html=True)

        time.sleep(1.2)

        status_placeholder.success("Optimization Completed!")

        # Hardcoded optimization result for illustration
        # Example quota for each year
        emission_quotas = [5000, 4800, 4600, 4400, 4200]

        best_solution = {
            1: {
                'buy': [
                    {'Vehicle ID': 'V101', 'Vehicle Type': 'Electric Truck', 'Size': 'Large',
                     'Cost (MYR)': 250000, 'Carbon Emissions (kg CO2)': 400},
                    {'Vehicle ID': 'V102', 'Vehicle Type': 'Hybrid Van', 'Size': 'Medium',
                     'Cost (MYR)': 180000, 'Carbon Emissions (kg CO2)': 320}
                ],
                'retain': [
                    {'Vehicle ID': 'R201', 'Vehicle Type': 'Diesel Truck', 'Size': 'Large',
                     'Cost (MYR)': 500000, 'Carbon Emissions (kg CO2)': 1500},
                    {'Vehicle ID': 'R202', 'Vehicle Type': 'Electric Car', 'Size': 'Small',
                     'Cost (MYR)': 120000, 'Carbon Emissions (kg CO2)': 100}
                ],
                'dispose': [
                    {'Vehicle ID': 'D301', 'Vehicle Type': 'Old Diesel Van',
                     'Size': 'Small', 'Cost (MYR)': 8000, 'Carbon Emissions (kg CO2)': 900}
                ]
            },
            2: {
                'buy': [
                    {'Vehicle ID': 'V103', 'Vehicle Type': 'Electric Truck', 'Size': 'Large',
                     'Cost (MYR)': 260000, 'Carbon Emissions (kg CO2)': 350},
                    {'Vehicle ID': 'V104', 'Vehicle Type': 'Hybrid SUV', 'Size': 'Medium',
                     'Cost (MYR)': 220000, 'Carbon Emissions (kg CO2)': 400}
                ],
                'retain': [
                    {'Vehicle ID': 'R203', 'Vehicle Type': 'Electric Van', 'Size': 'Medium',
                     'Cost (MYR)': 210000, 'Carbon Emissions (kg CO2)': 200},
                    {'Vehicle ID': 'R204', 'Vehicle Type': 'Diesel Truck', 'Size': 'Large',
                     'Cost (MYR)': 480000, 'Carbon Emissions (kg CO2)': 1400}
                ],
                'dispose': [
                    {'Vehicle ID': 'D302', 'Vehicle Type': 'Old Diesel Truck',
                     'Size': 'Large', 'Cost (MYR)': 15000, 'Carbon Emissions (kg CO2)': 1600}
                ]
            },
            3: {
                'buy': [
                    {'Vehicle ID': 'V105', 'Vehicle Type': 'Electric Car', 'Size': 'Small',
                     'Cost (MYR)': 130000, 'Carbon Emissions (kg CO2)': 80},
                    {'Vehicle ID': 'V106', 'Vehicle Type': 'Hybrid Truck', 'Size': 'Large',
                     'Cost (MYR)': 290000, 'Carbon Emissions (kg CO2)': 500}
                ],
                'retain': [
                    {'Vehicle ID': 'R205', 'Vehicle Type': 'Electric Van', 'Size': 'Medium',
                     'Cost (MYR)': 230000, 'Carbon Emissions (kg CO2)': 180},
                    {'Vehicle ID': 'R206', 'Vehicle Type': 'Diesel Van', 'Size': 'Medium',
                     'Cost (MYR)': 180000, 'Carbon Emissions (kg CO2)': 900}
                ],
                'dispose': [
                    {'Vehicle ID': 'D303', 'Vehicle Type': 'Old Diesel SUV', 'Size': 'Medium',
                     'Cost (MYR)': 20000, 'Carbon Emissions (kg CO2)': 1200}
                ]
            },
            4: {
                'buy': [
                    {'Vehicle ID': 'V107', 'Vehicle Type': 'Electric SUV', 'Size': 'Medium',
                     'Cost (MYR)': 250000, 'Carbon Emissions (kg CO2)': 150},
                    {'Vehicle ID': 'V108', 'Vehicle Type': 'Hybrid Truck', 'Size': 'Large',
                     'Cost (MYR)': 300000, 'Carbon Emissions (kg CO2)': 450}
                ],
                'retain': [
                    {'Vehicle ID': 'R207', 'Vehicle Type': 'Diesel Truck', 'Size': 'Large',
                     'Cost (MYR)': 510000, 'Carbon Emissions (kg CO2)': 1300},
                    {'Vehicle ID': 'R208', 'Vehicle Type': 'Electric Car', 'Size': 'Small',
                     'Cost (MYR)': 140000, 'Carbon Emissions (kg CO2)': 90}
                ],
                'dispose': [
                    {'Vehicle ID': 'D304', 'Vehicle Type': 'Old Diesel Van',
                     'Size': 'Small', 'Cost (MYR)': 7000, 'Carbon Emissions (kg CO2)': 850}
                ]
            },
            5: {
                'buy': [
                    {'Vehicle ID': 'V109', 'Vehicle Type': 'Electric Truck', 'Size': 'Large',
                     'Cost (MYR)': 280000, 'Carbon Emissions (kg CO2)': 320},
                    {'Vehicle ID': 'V110', 'Vehicle Type': 'Electric SUV', 'Size': 'Medium',
                     'Cost (MYR)': 260000, 'Carbon Emissions (kg CO2)': 200}
                ],
                'retain': [
                    {'Vehicle ID': 'R209', 'Vehicle Type': 'Hybrid Truck', 'Size': 'Large',
                     'Cost (MYR)': 320000, 'Carbon Emissions (kg CO2)': 1000},
                    {'Vehicle ID': 'R210', 'Vehicle Type': 'Electric Van', 'Size': 'Medium',
                     'Cost (MYR)': 220000, 'Carbon Emissions (kg CO2)': 150}
                ],
                'dispose': [
                    {'Vehicle ID': 'D305', 'Vehicle Type': 'Old Diesel Truck',
                     'Size': 'Large', 'Cost (MYR)': 10000, 'Carbon Emissions (kg CO2)': 1800}
                ]
            }
        }

        total_budget = 0  # Track total budget
        for year in range(1, 6):
            st.markdown(f"### Year {year}")
            total_emissions = 0  # Track total emissions for each year

            for action in ["buy", "retain", "dispose"]:
                action_data = best_solution.get(year, {}).get(action, [])
                df_action = pd.DataFrame(action_data) if action_data else pd.DataFrame(
                    columns=['Vehicle ID', 'Vehicle Type', 'Size', 'Cost (MYR)', 'Carbon Emissions (kg CO2)'])
                st.markdown(f"**Vehicles to {action.capitalize()}:**")
                st.table(df_action)

                # Sum up emissions for the year
                total_emissions += df_action['Carbon Emissions (kg CO2)'].sum()

                if action == "buy":
                    total_budget += df_action['Cost (MYR)'].sum()

            # Compare the emissions with the quota
            st.markdown(
                f"#### Emission Quota for Year {year}: {emission_quotas[year-1]} kg CO2")
            st.markdown(
                f"#### Total Carbon Emissions for Year {year}: {total_emissions} kg CO2")

            # Display whether the emissions are within the limit
            if total_emissions <= emission_quotas[year-1]:
                st.markdown(
                    f'<div class="emission-status within-limit">✅ Within Emission Quota</div>', unsafe_allow_html=True)
            else:
                st.markdown(
                    f'<div class="emission-status exceed-limit">❌ Exceeded Emission Quota</div>', unsafe_allow_html=True)

        st.markdown(f"""
            <div class="budget-box">
                <div class="budget-text">Estimated Budget:</div>
                <div class="budget-value">{total_budget:,.0f} MYR</div>
            </div>
        """, unsafe_allow_html=True)

        # Download CSV button
        if st.button("Download Results as CSV"):
            flattened_results = []
            for year, actions in best_solution.items():
                for action, vehicles in actions.items():
                    for vehicle in vehicles:
                        flattened_results.append({
                            'Year': year, 'Action': action.capitalize(),
                            'Vehicle ID': vehicle['Vehicle ID'], 'Vehicle Type': vehicle['Vehicle Type'],
                            'Size': vehicle['Size'], 'Cost (MYR)': vehicle['Cost (MYR)'],
                            'Carbon Emissions (kg CO2)': vehicle['Carbon Emissions (kg CO2)']
                        })
            results_df = pd.DataFrame(flattened_results)
            csv = results_df.to_csv(index=False).encode('utf-8')
            st.download_button("Download Results as CSV", csv, "fleet_optimization_results.csv",
                               "text/csv", key='download-csv', class_="csv-button")

elif page == "About Me":
    st.markdown('<div class="main-header">About Me</div>',
                unsafe_allow_html=True)
    st.markdown("""
        <div class="about-container">
            <img src='https://img.icons8.com/color/96/000000/panda.png' class='profile-photo' alt='Cute Panda Avatar'>
            <div class="info-section">
                <p>👤 <span class="highlight-text">Name:</span> Tan Peng Teck</p>
                <p>🎂 <span class="highlight-text">Age:</span> 23</p>
                <p>🎓 <span class="highlight-text">Education:</span> Master of Science in Artificial Intelligence</p>
                <div class="cause-section">
                    🌱 <strong>Cause:</strong> I am passionate about <strong>renewables</strong> and <strong>technology</strong>,
                    with a dedication to creating <strong>sustainable solutions</strong> through innovation in <strong>AI</strong> and <strong>data science</strong>.
                </div>
                <p>🔗 Connect with me on LinkedIn: 
                    <a href="https://www.linkedin.com/in/tan-peng-teck-573a201b8/" target="_blank" class="highlight-link">
                        <img src="https://img.icons8.com/color/48/000000/linkedin.png" alt="LinkedIn Icon" style="vertical-align:middle; margin-left: 5px;"> 
                    </a>
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)