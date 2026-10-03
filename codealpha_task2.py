# Hardcoded stock prices (USD per share)
STOCK_PRICES = {
    "apple": 180,
    "tesla": 250,
    "google": 140,
    "microsoft": 330,
    "amazon": 130,
}


def get_portfolio():
    """Ask the user for stock names and quantities. Returns {symbol: quantity}."""
    portfolio = {}
    print("Available stocks and prices:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ${price}")
    print("\nEnter stock name and quantity OR Type 'done' when finished.\n")

    while True:
        name = input("Stock symbol (or 'done'): ").strip().lower()
        if name == "done":
            break
        if name not in STOCK_PRICES:
            print(f"  '{name}' not found. Choose from: {', '.join(STOCK_PRICES)}")
            continue

        qty_text = input(f"Quantity of {name}: ").strip()
        try:
            qty = int(qty_text)
            if qty <= 0:
                raise ValueError
        except ValueError:
            print("  Please enter a positive whole number.")
            continue

        portfolio[name] = portfolio.get(name, 0) + qty
    return portfolio


def build_report(portfolio):
    """Return (report_text, total_value)."""
    lines = [f"{'Stock':<8}{'Qty':>6}{'Price':>10}{'Value':>12}", "-" * 36]
    total = 0
    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * qty
        total += value
        lines.append(f"{symbol:<8}{qty:>6}{price:>10}{value:>12}")
    lines.append("-" * 36)
    lines.append(f"{'Total investment value:':<24}${total:>10,.2f}")
    return "\n".join(lines), total


def main():
    print("=== Stock Portfolio Tracker ===\n")
    portfolio = get_portfolio()

    if not portfolio:
        print("\nNo stocks entered. Exiting.")
        return

    report, _ = build_report(portfolio)
    print("\n" + report)

    if input("\nSave result to a file? (y/n): ").strip().lower() == "y":
        filename = "portfolio_result.txt"
        with open(filename, "w") as f:
            f.write(report + "\n")
        print(f"Saved to {filename}")


if __name__ == "__main__":
    main()