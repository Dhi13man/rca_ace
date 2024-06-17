"""
This model holds the insights generated from the RCA analysis by the AI model
"""


class RCAAnalysisInsights:
    """
    The insights generated from the RCA analysis by the AI model

    Attributes:
        root_reasons: The root reasons extracted from the RCA analysis
        actionables: The actionables extracted from the RCA analysis
    """

    _root_reasons_key: str = "root_reasons"
    _actionables_key: str = "actionables"

    def __init__(
        self,
        root_reasons: list[str],
        actionables: list[str],
    ) -> "RCAAnalysisInsights":
        self.root_reasons = root_reasons
        self.actionables = actionables

    def to_json(self) -> dict:
        """
        Converts the insights to a JSON representation

        Returns:
            dict: The JSON representation of the insights
        """
        return {
            RCAAnalysisInsights._root_reasons_key: self.root_reasons,
            RCAAnalysisInsights._actionables_key: self.actionables,
        }

    @staticmethod
    def from_json(json: dict) -> "RCAAnalysisInsights":
        """
        Converts a JSON representation to the insights object

        Args:
            json (dict): The JSON representation of the insights

        Returns:
            RCAAnalysisInsights: The insights object
        """
        return RCAAnalysisInsights(
            root_reasons=json[RCAAnalysisInsights._root_reasons_key], 
            actionables=json[RCAAnalysisInsights._actionables_key],
        )
