import qrcode
import os


class QRCodeGenerator:
    def __init__(self, error_correction=qrcode.constants.ERROR_CORRECT_L,
                 version=1, box_size=10, border=4, path=".", save=True, test=False, show=False):
        self.error_correction = error_correction
        self.version = version
        self.box_size = box_size
        self.border = border
        self.path = path
        self.test = test
        self.show = show
        self.save = save

    def generate(self, data: str):
        qr = qrcode.QRCode(
            version=self.version,
            error_correction=self.error_correction,
            box_size=self.box_size,
            border=self.border,
        )

        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        if self.save:
            test_number = len([name for name in os.listdir(
                self.path) if os.path.isfile(os.path.join(self.path, name))])
            if not self.test:
                img.save(f"{self.path}/qrcode_{test_number}.png")
            else:
                img.save(f"./data/tests/test_qrcode_{test_number}.png")
        if(self.show):
            img.show()
        return img
