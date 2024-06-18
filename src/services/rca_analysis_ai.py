"""
Parses the human-written RCA and extracting the root reasons and actionables.
"""

import re
from json import loads
from openai import OpenAI
from openai.resources.chat.completions import ChatCompletion

from src.models.rca_analysis_insights import RCAAnalysisInsights, Insight


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
            "Each root_reason / actionable should have a brief and a details. "
            "brief should be a concise, high-level tag, represented with 1 or 2 well-defined words"
            "in alphabetical order, separated only by space (eg., 'documentation', 'monitoring', "
            "'code review'). It should be a common term that can be used to categorize the details."
            "details should provide more issue-specific information and relevant context,"
            "represented with a few words or a short sentence. brief is minimal, details maximal."
            "Respond with a JSON object containing two keys: 'root_reasons' and 'actionables', "
            "each holding list of simplified, common insights without numbers, special characters."
            "Example: {'root_reasons': [{'brief': 'load', 'details': 'CPU usage became high as"
            " the number of requests increased.'}], 'actionables': [{'brief': 'capacity', "
            "'details': 'Ensure we have enough capacity to handle peak traffic.'}, {'brief': "
            "'alerting', 'details': 'Set up alerts to notify us when CPU usage is high.'}]}"
        ),
    }

    def __init__(self, open_ai_client: OpenAI) -> "RCAAnalysisAI":
        self.open_ai_client = open_ai_client

    def extract_insights(self, rca_text: str) -> RCAAnalysisInsights:
        """
        Extracts the insights from the given RCA text

        Args:
            rca_text: The RCA text

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

        # Parse the response to RCAAnalysisInsights object
        insights: RCAAnalysisInsights = RCAAnalysisInsights.from_json(content_json)

        # Post-process the insights and return
        insights.root_reasons = self.post_process_insights(insights.root_reasons)
        insights.actionables = self.post_process_insights(insights.actionables)
        return insights

    def post_process_insights(self, insights: list[Insight]) -> list[Insight]:
        """
        Post-process the insights to improve the quality and readability

        Args:
            insights: The insights extracted from the RCA text

        Returns:
            list[Insight]: The post-processed insights
        """
        processed: list[Insight] = []
        for insight in insights:
            brief: str = insight.brief
            details: str = insight.details

            # Post-process the brief
            brief = brief.strip().lower()
            brief = re.sub(r"([^a-z])|(\s+)|(\n+)", " ", brief)

            # Post-process the details
            details = details.strip()

            # Add the processed insight
            processed.append(Insight(brief=brief, details=details))
        return insights
