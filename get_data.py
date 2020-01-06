from mwclient import Site

pokepedia = 'bulbapedia.bulbagarden.net'
ua = "Trainer 'Mons tool (austindmccarthy@gmail.com)"
site = Site(pokepedia, clients_useragent=ua)

gen_one_locations = ["Professor Oak's Laboratory", "Kanto Route 22", "Viridian Forest",\
                     "Pewter Gym", "Kanto Route 3", "Mt. Moon", "Kanto Route 4", "Cerulean City",\
                     "Kanto Route 24", "Kanto Route 25", "Cerulean Gym", "Kanto Route 6",\
                     "Kanto Route 11", "S.S. Anne", "Vermilion Gym", "Kanto Route 9", "Kanto Route 10",\
                     "Rock Tunnel", "Kanto Route 8", "Team Rocket Hideout", "Celadon Gym",\
                     "Silph Co.", "Fighting Dojo", "Saffron Gym", "Pokémon Tower", "Katno Route 16", \
                     "Kanto Route 17", "Kanto Route 18", "Fuchsia Gym", "Kanto Route 15",\
                     "Kanto Route 14", "Kanto Route 13", "Kanto Route 12", "Kanto Route 19",\
                     "Kanto Route 20", "Pokémon Mansion (Kanto)", "Cinnabar Gym", "Kanto Route 21",\
                     "Viridian Gym", "Victory Road (Kanto)", "Indigo Plateau/Generation I"]
gen_one_sections = [11, 11, 10, 5, 12, 24, 13, 27, 11, 10, 8, 10, 10, 6, 12, 10, 13, 20,\
                    11, 5, 5, 17, 13, 8, 11, 12, 10, 10, 5, 13, 12, 10, 14, 11, 14, 9, 5,\
                    10, 5, 22, 1]

gen_two_locations = ["Cherrygrove City", "Johto Route 30", "Johto Route 31", "Violet Gym",\
                     "Johto Route 32", "Union Cave", "Johto Route 33", "Slowpoke Well", "Azalea Gym",\
                     "Azalea Town", "Ilex Forest", "Johto Route 34", "Goldenrod Tunnel",\
                     "Goldenrod Radio Tower", "Goldenrod Gym", "Johto Route 35", "National Park",\
                     "Johto Route 36", "Johto Route 37", "Ecruteak City", "Burned Tower",\
                     "Ecruteak Gym", "Johto Route 38", "Johto Route 39", "Glitter Lighthouse",\
                     "Olivine Gym", "Johto Route 40", "Johto Route 41", "Cianwood City",\
                     "Cianwood Gym", "Johto Route 42", "Mt. Mortar", "Johto Route 43", "Lake of Rage",\
                     "Mahogany Gym", "Johto Route 44", "Blackthorn Gym", "Dragon's Den",\
                     "Johto Route 45", "Ruins of Alph", "Johto Route 46", "Kanto Route 27",\
                     "Kanto Route 26", "Victory Road (Kanto)", "Indigo Plateau/Generation II",\
                     "Indigo Plateau/Generation II", "Indigo Plateau/Generation II",\
                     "Indigo Plateau/Generation II", "Indigo Plateau/Generation II"]
gen_two_sections = [16, 7, 8, 7, 7, 13, 7, 13, 7, 18, 10, 8, 12, 9, 7, 7, 10, 9, 7, 20, 12,\
                    7, 7, 7, 3, 8, 7, 7, 21, 7, 7, 20, 7, 7, 7, 8, 7, 7, 25, 7, 9, 9, 23, 1,\
                    2, 3, 4, 5]

gen_three_locations = ["Hoenn Route 103", "Hoenn Route 102", "Pegtalburg Gym", "Hoenn Route 104",\
                       "Petalburg Woods", "Rustboro Gym", "Hoenn Route 116", "Rusturf Tunnel",\
                       "Hoenn Route 105", "Hoenn Route 106", "Gewford Gym", "Hoenn Route 107",\
                       "Hoenn Route 108", "Abandoned Ship", "Hoenn Route 109", "Oceanic Museum",\
                       "Hoenn Route 110", "Seaside Cycling Road", "Trick House", "Trick House",\
                       "Trick House", "Trick House", "Trick House", "Trick House", "Trick House",\
                       "Mauville City", "Mauville Gym", "Hoenn Route 117", "Hoenn Route 118",\
                       "Hoenn Route 111", "Winstrate Family", "Hoenn Route 112", "Mt. Chimney",\
                       "Jagged Pass", "Lavaridge Gym", "Hoenn Route 113", "Hoenn Route 114",\
                       "Meteor Falls", "Hoenn Route 115", "Hoenn Route 119", "Weather Institute",\
                       "Fortree Gym", "Hoenn Route 120", "Hoenn Route 121", "Mt. Pyre", "Hoenn Route 123",\
                       "Lilycove City", "Team Aqua Hideout", "Hoenn Route 124", "Mossdeep Gym",\
                       "Hoenn Route 125", "Hoenn Route 126", "Hoenn Route 127", "Hoenn Route 128",\
                       "Hoenn Route 129", "Hoenn Route 130", "Hoenn Route 131", "Hoenn Route 132",\
                       "Hoenn Route 133", "Hoenn Route 134", "Seafloor Cavern", "Sootopolis Gym",\
                       "Victory Road (Hoenn)", "Ever Grande City", "Ever Grande City", "Ever Grande City",\
                       "Ever Grande City", "Ever Grande City"]
gen_three_sections = [9, 8, 4, 14, 8, 6, 7, 8, 8, 8, 7, 9, 8, 6, 9, 8, 8, 7, 14, 19, 24, 29,\
                      39, 43, 48, 39, 6, 7, 10, 17, 4, 11, 5, 8, 6, 8, 10, 16, 7, 9, 11, 4, 12,\
                      7, 15, 15, 25, 11, 11, 6, 7, 11, 9, 11, 10, 11, 8, 7, 7, 7, 12, 6, 11,\
                      8, 14, 20, 26, 32]

gen_four_locations = []
gen_four_sections = []

gen_five_loctions = []
gen_five_sections = []

gen_six_locations = []
gen_six_sections = []

gen_seven_locations = []
gen_seven_sections = []

gen_eight_locations = []
gen_eight_sections = []
if __name__ == '__main__':
    raw_data = []
    for loc, sec in zip(locations, sections):
        raw_data.append(site.pages[loc].text(section=sec))
    with open('raw_data.txt', 'w') as filehandle:
        for listitem in raw_data:
            filehandle.write(f"{listitem}")