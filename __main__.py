"""
The main module to run the RCA analysis AI service
"""

from os.path import join
from openai import OpenAI
import pandas as pd

from src.services.rca_analysis_ai import RCAAnalysisAI
from src.services.rca_reader import RCAReader

INPUT_DIR = "./rcas"
OUTPUT_DIR = "./output"

RCA_FILE_HEADER = "rca_file"
ACTIONABLE_HEADER = "actionable"
ROOT_REASON_HEADER = "root_reason"

if __name__ == "__main__":
    # Create the Components
    rca_reader: RCAReader = RCAReader()
    open_ai_client: OpenAI = OpenAI(max_retries=5)
    rca_analysis_ai: RCAAnalysisAI = RCAAnalysisAI(open_ai_client)

    # The human-written RCA text
    rca_map: dict[str, str] = rca_reader.read_rca(INPUT_DIR)

    # Extract the insights from the RCA text and create the CSV files
    actionables = []
    root_reasons = []
    for rca_file, rca_text in rca_map.items():
        insights = rca_analysis_ai.extract_insights(rca_text)

        for actionable in insights.actionables:
            actionables.append(
                {RCA_FILE_HEADER: rca_file, ACTIONABLE_HEADER: actionable}
            )
        for root_reason in insights.root_reasons:
            root_reasons.append(
                {RCA_FILE_HEADER: rca_file, ROOT_REASON_HEADER: root_reason}
            )

    # Create the CSV files
    actionables_df = pd.DataFrame(actionables)
    root_reasons_df = pd.DataFrame(root_reasons)
    # Write the data to the CSV files
    actionables_df.to_csv(join(OUTPUT_DIR, "actionables.csv"), index=False)
    root_reasons_df.to_csv(join(OUTPUT_DIR, "root_reasons.csv"), index=False)
