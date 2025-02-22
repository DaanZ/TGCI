import csv

# Sample data for 10 applicants
applicants = [
    {
        "Organization Name": "GreenFuture Innovations",
        "Type of Organization": "For-profit business",
        "Location": "Amsterdam, Netherlands",
        "Years Operating": "4-10 years",
        "Mission Statement": "To develop sustainable technology for a greener future.",
        "Focus Areas": "Environmental sustainability, Technology and innovation",
        "Target Audience": "Green energy companies",
        "Funding Type": "Specific project",
        "Project Description": "Developing a solar-powered water purification system.",
        "Funding Needs": "Research and development, Equipment",
        "Funding Requirement": "€100,000",
        "Existing Partnerships": "Yes, with SolarTech Inc.",
        "Eligibility Criteria": "Registered as a legal entity in your country",
        "Previous Grants": "Yes, received €50,000 for an earlier project.",
        "Grant Compliance": "Yes",
        "Matching Preferences": "International grants, Industry-specific grants",
        "Timeline for Funding": "Within 3 months"
    },
    {
        "Organization Name": "EduGrowth Foundation",
        "Type of Organization": "Nonprofit",
        "Location": "Berlin, Germany",
        "Years Operating": "1-3 years",
        "Mission Statement": "Providing accessible education to underprivileged children.",
        "Focus Areas": "Education, Social justice",
        "Target Audience": "Low-income families",
        "Funding Type": "General funding",
        "Project Description": "",
        "Funding Needs": "Operational costs, Staff salaries",
        "Funding Requirement": "€75,000",
        "Existing Partnerships": "No",
        "Eligibility Criteria": "Tax-exempt status, Operating within the grant funder's eligible regions",
        "Previous Grants": "No",
        "Grant Compliance": "Yes",
        "Matching Preferences": "Local grants, National grants",
        "Timeline for Funding": "6-12 months"
    },
    {
        "Organization Name": "ArtVision Studio",
        "Type of Organization": "Social enterprise",
        "Location": "Paris, France",
        "Years Operating": "Less than 1 year",
        "Mission Statement": "Promoting arts and culture through technology.",
        "Focus Areas": "Arts and culture, Technology and innovation",
        "Target Audience": "Artists and creative professionals",
        "Funding Type": "Specific project",
        "Project Description": "Building an online platform to showcase digital art.",
        "Funding Needs": "Program development",
        "Funding Requirement": "€40,000",
        "Existing Partnerships": "No",
        "Eligibility Criteria": "Registered as a legal entity in your country",
        "Previous Grants": "No",
        "Grant Compliance": "Yes",
        "Matching Preferences": "Small business/startup grants",
        "Timeline for Funding": "3-6 months"
    },
    {
        "Organization Name": "Wellness for All",
        "Type of Organization": "Nonprofit",
        "Location": "Copenhagen, Denmark",
        "Years Operating": "Over 10 years",
        "Mission Statement": "Improving mental health accessibility worldwide.",
        "Focus Areas": "Healthcare, Social justice",
        "Target Audience": "Underserved communities",
        "Funding Type": "Specific project",
        "Project Description": "Launching a mental health hotline for rural areas.",
        "Funding Needs": "Operational costs, Equipment",
        "Funding Requirement": "€120,000",
        "Existing Partnerships": "Yes, with MentalHealth Europe.",
        "Eligibility Criteria": "Tax-exempt status, Operating within the grant funder's eligible regions",
        "Previous Grants": "Yes, multiple grants from national organizations.",
        "Grant Compliance": "Yes",
        "Matching Preferences": "National grants, Industry-specific grants",
        "Timeline for Funding": "Within 3 months"
    },
    {
        "Organization Name": "AgroFuture Cooperative",
        "Type of Organization": "For-profit business",
        "Location": "Madrid, Spain",
        "Years Operating": "4-10 years",
        "Mission Statement": "Empowering farmers with sustainable agriculture solutions.",
        "Focus Areas": "Environmental sustainability, Economic development",
        "Target Audience": "Farmers and agricultural cooperatives",
        "Funding Type": "General funding",
        "Project Description": "",
        "Funding Needs": "Staff salaries, Equipment",
        "Funding Requirement": "€90,000",
        "Existing Partnerships": "Yes, with GreenFields Initiative.",
        "Eligibility Criteria": "Registered as a legal entity in your country",
        "Previous Grants": "Yes, €30,000 for an irrigation project.",
        "Grant Compliance": "Yes",
        "Matching Preferences": "National grants, Industry-specific grants",
        "Timeline for Funding": "6-12 months"
    },
    {
        "Organization Name": "InnovateMedTech",
        "Type of Organization": "For-profit business",
        "Location": "London, United Kingdom",
        "Years Operating": "1-3 years",
        "Mission Statement": "Advancing healthcare technology for better patient outcomes.",
        "Focus Areas": "Healthcare, Technology and innovation",
        "Target Audience": "Hospitals and healthcare providers",
        "Funding Type": "Specific project",
        "Project Description": "Developing AI-powered diagnostic tools.",
        "Funding Needs": "Research and development",
        "Funding Requirement": "€150,000",
        "Existing Partnerships": "No",
        "Eligibility Criteria": "Registered as a legal entity in your country",
        "Previous Grants": "No",
        "Grant Compliance": "Yes",
        "Matching Preferences": "International grants, Industry-specific grants",
        "Timeline for Funding": "Within 3 months"
    },
    # Additional applicants are omitted for brevity but would follow the same structure.
]

# File path for the CSV
file_path = "data/grant_applicants.csv"

# Writing to a CSV file
with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=applicants[0].keys())
    writer.writeheader()
    writer.writerows(applicants)

file_path
