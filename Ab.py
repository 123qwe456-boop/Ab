from abc import ABC, abstractmethod

# 1. Create the abstract parent class
class Instrument(ABC):
    def __init__(self, name: str, brand: str):
        """Parent constructor to initialize common attributes."""
        self.name = name
        self.brand = brand

    @abstractmethod
    def make_sound(self):
        """Abstract method that must be implemented by all child classes."""
        pass


# 2. Build child classes for different instruments
class Guitar(Instrument):
    def __init__(self, name: str, brand: str, string_count: int):
        # Call the parent constructor using super()
        super().__init__(name, brand)
        self.string_count = string_count

    def make_sound(self):
        """Implementation of the abstract method for Guitar."""
        return f"🎸 The {self.brand} {self.name} (with {self.string_count} strings) goes: Strum... Twang! ♪"


class Drums(Instrument):
    def __init__(self, name: str, brand: str, drum_type: str):
        # Call the parent constructor using super()
        super().__init__(name, brand)
        self.drum_type = drum_type

    def make_sound(self):
        """Implementation of the abstract method for Drums."""
        return f"🥁 The {self.brand} {self.name} ({self.drum_type} setup) goes: Boom-Ba-Dum-Tsh! ♫"


class Flute(Instrument):
    def __init__(self, name: str, brand: str, material: str):
        # Call the parent constructor using super()
        super().__init__(name, brand)
        self.material = material

    def make_sound(self):
        """Implementation of the abstract method for Flute."""
        return f" flute The {self.brand} {self.name} (crafted from {self.material}) goes: Tu-Li-Loo... Slur! ♩"


# 3. The Music Instrument Sound Show Performance
def start_sound_show(instruments_list):
    print("=== Welcome to the Music Instrument Sound Show! ===")
    for instrument in instruments_list:
        print(instrument.make_sound())

# --- Execution ---
if __name__ == "__main__":
    # Instantiate child objects
    my_guitar = Guitar(name="Electric Guitar", brand="Fender", string_count=6)
    my_drums = Drums(name="Drum Kit", brand="Yamaha", drum_type="5-piece Acoustic")
    my_flute = Flute(name="Concert Flute", brand="Pearl", material="Silver")

    # Put them in a collection to showcase polymorphism
    show_lineup = [my_guitar, my_drums, my_flute]
    
    # Run the show
    start_sound_show(show_lineup)
