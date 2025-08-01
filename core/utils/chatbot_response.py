from pyexpat.errors import messages


class InvestmentChatBot:
    def __init__(self):
        self.guidelines = [
            {
                "keywords": ["treasury bills", "t-bills", "t bills"],
                "response": "Treasury bills are government-backed low-risk instruments.",
                "filters": {"asset_type": "TREASURY_BILLS"}
            },
            {
                "keywords": ["mutual funds", "mutual"],
                "response": "Mutual funds are professionally managed investment pools",
                "filters": {"asset_type": "MUTUAL_FUNDS"}
            },
            {
                "keywords": ["naira bonds", "bonds", "fgn bonds"],
                "response": "Naira bonds are fixed-income securities offering steady returns, usually over the long term.",
                "filters": {"asset_type": "NAIRA_BONDS"}
            },
            {
                "keywords": ["low risk", "safe", "conservative", "low-risk"],
                "response": "Here are some low-risk investment options available.",
                "filters": {"risk_level": "LOW"}
            },
            {
                "keywords": ["medium risk", "moderate", "medium-risk"],
                "response": "These options offer moderate returns with moderate risk.",
                "filters": {"risk_level": "MEDIUM"}
            },
            {
                "keywords": ["high risk", "aggressive", "high-risk"],
                "response": "These are high-risk investment with potentially high returns.",
                "filters": {"risk_level": "HIGH"}
            },
        ]

    def get_response(self, user_input):
        user_input_l = user_input.lower().strip()

        for guide in self.guidelines:
            for keyword in guide["keywords"]:
                if keyword in user_input_l:
                    return {
                        "message": guide["response"],
                        "filters": guide.get("filters", {})
                    }

        return {
            "message": (
                "I am sorry, I didn't catch that. "
                "You can ask about investment types like 'treasury bills', "
                "'mutual funds', or 'low-risk options'"
            ),
            "filter": {}
        }