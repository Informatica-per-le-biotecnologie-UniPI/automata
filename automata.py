# mi permette di indicare una classe come suo tipo di ritorno
from __future__ import annotations


class State:
    """Definisce uno stato."""
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"State {self.name}"

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return isinstance(other, State) and self.name == other.name


class Symbol:
    """Definisce uno simbolo nell'alfabeto."""
    def __init__(self, symbol):
        self.symbol = symbol

    def __eq__(self, other):
        return isinstance(other, Symbol) and self.symbol == other.symbol

    def __hash__(self):
        return hash(self.symbol)

    def __str__(self):
        return str(self.symbol)


class Transaction:
    """Definisce transizioni tra State"""
    def __init__(self, source: State, symbol: Symbol, destination: State):
        self.source = source
        self.symbol = symbol
        self.destination = destination

    def __eq__(self, other):
        # nota: per righe lunghe, posso separarle con un "\" e andare a capo
        return isinstance(other, Transaction)\
                and self.source == other.source\
                and self.symbol == other.symbol\
                and self.destination == other.destination

    def __hash__(self):
        return hash(self.source) + hash(self.symbol) + hash(self.destination)

    def __str__(self):
        return f"{str(self.source)} -- {self.symbol} --> {self.destination}"


class Automaton:
    # nota: per tipi collezione, possiamo usare T[X] per indicare che la collezione T contiene oggetti di tipo X
    def __init__(self, transactions: set[Transaction], start_state: State, final_states: set[State]):
        """

        :param transactions: Transizioni dell'automa
        :param start_state: Stato iniziale
        :param final_states: Stato/i finale
        """
        self.states = [transaction.source for transaction in transactions]\
                                 + [transaction.destination for transaction in transactions]
        self.states = set(self.states)

        # e se lo stato iniziale non esistesse?
        if start_state not in self.states:
            raise ValueError(f"Stato iniziale {start_state} non trovato nelle transizioni")

        # e se gli stati finali non esistessero?
        for state in final_states:
            if state not in self.states:
                raise ValueError(f"Stato finale {state} non trovato nelle transizioni")

        self.start_state = start_state
        self.final_states = final_states
        self.transactions = transactions

    def add(self, transaction: Transaction) -> Automaton:
        """Aggiungi una transizione all'automa corrente, modificandolo.

        :param transaction: La transizione da aggiungere
        :return: Questo automa.
        """
        # lo stato iniziale *deve* essere gia' parte dell'automa
        if transaction.source not in self.states:
            raise ValueError(f"Stato iniziale {transaction.source} non trovato in {self.states}")

        self.transactions.add(transaction)
        self.states.add(transaction.destination)
        # non ho bisogno di aggiungere anche la sorgente dato che e' gia' negli stati

        return self

    def mark_as_final(self, state: State) -> Automaton:
        """Marca lo stato dato come finale.

        :param state: Lo stato: deve essere uno degli stati esistenti.
        :return: Questo automa.
        """
        if state not in self.states:
            raise ValueError(f"Stato {state} non trovato in {self.states}")

        self.final_states.add(state)

        return self

    def __contains__(self, item: State | Transaction) -> bool:
        if isinstance(item, State):
            return item in self.states
        elif isinstance(item, Transaction):
            return item in self.transactions
        else:
            return False

    # domanda: la dunder __call__ a cosa serve?
    def __call__(self, string: list[Symbol]) -> bool:
        """L'automa riconosce la `string` data?

        :param string: La stringa da riconoscere.
        :return: True se riconosciuta, False altrimenti.
        """
        return self._simulate(string, state=self.start_state)

    def _simulate(self, string: list[Symbol], state: State) -> bool:
        """Simula il riconoscimento di `string` partendo dallo stato `state` dato.

        :param string: La stringa da riconoscere.
        :param state: Lo stato iniziale. Si assume sia nell'insieme degli stati dell'automa
        :return: True se riconosciuta, False altrimenti.
        """
        # ho terminato tutta la stringa...
        if len(string) == 0:
            # ... accetto se sono in uno stato finale
            return state in self.final_states

        next_state = list()
        for transaction in self.transactions:
            if transaction.source == state:
                if transaction.symbol == string[0]:
                    next_state.append(transaction.destination)

        next_state = [
            transaction.destination
            for transaction in self.transactions
            if transaction.source == state and transaction.symbol == string[0]
        ]

        # stringa non riconosciuta!
        if len(next_state) == 0:
            return False

        return self._simulate(string[1:], next_state[0])
