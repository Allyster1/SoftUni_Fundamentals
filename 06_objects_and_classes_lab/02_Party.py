class Party:
    def __init__(self):
        self.people = []

    def add_persion(self, name):
        self.people.append(name)

    def get_party_info(self):
        party_info = {
            'Going': ", ".join(party.people),
            'Total': len(party.people)
        }
        return party_info


party = Party()

while True:
    name = input()

    if name == "End":
        break

    party.add_persion(name)

info = party.get_party_info()
print(f'Going:', info['Going'])
print(f'Total:', info["Total"])
