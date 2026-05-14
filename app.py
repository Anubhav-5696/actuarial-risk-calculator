from flask import Flask, request

app = Flask(__name__)


def calculate_expected_loss(claim_probability, coverage_amount):
    """
    Calculates expected loss.

    Expected Loss = Claim Probability x Coverage Amount
    """
    return claim_probability * coverage_amount


def calculate_premium(expected_loss, expense_loading, profit_margin):
    """
    Calculates insurance premium.

    Premium = Expected Loss + Expense Loading + Profit Margin
    """
    expense_amount = expected_loss * expense_loading
    profit_amount = expected_loss * profit_margin
    return expected_loss + expense_amount + profit_amount


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        age = int(request.form["age"])
        smoker = request.form["smoker"]
        coverage_amount = float(request.form["coverage_amount"])
        claim_probability = float(request.form["claim_probability"]) / 100
        expense_loading = float(request.form["expense_loading"]) / 100
        profit_margin = float(request.form["profit_margin"]) / 100

        expected_loss = calculate_expected_loss(
            claim_probability,
            coverage_amount
        )

        premium = calculate_premium(
            expected_loss,
            expense_loading,
            profit_margin
        )

        result = f"""
        <h2>Results</h2>
        <p><strong>Age:</strong> {age}</p>
        <p><strong>Smoker:</strong> {smoker}</p>
        <p><strong>Coverage Amount:</strong> ${coverage_amount:,.2f}</p>
        <p><strong>Claim Probability:</strong> {claim_probability * 100:.2f}%</p>
        <p><strong>Expected Loss:</strong> ${expected_loss:,.2f}</p>
        <p><strong>Estimated Premium:</strong> ${premium:,.2f}</p>
        """

    return f"""
    <html>
        <head>
            <title>Actuarial Risk Calculator</title>
        </head>

        <body>
            <h1>Actuarial Risk & Premium Calculator</h1>

            <p>
                This app estimates expected loss and insurance premium
                using basic actuarial pricing ideas.
            </p>

            <form method="POST">
                <label>Age:</label><br>
                <input type="number" name="age" required><br><br>

                <label>Smoker:</label><br>
                <select name="smoker">
                    <option value="No">No</option>
                    <option value="Yes">Yes</option>
                </select><br><br>

                <label>Coverage Amount:</label><br>
                <input type="number" name="coverage_amount" required><br><br>

                <label>Claim Probability (%):</label><br>
                <input type="number" step="0.01" name="claim_probability" required><br><br>

                <label>Expense Loading (%):</label><br>
                <input type="number" step="0.01" name="expense_loading" required><br><br>

                <label>Profit Margin (%):</label><br>
                <input type="number" step="0.01" name="profit_margin" required><br><br>

                <button type="submit">Calculate Premium</button>
            </form>

            {result}
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

