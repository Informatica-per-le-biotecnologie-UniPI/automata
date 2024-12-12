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

    def __hash__(self):
        return hash(self.symbol)


class Transaction:
    """Definisce transizioni tra State"""
    def __init__(self, source: State, symbol: Symbol, destination: State):
        self.source = source
        self.symbol = symbol
        self.destination = destination

    def __eq__(self, other):
        return isinstance(other, Transaction)\
                and self.source == other.source\
                and self.symbol == other.symbol\
                and self.destination == other.destination

    def __hash__(self):
        return hash(self.source) + hash(self.symbol) + hash(self.destination)

    def __str__(self):
        return f"{str(self.source)} -- {self.symbol} --> {self.destination}"
