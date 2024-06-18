"""
Parses the human-written RCA and extracting the root reasons and actionables.
"""

from json import loads
from openai import OpenAI
from openai.resources.chat.completions import ChatCompletion

from src.models.rca_analysis_insights import RCAAnalysisInsights


class RCAAnalysisAI:
    """
    Parses the human-written RCA and extracting the root reasons and actionables.

    Attributes:
        open_ai_client: The OpenAI client to interact with the OpenAI API
    """

    _model: str = "gpt-4o"
    _response_format: str = {"type": "json_object"}
    _system_message: dict = {
        "role": "system",
        "content": (
            "As an AI with expertise in technology systems, text processing, and data analysis, "
            "your task is to generate concise insights/tags from human-written RCA documents. "
            "Analyze the provided RCA texts to identify the primary causes (root reasons) of "
            "incidents and recommend steps (actionables) to prevent future occurrences. "
            "Aim for conciseness and clarity in the generated insights, allowing for effective "
            "statistical analysis and pattern recognition to prioritize improvements. "
            "Simplify technical terms to their generic counterparts (e.g., 'MySQL' to 'database', "
            "'Redis' to 'cache') and avoid specific implementation details in favor of broader "
            "categories (e.g., 'max.poll.records' to 'Kafka config'). Exclude special characters "
            "and numbers, focusing on extracting overarching themes and commonalities. "
            "Generate a comprehensive list of at least 10 actionable steps without redundancy or "
            "unnecessary details. It is fine to have wrong grammar if the meaning is clear with "
            "minimal words. The number of items in root reasons and actionables should be "
            "maximised while the number of words in each individual item is minimised."
            "Respond with a JSON object containing two keys: 'root_reasons' and 'actionables', "
            "each holding a list of simplified, common terms without numbers or special characters."
            "Example: {'root_reasons': ['cpu high'], 'actionables': ['capacity planning']}."
        )
    }

    def __init__(self, open_ai_client: OpenAI) -> "RCAAnalysisAI":
        self.open_ai_client = open_ai_client

    def extract_insights(self, rca_text: str) -> RCAAnalysisInsights:
        """
        Extracts the insights from the given RCA text

        Args:
            rca_text (str): The RCA text

        Returns:
            RCAAnalysisInsights: The insights extracted from the RCA text
        """
        # Call the OpenAI API to extract the insights
        completion: ChatCompletion = self.open_ai_client.chat.completions.create(
            model=self._model,
            messages=[
                RCAAnalysisAI._system_message,
                {"role": "user", "content": rca_text},
            ],
            response_format=self._response_format,
        )

        # Extract the response from the completion
        first_choice_message_content: str = completion.choices[0].message.content
        content_json: dict = loads(first_choice_message_content)
        print(content_json)

        # Parse the response to RCAAnalysisInsights object
        return RCAAnalysisInsights.from_json(content_json)
