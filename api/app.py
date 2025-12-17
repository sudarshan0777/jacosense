import numpy as np
import json

def handler(request):
    D = np.random.uniform(10, 50)
    V = np.random.uniform(1, 5)
    L = np.random.uniform(5, 20)
    T = np.random.uniform(-3, 3)
    C = np.random.uniform(-10, 10)

    price = 2*D + 0.5*(V**2) - L + 1.5*T + 0.2*C

    jacobian = {
        "Demand": 2,
        "Volatility": round(V, 2),
        "Liquidity": -1,
        "Trend": 1.5,
        "Volume": 0.2
    }

    if jacobian["Demand"] > 1.5 and T > 0:
        decision = "BUY"
    elif T < 0:
        decision = "SELL"
    else:
        decision = "HOLD"

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "Demand": round(D,2),
            "Volatility": round(V,2),
            "Liquidity": round(L,2),
            "Trend": round(T,2),
            "VolumeChange": round(C,2),
            "Price": round(price,2),
            "Jacobian": jacobian,
            "Decision": decision
        })
    }
