import google.generativeai as genai
import os

# ==============================================================================
# 🤖 GOOGLE AI STUDIO QUICKSTART (B2B WORKFLOW)
# By Rifin De Josh | AI NY City 🗽
# Read the full audit: https://www.ainycity.com
# ==============================================================================

print("Initializing Zero-Fluff AI Workflow...\n")

# STEP 1: Insert your API Key here
# (Get it for free at: https://aistudio.google.com/app/apikey)
API_KEY = "YOUR_API_KEY_HERE"

# Configure the SDK
genai.configure(api_key=API_KEY)

# STEP 2: Initialize the Model 
# Using gemini-1.5-flash for maximum speed in B2B automation
model = genai.GenerativeModel('gemini-1.5-flash')

# STEP 3: The Business Data & Prompt
business_data = """
Q3 Spend: $45,000 on FB Ads, $20,000 on Google Ads. 
Leads Generated: 120 from FB, 80 from Google. 
Conversion Rates: FB at 5%, Google at 12%.
"""

prompt = f"""
Act as a brutal, data-driven Financial Analyst. 
Read the following raw business data and calculate the Cost Per Lead (CPL) 
and the total number of converted customers for both platforms. 
Output the results in a clean, zero-fluff bulleted list.

DATA:
{business_data}
"""

print("📤 Sending business data to Google AI Studio...")

# STEP 4: Execute and Print
try:
    response = model.generate_content(prompt)
    print("\n✅ AI AUDIT RESULT:\n")
    print(response.text)
except Exception as e:
    print(f"\n❌ ERROR: Did you forget to paste your API Key? \nDetails: {e}")

# ==============================================================================
# End of script. Real tests. Zero fluff.
