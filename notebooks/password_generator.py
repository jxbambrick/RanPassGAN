import random
import string
import secrets

class PasswordGenerator:

    # New class variable for special characters
    SPECIAL_CHARS = "!@#$%^&"

    def __init__(self):
        self.secure = True
        self.use_upper = True
        self.use_lower = True
        self.use_digits = True
        self.use_special = True
        self.avoid_ambiguous = True
        self.length = 12

    def generate(self, **kwargs):
        secure = kwargs.get('secure', self.secure)
        use_upper = kwargs.get('use_upper', self.use_upper)
        use_lower = kwargs.get('use_lower', self.use_lower)
        use_digits = kwargs.get('use_digits', self.use_digits)
        use_special = kwargs.get('use_special', self.use_special)
        avoid_ambiguous = kwargs.get('avoid_ambiguous', self.avoid_ambiguous)
        length = kwargs.get('length', self.length)
        
        character_set = ""
        
        if secure:
            rand_gen = secrets
        else:
            rand_gen = random

        if use_upper:
            character_set += string.ascii_uppercase
            if avoid_ambiguous:
                character_set = character_set.replace('O', '').replace('I', '')

        if use_lower:
            character_set += string.ascii_lowercase
            if avoid_ambiguous:
                character_set = character_set.replace('l', '')

        if use_digits:
            character_set += string.digits
            if avoid_ambiguous:
                character_set = character_set.replace('0', '').replace('1', '')

        if use_special:
            character_set += PasswordGenerator.SPECIAL_CHARS  # Use the class variable here

        if len(character_set) == 0:
            raise ValueError("No characters available for password generation based on given criteria.")

        password = ''.join(rand_gen.choice(character_set) for _ in range(length))

        return password[:3] + '1' + password[4:7] + '2' + password[8:11] + '3' + password[12:]
