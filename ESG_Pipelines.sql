CREATE DATABASE EnterpriseESG;
GO
USE EnterpriseESG;
GO

CREATE TABLE Fact_Emissions (
    RecordID INT IDENTITY(1,1) PRIMARY KEY,
    CompanyName VARCHAR(150),
    ReportingYear INT,
    Scope1_MT FLOAT,
    Scope2_MT FLOAT,
    Scope3_MT FLOAT,
    WomenOnBoard_Pct FLOAT,
    IngestionDate DATETIME DEFAULT GETDATE()
);