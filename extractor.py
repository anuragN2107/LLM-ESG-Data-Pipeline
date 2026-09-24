import os
from pydantic import BaseModel, Field
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
client = genai.Client() # Automatically finds GEMINI_API_KEY

# 1. Define the strict Data Schema
class ESGData(BaseModel):
    company_name: str = Field(description="Name of the company")
    reporting_year: int = Field(description="The year the ESG report covers")
    scope_1_emissions_mt: float = Field(description="Direct greenhouse gas emissions in metric tons")
    scope_2_emissions_mt: float = Field(description="Indirect greenhouse gas emissions in metric tons")
    scope_3_emissions_mt: float = Field(None, description="Supply chain emissions in metric tons. Null if not reported.")
    women_on_board_pct: float = Field(description="Percentage of female board members as a float.")

# 2. The Extraction Engine (No retry loop needed!)
def extract_metrics(raw_text):
    print("Extracting metrics using Gemini...")
    
    prompt = f"Extract the requested ESG metrics from the following text:\n\n{raw_text[:8000]}"
    
    # Gemini natively forces the output to perfectly match our Pydantic schema
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=ESGData,
            temperature=0.1
        ),
    )
    
    # The text is already perfect JSON
    return response.text

# 3. Test the Engine
if __name__ == "__main__":
    test_text = """
    In our 2023 sustainability report for Acme Corp, we are proud to announce major milestones. 
    Our Scope 1 direct emissions dropped to 4500.5 metric tons. We purchased renewable energy, 
    lowering our Scope 2 indirect emissions to 1200.75 MT. Scope 3 calculations are ongoing 
    and not reported here. We also improved diversity, with women now making up 42.5% of our Board of Directors.
    """
    
    result = extract_metrics(test_text)
    print("\nSUCCESS! Extracted JSON:")
    print(result)