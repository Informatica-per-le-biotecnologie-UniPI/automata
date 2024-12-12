from automata import State, Symbol, Transaction, Automaton

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

# testing adding more final states
for s in a.final_states:
    print(f"Final state: {s}")
a.mark_as_final(s2)

s3 = State("3")
try:
    a.mark_as_final(s3)
except ValueError as e:
    print(f"Errore nell'aggiunta dello stato finale: {e}")

for s in a.final_states:
    print(f"Final state: {s}")

# testing adding transitions
s3 = State("3")
a.add(Transaction(s1, Symbol("2"), s3))
a.add(Transaction(s3, Symbol("2"), s1))
a.mark_as_final(s3)

for s in a.final_states:
    print(f"Final state: {s}")

for t in a.transactions:
    print(t)

for s in a.final_states:
    print(f"Final state: {s}")
a.mark_as_final(s2)

# should fail
s4 = State("4")
try:
    a.add(Transaction(s4, Symbol("2"), s1))
except ValueError as e:
    print(e)

