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
            "You are an expert in systems, people, and data analysis."
            " Your directive is to generate insights/tags from human-written RCA documents."
            " Please analyze given RCA texts and extract the root reasons and actionables."
            " The root reasons are the primary causes of the incident,"
            " and the actionables are the steps to prevent the incident from happening again."
            " The idea is to keep the generated insights concise and common so we can"
            " calculate statistics and patterns of the incidents to learn what to prioritise"
            " and what to improve in the future."
            " You should only respond in a json that contains 2 keys:"
            " root_reasons and actionables"
            'Eg. {"root_reasons": ["The server was overloaded"]'
            ', "actionables": ["Do capacity planning"]}'
        ),
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
