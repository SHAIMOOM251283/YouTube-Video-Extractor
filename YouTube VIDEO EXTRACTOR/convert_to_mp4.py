import subprocess

class Converter:

    def __init__(self):
        file = input("Enter File Name (without extension): ")
        self.input_file = f"{file}.webm"  # Corrected: Append ".webm" to the user input
        self.output_file = f"{file}.mp4"  # Corrected: Append ".mp4" to the user input

    def convert_webm_to_mp4(self):
        # Command to convert .webm to .mp4
        command = ['ffmpeg', '-i', self.input_file, self.output_file]
    
        try:
            # Running the command
            subprocess.run(command, check=True)
            print(f"Conversion successful: {self.input_file} to {self.output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error during conversion: {e}")

if __name__ == '__main__':
    convert = Converter()
    convert.convert_webm_to_mp4()
