#  Info

link = 'https://probe.fbrq.cloud/docs'
server = 'https://probe.fbrq.cloud/v1'


class Schemas:
    def __init__(self, name):
        self.name = name
        self.types = {}

ApiResponse = Schemas('ApiResponse')
ApiResponse.types = {'code': int, 'message': str}
Msg = ApiResponse = Schemas('Msg')
ApiResponse.types = {'id': int, 'phone': int, 'text': str}
