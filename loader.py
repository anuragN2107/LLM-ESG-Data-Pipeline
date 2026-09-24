import pyodbc
import json

def load_to_sql_server(json_data_string):
    print("Connecting to SQL Server...")
    # Connection string for local SQL Server using Windows Authentication
    # Connection string matching your SSMS configuration
    conn_str = (
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER=LAPTOP-GEC0TTHB\MSSQL;'
        r'DATABASE=EnterpriseESG;'
        r'Trusted_Connection=yes;'
        r'TrustServerCertificate=yes;'
    )
    
    try:
        # Parse the JSON string into a Python dictionary
        data = json.loads(json_data_string)
        
        with pyodbc.connect(conn_str) as conn:
            cursor = conn.cursor()
            sql_query = """
                INSERT INTO Fact_Emissions 
                (CompanyName, ReportingYear, Scope1_MT, Scope2_MT, Scope3_MT, WomenOnBoard_Pct)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            
            # Execute the insertion
            cursor.execute(sql_query, (
                data['company_name'],
                data['reporting_year'],
                data['scope_1_emissions_mt'],
                data['scope_2_emissions_mt'],
                data['scope_3_emissions_mt'],
                data['women_on_board_pct']
            ))
            conn.commit()
            print(f"Successfully inserted data for {data['company_name']} into SQL Server!")
            
    except Exception as e:
        print(f"Database error: {e}")

# Test the loader using the exact JSON output from Phase 2
if __name__ == "__main__":
    sample_json = '{"company_name": "Acme Corp", "reporting_year": 2023, "scope_1_emissions_mt": 4500.5, "scope_2_emissions_mt": 1200.75, "scope_3_emissions_mt": 0.0, "women_on_board_pct": 42.5}'
    load_to_sql_server(sample_json)