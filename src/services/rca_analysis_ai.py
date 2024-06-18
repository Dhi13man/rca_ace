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
            "You are an expert in tech systems, people, text processing, and data analysis."
            " Your directive is to generate insights/tags from human-written RCA documents."
            " Please analyze given RCA texts and extract the root reasons and actionables."
            " The root reasons are the primary causes of the incident,"
            " and the actionables are the steps to prevent the incident from happening again."
            " The idea is to keep the generated insights concise and common so we can"
            " calculate statistics and patterns of the incidents to learn what to prioritise"
            " and what to improve in the future."
            " Keep the number of words in each root reason and actionable to a minimum"
            " so that it can be easy to tally or categorize them. Tokenise them basically."
            " As an expert in tech language, try to make things generic. If you see words"
            " like MySQL, think database, if you see words like Redis, think cache,"
            " if you see words like PayU or Juspay, think third-party. If you see"
            " implementation words like max.poll.records or session.timeout.ms, think Kafka config."
            " We also want to have zero special characters and numbers. If you see 100%, think high"
            " We want to focus on extracting commonalities and the bigger picture overall."
            " Come up with as many actionables as you can, but have zero unnecessary words,"
            " and don't repeat the same actionables. It is fine to have bad grammar or"
            " incomplete sentences, as long as the meaning is clear with minimal words."
            " You should only respond in a json that contains 2 keys:"
            " root_reasons and actionables"
            " The json actionables and root_reasons lists should only contain common words,"
            " no numbers or special characters."
            'Eg. {"root_reasons": ["cpu high"], "actionables": ["capacity planning"]}'
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
