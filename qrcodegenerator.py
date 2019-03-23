import qrcode
import json
import random
import os
import sys

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


class QRCodeGenerator:
    path = "./data/tests/"

    def generate(self, data: str):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        test_number = len([name for name in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, name))])
        img.save(f"./data/tests/test_qrcode_{test_number}.png")
        img.show()


if __name__ == "__main__":
    passager_mock = Passager(
        "Otávio",
        "43781685888",
        "230942973491284962",
        "13",
        "Joinville - SC",
        "Blumenau - SC"
    )

    # print("Digite as informações do passageiro")
    # name = input("Nome: ", end="")
    # doc = input("Documento: ", end="")
    # pass_number = input("Nº Passagem: ", end="")
    # place_number = input("Assento: ", end="")
    # up_place = input("Embarque: ", end="")
    # down_place = input("Desembarque: ", end="")
    #
    # passager = Passager(
    #     name, doc, pass_number, place_number, up_place, down_place
    # )

    data_str = json.dumps(passager_mock.get_data())
    QRCodeGenerator().generate(data_str)
    print("Done")

