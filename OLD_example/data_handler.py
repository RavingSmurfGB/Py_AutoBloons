import logger

Logger = logger.Logger()

class Handler:
    def __init__(self, data_path:str):
        self.data_path = data_path

    def read_data(self, data_name:str):
        with open(self.data_path + "/" + data_name, "r") as file:
            lines = [r.replace("\n","") for r in file.readlines()]
            file.close()
        return lines
