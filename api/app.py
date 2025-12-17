from flask import Flask, render_template
import numpy as np

app = Flask(__name__)

@app.route("/")
def index():
    # Simulated market inputs
    D = np.random.uniform(10, 50)      # Demand
    V = np.random.uniform(1, 5)        # Volatility
    L = np.random.uniform(5, 20)       # Liquidity
    T = np.random.uniform(-3, 3)       # Trend (-ve down, +ve up)
    C = np.random.uniform(-10, 10)     # Volume Change

    # Price model (simple & explainable)
    price = 2*D + 0.5*(V**2) - L + 1.5*T + 0.2*C

    # Jacobian (partial derivatives)
    jacobian = {
        "Demand": 2,
        "Volatility": round(V, 2),
        "Liquidity": -1,
        "Trend": 1.5,
        "Volume": 0.2
    }

    # Decision logic (rule-based)
    if jacobian["Demand"] > 1.5 and jacobian["Trend"] > 0 and T > 0:
        decision = "BUY"
        reason = "High demand and positive trend"
    elif jacobian["Trend"] < 0 and T < 0:
        decision = "SELL"
        reason = "Negative trend dominating"
    else:
        decision = "HOLD"
        reason = "Mixed or moderate market signals"

    return render_template(
        "index.html",
        D=round(D,2), V=round(V,2), L=round(L,2),
        T=round(T,2), C=round(C,2),
        price=round(price,2),
        jacobian=jacobian,
        decision=decision,
        reason=reason
    )

if __name__ == "__main__":
    app.run(debug=True)
