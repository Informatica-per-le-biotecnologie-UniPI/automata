from automata import State, Symbol, Transaction

# esempio sulla consegna
s1, s2 = State("1"), State("2")
transactions = [
    Transaction(s1, Symbol("0"), s2),
    Transaction(s1, Symbol("1"), s1),
    Transaction(s2, Symbol("0"), s1),
    Transaction(s2, Symbol("1"), s2),
]

print(f"States: {s1, s2}")

print(f"Transactions")
for t in transactions:
    print(t)
