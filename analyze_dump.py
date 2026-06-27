from google import genai

# ================================
# Paste your Gemini API Key below
# ================================
client = genai.Client(
    api_key="YOUR_GEMINI_API_KEY"
    )

# ================================
# Read ST22 dump from text file
# ================================
with open("xt22_dump.txt", "r", encoding="utf-8") as file:
    dump_text = file.read()

# ================================
# Prompt for Gemini
# ================================
prompt = f"""
You are a Senior SAP Basis Consultant, Senior ABAP Consultant, and SAP Support Engineer.

Analyze the following SAP ST22 dump.

Generate a professional report in the following format.

========================================================
SAP ST22 DUMP ANALYSIS REPORT
========================================================

1. Executive Summary

2. Runtime Error

3. Root Cause Analysis

4. Technical Explanation

5. Business Impact

6. Affected SAP Object
   • Program
   • Include
   • Line Number
   • Exception Class

7. Recommended Resolution
   Step 1
   Step 2
   Step 3

8. Corrected ABAP Code

9. SAP Best Practices

10. Possible SAP Notes
(If exact SAP Note is not known, clearly mention it.)

11. SAP Community Search Keywords

12. Prevention

13. Confidence Level (High /Medium /Low)

Use simple English.

ST22 Dump:

{dump_text}
"""

# ================================
# Call Gemini API
# ================================
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

# ================================
# Print Result
# ================================
print(response.text)

# ================================
# Save Result
# ================================
with open("result.txt", "w", encoding="utf-8") as file:
    file.write(response.text)

print("\n====================================")
print("Analysis saved to result.txt")
print("====================================")