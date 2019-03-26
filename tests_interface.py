import json
from qrcodegenerator.qrcodegenerator import QRCodeGenerator

class Passager:
    def __init__(self, name, doc, pass_number, place_number, up_place, down_place):
        self.name = name
        self.doc = doc
        self.pass_number = pass_number
        self.place_number = place_number
        self.up_place = up_place
        self.down_place = down_place

    def get_data(self):
        return {
            "name": self.name,
            "doc": self.doc,
            "pass_number": self.pass_number,
            "place_number": self.place_number,
            "up_place": self.up_place,
            "down_place": self.down_place,
        }

if __name__ == "__main__":
    passager_mock = Passager(
        "Otávio",
        "43781685888",
        "230942973491284962",
        "13",
        "Joinville - SC",
        "Blumenau - SC"
    )
    
    data_str = json.dumps(passager_mock.get_data())
    qrcodegen = QRCodeGenerator(tests=True)
    img = qrcodegen.generate(data_str)
    img.show()
    print("Done")

