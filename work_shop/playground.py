import file
import utils

class Playground:
    def get_data(self) -> list:

        return utils.fetch('https://webhook.site/04f01637-5b67-44a5-9982-f1ddc722d086')
    
    def get_data_from_file(self):
        return file.read_text_file_stream('/Users/samat-tolkunbekov/Repositories/hagrid/storage/sample3.txt')
    
playground = Playground()
response = playground.get_data()
print(response)
print(playground.get_data_from_file())