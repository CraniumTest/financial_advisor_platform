import datetime
import random

def get_financial_plan(user_goals, risk_tolerance):
    """
    Generates a mock personalized financial plan.
    
    Args:
        user_goals (str): The user's financial goals.
        risk_tolerance (str): The user's risk tolerance.
    
    Returns:
        dict: A financial plan including recommended savings, investments, and timeframes.
    """
    plan = {
        "goals": user_goals,
        "risk_tolerance": risk_tolerance,
        "recommended_savings": f"${random.randint(1000, 5000)} per month",
        "recommended_investments": ["Index Funds", "ETFs", "Bonds"] if risk_tolerance == "low" else ["Stocks", "Cryptocurrency"],
        "timeframes": {
            "short_term": "2-5 years",
            "long_term": "10-20 years"
        }
    }
    return plan

def get_market_analysis():
    """
    Generates a mock market analysis.
    
    Returns:
        str: A string summarizing the current market outlook.
    """
    # Simulating a market analysis response
    analysis = f"""
    Market Analysis as of {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:
    - The stock market has shown a {'positive' if random.choice([True, False]) else 'negative'} trend over the last week.
    - Technology stocks are {'performing well' if random.choice([True, False]) else 'underperforming'}.
    - Energy sector is seeing {'growth' if random.choice([True, False]) else 'decline'}.
    """
    return analysis

def main():
    print("Welcome to the AI Financial Advisor Platform!")
    
    # Simulate user input for financial planning
    user_goals = input("Please enter your financial goals (e.g., retirement, buying a house): ")
    risk_tolerance = input("Enter your risk tolerance (low, medium, high): ")
    
    plan = get_financial_plan(user_goals, risk_tolerance)
    print("\n--- Your Personalized Financial Plan ---")
    for key, value in plan.items():
        print(f"{key.capitalize()}: {value}")
        
    # Simulate market analysis feature
    print("\n--- Real-Time Market Analysis ---")
    market_analysis = get_market_analysis()
    print(market_analysis)

if __name__ == "__main__":
    main()
