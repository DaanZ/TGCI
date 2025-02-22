import pandas as pd

# Sample data for US government grants in different areas
grant_data = {
    "Grant ID": [
        "EDU123", "HEA456", "ENV789", "TEC101", "AGR202",
        "CUL303", "SCI404", "ART505", "SMB606", "RES707"
    ],
    "Grant Name": [
        "Education for All Initiative", "Healthcare Innovation Fund",
        "Clean Energy Research Grant", "Tech Advancement Program",
        "Agriculture Development Grant", "Cultural Heritage Preservation",
        "Scientific Breakthroughs Program", "Art in Communities Fund",
        "Small Business Expansion Grant", "Renewable Energy Studies"
    ],
    "Category": [
        "Education", "Healthcare", "Environment", "Technology", "Agriculture",
        "Culture", "Science", "Arts", "Small Business", "Research"
    ],
    "Eligibility": [
        "Nonprofits, Schools", "Nonprofits, Hospitals",
        "Research Institutions", "Startups, Universities",
        "Farmers, NGOs", "Museums, Nonprofits",
        "Universities, Labs", "Artists, NGOs",
        "Small Businesses", "Universities, Labs"
    ],
    "Funding Amount (USD)": [
        "500,000", "1,000,000", "750,000", "1,200,000",
        "300,000", "400,000", "2,000,000", "100,000",
        "250,000", "1,500,000"
    ],
    "Application Deadline": [
        "2025-03-15", "2025-04-01", "2025-05-20", "2025-06-10",
        "2025-04-15", "2025-05-01", "2025-06-30", "2025-03-30",
        "2025-04-20", "2025-05-25"
    ],
    "Grant URL": [
        "https://grants.gov/edu123", "https://grants.gov/hea456",
        "https://grants.gov/env789", "https://grants.gov/tec101",
        "https://grants.gov/agr202", "https://grants.gov/cul303",
        "https://grants.gov/sci404", "https://grants.gov/art505",
        "https://grants.gov/smb606", "https://grants.gov/res707"
    ]
}

# Create a DataFrame
grant_df = pd.DataFrame(grant_data)

# Save to CSV
grant_file_path = "data/us_government_grants.csv"
grant_df.to_csv(grant_file_path, index=False)

grant_file_path
