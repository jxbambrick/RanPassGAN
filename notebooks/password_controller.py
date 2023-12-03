import os
from password_generator import PasswordGenerator
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

# 100 million passwords = 200 files of 500,000 passwords each = 1.2 GB of data
# 1 billion passwords = 2,000 files of 500,000 passwords each = 12 GB of data
# Numeric only 12 digit passwords contain 10^12 = 1 trillion possible combinations
# Numberic only 14 digit passwords contain 10^14 = 100 trillion possible combinations

# storage size of 1 password with 12 digits = 12 bytes
# storage of 1 file with 500,000 passwords = 6 MB
# storage of 200 files with 500,000 passwords = 1.2 GB

class PasswordController:

    PASSWORD_FOLDER_NAME = "validation_12digit_pattern4"
    PASSWORD_FILENAME = "validation_12digit_pattern4"  # Base filename
    
    PASSWORDS_PER_FILE = 1000000
    TOTAL_PASSWORDS = 1000000
    
    OUTPUT_DIR = f"resources/{PASSWORD_FOLDER_NAME}"
    THREAD_POOL_SIZE = 20  # Variable for thread pool size
    
    def __init__(self):
        self.generator = PasswordGenerator()

        self.generator.secure = False
        self.generator.length = 12
        self.generator.use_upper = False
        self.generator.use_lower = False
        self.generator.use_special = False
        self.generator.use_digits = True
        self.generator.avoid_ambiguous = False

        if not os.path.exists(PasswordController.OUTPUT_DIR):
            os.makedirs(PasswordController.OUTPUT_DIR)

    def _generate_and_save(self, file_name, batch_size):
        with open(file_name, 'w') as f:
            for _ in range(batch_size):
                f.write(self.generator.generate() + '\n')
        
        # Print the completion message along with the file name
        print(f"Thread completed its task. File generated: {file_name}")

    
    def generate_password_files(self):
        num_files = PasswordController.TOTAL_PASSWORDS // PasswordController.PASSWORDS_PER_FILE

        with ThreadPoolExecutor(max_workers=PasswordController.THREAD_POOL_SIZE) as executor:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            for i in range(num_files):
                file_name = os.path.join(
                    PasswordController.OUTPUT_DIR,
                    f'{PasswordController.PASSWORD_FILENAME}_{timestamp}_{i + 1}_of_{num_files}.txt'
                )
                executor.submit(self._generate_and_save, file_name, PasswordController.PASSWORDS_PER_FILE)


print("Starting password generation...\n")

controller = PasswordController()
controller.generate_password_files()

print("\n\nPassword generation complete...")