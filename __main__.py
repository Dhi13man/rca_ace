"""
The main module to run the RCA analysis AI service
"""

from openai import OpenAI

from src.services.rca_analysis_ai import RCAAnalysisAI

if __name__ == "__main__":
    # Create the OpenAI client
    open_ai_client: OpenAI = OpenAI()

    # Create the RCAAnalysisAI service wrapper
    rca_analysis_ai: RCAAnalysisAI = RCAAnalysisAI(open_ai_client)

    # The human-written RCA text
    rca_text: str = (
        "The server was overloaded due to a sudden spike in traffic."
        " The database connection was lost, which caused the server to crash."
    )

    # Extract the insights from the RCA text
    insights = rca_analysis_ai.extract_insights(rca_text)
