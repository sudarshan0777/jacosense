import numpy as np
import json

def handler(request):
    D = np.random.uniform(10, 50) # Demand
    V = np.random.uniform(1, 5) # Volatility
    L = np.random.uniform(5, 20) # Liquidity

    # Price function
    price = 2*D + 0.5*(V**2) - L

    # Jacobian (partial derivatives)
    jacobian = {
        "Demand": 2,
        "Volatility": round(V, 2),
        "Liquidity": -1
    }

    # Sensitivity score (Using Jacobian)
    sensitivity_score = (
        jacobian["Demand"] * D +
        jacobian["Volatility"] * V +
        jacobian["Liquidity"] * L
    )

    # Decision logic using sensitivity
    if sensitivity_score > 80:
        decision = "BUY"
    elif sensitivity_score < 40:
        decision = "SELL"
    else:
        decision = "HOLD"

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "Demand": round(D, 2),
            "Volatility": round(V, 2),
            "Liquidity": round(L, 2),
            "Price": round(price, 2),
            "Jacobian": jacobian,
            "SensitivityScore": round(sensitivity_score, 2),
            "Decision": decision
        })
    }