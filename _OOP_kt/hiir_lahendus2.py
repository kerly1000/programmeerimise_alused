class Mouse:
    # klassimuutuja
    total_mice = 0

    def __init__(self, brand, dpi):
        self.brand = brand
        self.dpi = dpi
        Mouse.total_mice += 1

    def click(self):
        print(f"{self.brand} hiir klõpsas!")

    def change_dpi(self, new_dpi):
        if new_dpi <= 0:
            print("Viga: DPI peab olema positiivne.")
        else:
            self.dpi = new_dpi


class GamingMouse(Mouse):
    def __init__(self, brand, dpi, rgb=True):
        super().__init__(brand, dpi)
        self.rgb = rgb  # uus väli (vaikeväärtus!)

    def toggle_rgb(self):
        self.rgb = not self.rgb
        print(f"RGB on nüüd {'sees' if self.rgb else 'väljas'}")

    def click(self):
        print(f"{self.brand} GAMING hiir teeb kiire klõpsu!")


if __name__ == '__main__':
    try:
        mouse1 = Mouse("Logitech", 800)
        gaming_mouse = GamingMouse("Razer", 1600)

        print("Kõik hiired kokku:", Mouse.total_mice)

        # 👉 LOO LIST
        mice = []

        for i in range(60):
            mice.append(Mouse("Generic", 800))

        for i in range(40):
            mice.append(GamingMouse("Razer", 1600))

        # 👉 KASUTA MEETODIT
        for m in mice:
            m.click()

        # 👉 LOENDA
        gaming_count = 0

        for m in mice:
            if isinstance(m, GamingMouse):
                gaming_count += 1

        print("Gaming hiiri:", gaming_count)

    except ValueError:
        print("Tundmatu")