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


RISK_BASED_PROMPTS = {
    "LOW": [
        "I'm looking for stable investments that won’t put my capital at risk.",
        "Can you suggest government-backed or fixed-income products I can start with?",
        "I want to start small and build gradually — what low-risk options do I have?",
        "Which investment will help me grow my savings while staying conservative?"
    ],
    "MEDIUM": [
        "I’m okay with moderate risk if it means better returns. What do you suggest?",
        "I’d like to invest in a mix of options — not too risky, not too safe. What works?",
        "I want to diversify my portfolio. What balanced investment options are available?",
        "Which investments offer a fair trade-off between stability and profit?"
    ],
    "HIGH": [
        "What are the high-yield investment opportunities available right now?",
        "I’m willing to take risks for big returns — what products should I look at?",
        "Can you show me some aggressive investments to maximize my earnings?",
        "I want to beat inflation and build serious wealth — where should I invest?"
    ]
}

PROMPT_TO_RISK_MAP = {
    prompt.lower(): risk_level
    for risk_level, prompts in RISK_BASED_PROMPTS.items()
    for prompt in prompts
}

PROMPT_RESPONSE_MESSAGES = {
    "i'm looking for stable investments that won’t put my capital at risk.": "For investors seeking capital preservation, low-risk investments like fixed-income funds or government-backed securities are ideal. These options prioritize safety over high returns.",
    "can you suggest government-backed or fixed-income products i can start with?": "Government-backed and fixed-income investments are great for cautious investors. They provide predictable returns and are backed by reliable institutions.",
    "i want to start small and build gradually — what low-risk options do i have?": "You can explore mutual funds with low entry amounts or fixed-income securities that offer steady growth and minimal volatility.",
    "which investment will help me grow my savings while staying conservative?": "Look into conservative bond funds or treasury bills. These options allow your money to grow steadily without exposing you to unnecessary risk.",

    "i’m okay with moderate risk if it means better returns. what do you suggest?": "Medium-risk investments provide a good balance between risk and return. Consider diversified mutual funds or blended bond-equity portfolios.",
    "i’d like to invest in a mix of options — not too risky, not too safe. what works?": "Balanced portfolios like hybrid mutual funds or medium-term treasury bonds offer a good mix of safety and performance.",
    "i want to diversify my portfolio. what balanced investment options are available?": "Diversified investments spread your risk across assets. Explore medium-risk mutual funds and blended fixed-income products.",
    "which investments offer a fair trade-off between stability and profit?": "Mid-tier bond funds and balanced equity products often strike a healthy balance between growth and security.",

    "what are the high-yield investment opportunities available right now?": "High-yield opportunities include equity-focused mutual funds, aggressive treasury instruments, and corporate bonds with high returns.",
    "i’m willing to take risks for big returns — what products should i look at?": "If you're growth-oriented, explore aggressive equity funds or speculative bond products with high potential upside.",
    "can you show me some aggressive investments to maximize my earnings?": "Aggressive investments focus on maximizing gains. Consider funds targeting emerging markets, small caps, or speculative instruments.",
    "i want to beat inflation and build serious wealth — where should i invest?": "High-risk products like growth equity funds or high-yield bonds can help outpace inflation and accumulate wealth over time.",
}
