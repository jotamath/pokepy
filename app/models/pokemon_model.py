class Pokemon:
    def __init__(self, name, height, weight, abilities):
        self.name = name
        self.height = height
        self.weight = weight
        self.abilities = abilities
    
    @staticmethod
    def from_api_response(data):
        name = data.get('name')
        height = data.get('height')
        weight = data.get('weight')
        abilities = [ability['ability']['name'] for ability in data['abilities']]
        return Pokemon(name, height, weight, abilities)