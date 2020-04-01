class Character:
    def __init__(self, name, occupation, influence, attack, search, ability_location, ability_description, ability_roll = 0):
        self.name = name
        self.occupation = occupation
        
        self.influence = influence
        self.attack = attack
        self.search = search
        
        self.ability_location = ability_location
        self.ability_description = ability_description
        self.ability_roll = ability_roll

harman_brooks = Character("Harman Brooks", "Park Ranger", 32, 3, 3, "Anywhere", "If Harman would receive a frostbite wound, he receives a wound instead.")
sparky = Character("Sparky", "Stunt Dog", 10, 2, 2, "Anywhere", "When rolling for exposure with Sparky if you roll a bite, treat it as if you rolled a wound. When spreading a bite effect, ignore Sparky.")
thomas_heart = Character("Thomas Heart", "Soldier", 64, 1, 3, "Colony", "Once per round you may kill 2 zombies at the colony. Do not roll for exposure.", 5)
loretta_clay = Character("Loretta Clay", "Cook", 20, 2, 4, "Colony", "Once per round you may add 2 food tokens to the food supply.", 4)
janet_taylor = Character("Janet Taylor", "Nurse", 42, 3, 4, "Hospital", "Once per round, when performing a search at the hospital you may look at and keep 1 additional card.")
gray_beard = Character("Gray Beard", "Pirate", 16, 1, 4, "Colony", "Once per round you may take a card at random from another player's hand and place it into your hand.")
buddy_davis = Character("Buddy Davis", "Fitness Trainer", 36, 2, 4, "Anywhere", "It takes 4 or more wound tokens to kill Buddy instead of 3.")
forest_plum = Character("Forest Plum", "Mall Santa", 14, 2, 5, "Anywhere", "At the beginning of your turn you may remove Forest from the game to raise morale by 1.")
alexis_grey = Character("Alexis Grey", "Librarian", 46, 5, 4, "Library", "Once per round, when performing a search at the library you may look at and keep 1 additional card.")
rod_miller = Character("Rod Miller", "Truck Driver", 40, 3, 3, "Anywhere", "When moving Rod, do not roll for exposure.")
james_meyers = Character("James Meyers", "Psychiatrist", 54, 6, 3, "Anywhere", "Once per round you may reroll 1 or more of your unused action dice. You must keep the second result(s).")
olivia_brown = Character("Olivia Brown", "Doctor", 56, 4, 3, "Anywhere", "Once per round you may remove any type of wound token from a survivor that shares a location with Olivia. Olivia may use this ability on herself.")
ashley_ross = Character("Ashley Ross", "Construction Worker", 52, 2, 5, "Anywhere", "Once per round you may perform a barricade action without using an action die.")
bev_russell = Character("Bev Russell", "Mother", 34, 2, 4, "Colony", "Once per round you may kill 2 zombies at the colony as long as there is at least 1 helpless survivor token at the colony. Do not roll for exposure.", 1)
edward_white = Character("Edward White", "Chemist", 44, 4, 3, "Colony", "Once per round, when performing an attack with Edward, you may play a medicine card to kill 3 zombies instead of just 1. Do not roll for exposure. Do not use the ability on the medicine card.", 1)
arthur_thurston = Character("Arthur Thurston", "Principal", 62, 4, 2, "School", "Once per round, when performing a search at the school you may look at and keep 1 additional card.")
david_garcia = Character("David Garcia", "Accountant", 50, 4, 3, "Anywhere", "When performing a search with David you may look at 1 additional card.")
maria_lopez = Character("Maria Lopez", "Teacher", 48, 4, 2, "School", "Once per round you may kill 1 zombie at the school. Do not roll for exposure.", 1)
gabriel_diaz = Character("Gabriel Diaz", "Fireman", 60, 2, 3, "Anywhere", "Once per round, when Gabriel is at a location with an item deck, you may reveal the top 4 cards of that item deck. If you revealed any outsider cards you may place 1 into your hand. Shuffle the remaining cards back into the item deck.")
andrew_evans = Character("Andrew Evans", "Farmer", 12, 3, 3, "Grocery Store", "Once per round, when performing a search at the grocery store you may look at and keep 1 additional card.")
carla_thompson = Character("Carla Thompson", "Police Dispatcher", 22, 4, 2, "Police Station", "Once per round, when performing a search at the police station you may look at and keep 1 additional card.")
john_price = Character("John Price", "Student", 18, 3, 3, "Non-colony", "When John is not at the colony, he is considered to have the ability of every other survivor he shares a location with.")
mike_cho = Character("Mike Cho", "Ninja", 30, 2, 4, "Anywhere", "When performing an attack with Mike do not roll for exposure.")
annaleigh_chan = Character("Annaleigh Chan", "Lawyer", 38, 2, 2, "Colony", "Once per round you may look at 1 card at random in a player's hand.")
talia_jones = Character("Talia Jones", "Fortune Teller", 28, 3, 1, "Anywhere", "Once per round you may look at the top 2 cards of the crisis deck and place them back in any order. Then you may say exactly 2 words to all players about the crisis cards, nothing more.")
jenny_clark = Character("Jenny Clark", "Waitress", 24, 4, 3, "Anywhere", "Once per round when performing a search with Jenny you may look at 3 additional cards.")
brian_lee = Character("Brian Lee", "Mayor", 68, 3, 4, "Anywhere", "Once per round you may increase an unused action die you control by 1.")
sophie_robinson = Character("Sophie Robinson", "Pilot", 58, 4, 1, "Anywhere", "Once per round you may look at the top card of a single location's item deck. After you have looked at the card place it back on top of that item deck.")
brandon_kane = Character("Brandon Kane", "Janitor", 26, 2, 4, "Colony", "Once per round you may remove 5 cards instead of 3 from the waste pile when taking the clean waste action.")
daniel_smith = Character("Daniel Smith", "Sheriff", 66, 2, 5, "Anywhere", "Once per round you may kill 2 zombies at Daniel's current location. Only roll for exposure once.", 4)

characters = [harman_brooks, sparky, thomas_heart, loretta_clay, janet_taylor, gray_beard,\
              buddy_davis, forest_plum, alexis_grey, rod_miller, james_meyers, olivia_brown,\
              ashley_ross, bev_russell, edward_white, arthur_thurston, david_garcia,\
              maria_lopez, gabriel_diaz, andrew_evans, carla_thompson, john_price,\
              mike_cho, annaleigh_chan, talia_jones, jenny_clark, brian_lee, sophie_robinson,\
              brandon_kane, daniel_smith]