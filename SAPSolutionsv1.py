import streamlit as st

# Title and Description
st.title("Exhaustive List of SAP Modules and Solutions")
st.write("""
This application provides a comprehensive list of SAP (Systems, Applications, and Products in Data Processing) solutions and modules categorized by different areas.
""")

# Core ERP Modules
st.header("Core ERP Modules")
st.subheader("FI (Financial Accounting)")
st.write("""
- General Ledger (GL)
- Accounts Receivable (AR)
- Accounts Payable (AP)
- Asset Accounting (AA)
- Bank Accounting (BA)
- Travel Management (TM)
""")

st.subheader("CO (Controlling)")
st.write("""
- Cost Element Accounting (CEA)
- Cost Center Accounting (CCA)
- Internal Orders (IO)
- Activity-Based Costing (ABC)
- Product Cost Controlling (PCC)
- Profitability Analysis (PA)
""")

st.subheader("SD (Sales and Distribution)")
st.write("""
- Sales Support
- Sales
- Shipping
- Billing
- Sales Information System
- Credit Management
""")

st.subheader("MM (Materials Management)")
st.write("""
- Procurement
- Inventory Management
- Purchasing
- Master Data
- Material Valuation
""")

st.subheader("PP (Production Planning)")
st.write("""
- Production Planning and Control
- MRP (Material Requirements Planning)
- CRP (Capacity Requirements Planning)
- SOP (Sales and Operations Planning)
- Production Orders
""")

st.subheader("QM (Quality Management)")
st.write("""
- Quality Planning
- Quality Inspection
- Quality Control
""")

st.subheader("PM (Plant Maintenance)")
st.write("""
- Preventive Maintenance
- Maintenance Planning
- Work Order Management
""")

st.subheader("PS (Project System)")
st.write("""
- Project Planning
- Project Scheduling
- Project Execution
- Project Costing
""")

st.subheader("HCM (Human Capital Management)")
st.write("""
- Personnel Administration
- Organizational Management
- Payroll
- Time Management
- Recruitment
- Personnel Development
""")

# Advanced and Specialized Modules
st.header("Advanced and Specialized Modules")
st.subheader("APO (Advanced Planner and Optimizer)")
st.write("""
- Demand Planning (DP)
- Supply Network Planning (SNP)
- Production Planning/Detailed Scheduling (PP/DS)
- Global Available to Promise (GATP)
""")

st.subheader("SRM (Supplier Relationship Management)")
st.write("""
- Supplier Collaboration
- Procurement
""")

st.subheader("CRM (Customer Relationship Management)")
st.write("""
- Sales
- Service
- Marketing
- Interaction Center
- Web Channel
""")

st.subheader("SCM (Supply Chain Management)")
st.write("""
- Supply Chain Planning
- Supply Chain Execution
""")

st.subheader("PLM (Product Lifecycle Management)")
st.write("""
- Portfolio and Project Management
- Product Data Management
- Lifecycle Data Management
""")

st.subheader("EWM (Extended Warehouse Management)")
st.write("""
- Warehouse Management
- Inventory Management
""")

st.subheader("GTS (Global Trade Services)")
st.write("""
- Compliance Management
- Customs Management
- Risk Management
""")

st.subheader("BW (Business Warehouse)")
st.write("""
- Data Warehousing
- Business Intelligence
""")

st.subheader("BO (Business Objects)")
st.write("""
- Business Intelligence
- Reporting
- Analytics
""")

st.subheader("S/4HANA")
st.write("""
- Next-generation ERP suite
- Simplified data model
- Real-time analytics
- Fiori user experience
""")

# Industry Solutions
st.header("Industry Solutions")
industry_solutions = [
    "IS-Oil and Gas", "IS-Retail", "IS-Aerospace & Defense", "IS-Automotive",
    "IS-Banking", "IS-Chemicals", "IS-Healthcare", "IS-Insurance", "IS-Media",
    "IS-Pharmaceuticals", "IS-Public Sector", "IS-Utilities"
]
st.write(", ".join(industry_solutions))

# Cross-Application Components
st.header("Cross-Application Components")
st.subheader("SAP NetWeaver")
st.write("""
- Integration and Application Platform
- Portal
- Mobile
- Process Integration
- Business Warehouse
""")

st.subheader("SAP Solution Manager")
st.write("""
- Application Lifecycle Management
- IT Service Management
- Business Process Operations
""")

st.subheader("SAP Fiori")
st.write("""
- User experience (UX) design principles
- Simplified and responsive applications
""")

st.subheader("SAP Ariba")
st.write("""
- Procurement solutions
- Supplier management
""")

st.subheader("SAP Concur")
st.write("""
- Travel and expense management
""")

st.subheader("SAP SuccessFactors")
st.write("""
- Human capital management (HCM) solutions
- Talent management
""")

st.subheader("SAP Hybris")
st.write("""
- E-commerce
- Marketing
- Sales
- Service
""")

# New Innovations
st.header("New Innovations")
st.subheader("SAP Leonardo")
st.write("""
- Digital innovation system
- Internet of Things (IoT)
- Machine Learning
- Blockchain
- Big Data
""")

st.subheader("SAP Cloud Platform")
st.write("""
- Platform-as-a-Service (PaaS)
- Integration services
- Application development
""")

st.subheader("SAP Analytics Cloud")
st.write("""
- Business Intelligence (BI)
- Planning
- Predictive Analytics
""")

# Additional Solutions and Tools
st.header("Additional Solutions and Tools")
additional_solutions = [
    "SAP IBP (Integrated Business Planning)", "SAP MDG (Master Data Governance)",
    "SAP MDM (Master Data Management)", "SAP HANA (High-Performance Analytic Appliance)",
    "SAP VIM (Vendor Invoice Management)", "SAP TM (Transportation Management)",
    "SAP EM (Event Management)", "SAP EHS (Environment, Health, and Safety)",
    "SAP MRS (Multi-Resource Scheduling)", "SAP LBN (Logistics Business Network)"
]
st.write(", ".join(additional_solutions))
