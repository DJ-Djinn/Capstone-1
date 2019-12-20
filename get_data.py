from mwclient import Site

pokepedia = 'bulbapedia.bulbagarden.net'
ua = "Trainer 'Mons tool (austindmccarthy@gmail.com)"
site = Site(pokepedia, clients_useragent=ua)

locations = ["Professor Oak's Laboratory", "Kanto Route 22", "Viridian Forest",\
             "Pewter Gym", "Kanto Route 3", "Mt. Moon", "Kanto Route 4", "Cerulean City",\
             "Kanto Route 24", "Kanto Route 25", "Cerulean Gym", "Kanto Route 6",\
             "Kanto Route 11", "S.S. Anne", "Vermilion Gym", "Kanto Route 9", "Kanto Route 10",\
             "Rock Tunnel", "Kanto Route 8", "Team Rocket Hideout", "Celadon Gym", "Silph Co.",\
             "Fighting Dojo", "Saffron Gym", "Pokémon Tower", "Katno Route 16", "Kanto Route 17",\
             "Kanto Route 18", "Fuchsia Gym", "Kanto Route 15", "Kanto Route 14", "Kanto Route 13",\
             "Kanto Route 12", "Kanto Route 19", "Kanto Route 20", "Pokémon Mansion (Kanto)",\
             "Cinnabar Gym", "Kanto Route 21", "Viridian Gym", "Victory Road (Kanto)", "Indigo Plateau"]
sections = [11, 11, 10, 5, 12, 24, 13, 27, 11, 10, 8, 10, 10, 6, 12, 10, 13, 20, 11, 5, 5,\
            17, 13, 8, 11, 12, 10, 10, 5, 13, 12, 10, 14, 11, 14, 9, 5, 10, 5, 22, 17]

if __name__ == '__main__':
    raw_data = []
    for loc, sec in zip(locations, sections):
        raw_data.append(site.pages[loc].text(section=sec))
    with open('raw_data.txt', 'w') as filehandle:
        for listitem in raw_data:
            filehandle.write(f"{listitem}")