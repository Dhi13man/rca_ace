"""
This model holds the insights generated from the RCA analysis by the AI model
"""


class Insight:
    """
    The insight extracted from the RCA analysis

    Attributes:
        brief: The brief description of the insight
        details: The detailed description of the insight
    """

    _brief_key: str = "brief"
    _details_key: str = "details"

    def __init__(self, brief: str, details: str) -> "Insight":
        self.brief = brief
        self.details = details

    def to_json(self) -> dict:
        """
        Converts the insight to a JSON representation

        Returns:
            dict: The JSON representation of the insight
        """
        return {
            Insight._brief_key: self.brief,
            Insight._details_key: self.details,
        }

    @staticmethod
    def from_json(json: dict) -> "Insight":
        """
        Converts a JSON representation to the insight object

        Args:
            json (dict): The JSON representation of the insight

        Returns:
            Actionable: The insight object
        """
        return Insight(
            brief=json.get(Insight._brief_key, ""),
            details=json.get(Insight._details_key, ""),
        )


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
        root_reasons: list[Insight],
        actionables: list[Insight],
    ) -> "RCAAnalysisInsights":
        self.root_reasons: list[Insight] = root_reasons
        self.actionables: list[Insight] = actionables

    def to_json(self) -> dict:
        """
        Converts the insights to a JSON representation

        Returns:
            dict: The JSON representation of the insights
        """
        return {
            RCAAnalysisInsights._root_reasons_key: [
                insight.to_json() for insight in self.root_reasons
            ],
            RCAAnalysisInsights._actionables_key: [
                actionable.to_json() for actionable in self.actionables
            ],
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
            root_reasons=[
                Insight.from_json(r)
                for r in json.get(RCAAnalysisInsights._root_reasons_key, [])
            ],
            actionables=[
                Insight.from_json(a)
                for a in json.get(RCAAnalysisInsights._actionables_key, [])
            ],
        )
