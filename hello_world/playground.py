import file
import utils

class Playground:
    def get_data(self) -> list:

        return utils.fetch('')
    
    def get_data_from_file(self):
        return file.read_text_file_stream('')
    
playground = Playground()
response = playground.get_data()
print(response)
print(playground.get_data_from_file())