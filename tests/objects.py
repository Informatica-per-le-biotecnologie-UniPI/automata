from automata import State, Symbol, Transaction, Automaton

# esempio sulla consegna
s1, s2 = State("1"), State("2")
transactions = [
    Transaction(s1, Symbol("0"), s2),
    Transaction(s1, Symbol("1"), s1),
    Transaction(s2, Symbol("0"), s1),
    Transaction(s2, Symbol("1"), s2),
]

# print(f"States: {s1, s2}")
#
# print(f"Transactions")
# for t in transactions:
#     print(t)


##############################################################################
# Automaton ##################################################################
##############################################################################
a = Automaton(
    start_state=s1,
    final_states={s1},
    transactions=set(transactions)
)

for state in a.states:
    print(state)

print(f"Starting state: {a.start_state}")
for s in a.final_states:
    print(f"Final state: {s}")

for t in a.transactions:
    print(t)
