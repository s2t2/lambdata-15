
# attributes / properties

# behaviors / methods



# my_labmdata/polos.py

class Polo():
    def __init__(self, color, size, price, style="Normal Fit"):
        self.color = color
        self.size = size
        self.price = price
        self.style = style

    def fold(self):
        print(f"FOLDING THE {self.size.upper()} {self.color.upper()} POLO HERE!")

if __name__ == "__main__":

    # df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})

    polo = Polo("Blue", "Large", 99.99)
    print(type(polo))
    print(polo.color, polo.size, polo.price)
    polo.fold()

    polo2 = Polo(color="Yellow", size="Small", price=69.99)
    print(polo2.color, polo2.size, polo2.price)
    polo2.fold()

    polo3 = Polo(color="Green", size="Medium", price=69.99, style="Fit Cut")
    print(polo3.color, polo.size, polo.price)
    polo3.fold()
