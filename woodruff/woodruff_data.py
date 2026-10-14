from dataclasses import dataclass
from enum import IntEnum


#####################################
# ZONES
# List of zones in the game
#####################################

@dataclass(frozen=True)
class Zone:
    id: int  # ID of zone ingame
    map: str  # ID of map file / TOT file
    key: str  # Zone identifier (3 letters)
    name: str  # Zone full name
    connections: tuple[str, ...] = ()  # Connections with other zones

ZONES: tuple[Zone, ...] = (
    Zone(1, "EMAP2001", "STS", "Stairs Street", ("AZI", "WNO", "MEM")),
    Zone(2, "EMAP2002", "AZI", "Azimuth's house", ("STS", "SAD", "ADM")),
    Zone(3, "EMAP2003", "SAD", "Street of the Sad Boozook", ("SAD", "BRS")),
    Zone(4, "EMAP2004", "BRS", "Bridge of the Slums", ("BRS", "WNO")),
    Zone(5, "EMAP2005", "WNO", "Wino's Alley", ("BRS", "BAR", "STS")),
    Zone(6, "EMAP2006", "VTT", "Virtual Trip Tower", ("RLD",)),
    Zone(7, "EMAP2007", "ADM", "Administration Center", ("AZI", "BRO")),
    Zone(8, "EMAP2008", "HMC", "High Morals Club", ("ADM",)),
    Zone(9, "EMAP2009", "TIT", "Title Boulevard", ("BAR",)),
    Zone(10, "EMAP2010", "BAR", "Bar of Friendship", ("WNO", "TIT")),
    # EMAP2011 is for Virtual trip animations and game overs
    Zone(12, "EMAP2012", "BRO", "Brotoflatron's Plazza", ("CUI", "BGA")),
    Zone(13, "EMAP2013", "CUI", "Cui-cui store", ("BRO", "CGR")),
    Zone(14, "EMAP2014", "CGR", "Clandestine Gaming Room", ("CUI", "RLD")),
    Zone(15, "EMAP2015", "RLD", "Red Light District", ("CGR", "VTT")),
    Zone(16, "EMAP2016", "PLF", "Place of the Fountain", ("BGA", "SDE", "TPF")),
    Zone(17, "EMAP2017", "BGA", "Bigwig's Area", ("BRO", "PLF", "FCF", "SEC")),
    Zone(18, "EMAP2018", "SEC", "Schnibble's Sect", ("BGA",)),
    Zone(19, "EMAP2019", "SDE", "Slammer's Dead End", ("PLF", "RLD", "PRC")),
    Zone(20, "EMAP2020", "TPF", "Temple's Front yard", ("PLF", "FCF", "TP1")),
    Zone(21, "EMAP2021", "FCF", "Factory's Front yard", ("BGA", "TPF", "FAC")),
    Zone(22, "EMAP2022", "FAC", "Hat Division", ("FCF", "HOH")),
    Zone(23, "EMAP2023", "HOH", "Home of Happiness", ("LAB",)),
    Zone(24, "EMAP2024", "PRC", "Prison's Courtyard", ("SDE", "PRT")),
    Zone(25, "EMAP2025", "TP1", "Temple's Hallways level 1", ("TPF", "TP2", "TP3")),
    Zone(26, "EMAP2026", "TER", "Aristocrats Terrace", ("FCF", "PAR")),
    Zone(27, "EMAP2027", "FAN", "Fan's platform", ("LAB", "HMC", "TER")),
    Zone(28, "EMAP2028", "LAB", "Experimentation Lab", ("SDE", "HOH", "FAN")),
    Zone(29, "EMAP2029", "PRT", "Prison's Central Tower", ("PRC", "CEL")),
    Zone(30, "EMAP2030", "THR", "Throne Room", ("TP3",)),
    Zone(31, "EMAP2031", "CNC", "Council Chambers", ("TP2",)),
    Zone(32, "EMAP2032", "PAR", "Big \"Eye\" Party", ("TER", "COH")),
    Zone(33, "EMAP2033", "COH", "Coh Cott Quarters", ("TER", "BGQ")),
    Zone(34, "EMAP2034", "BGQ", "At the Bigwig's", ("COH", "FCF", "END")),
    Zone(35, "EMAP2035", "END", "Ending"),
    Zone(36, "EMAP2036", "CEL", "Azimuth's Cell", ("PRT",)),
    Zone(37, "EMAP2037", "MEM", "Memorial", ("STS", "PST")),
    # EMAP2038 not used
    Zone(39, "EMAP2039", "PST", "Peace Plazza", ("MEM",)),
    # EMAP2040 not used
    Zone(41, "EMAP2041", "TP2", "Temple's Hallways level 2", ("TP1", "TP3", "CNC")),
    Zone(42, "EMAP2042", "TP3", "Temple's Hallways level 3", ("TP1", "TP2", "THR")),
    # EMAP2043 is for Asylum Cell
    # EMAP2044 is for Transportozon
)
ZONE_BY_KEY: dict[str, Zone] = {z.key: z for z in ZONES}
ZONE_BY_ID: dict[int, Zone] = {z.id: z for z in ZONES}




#####################################
# ENTITIES
# List of entities / hotspots attached to zones
# Not all game entities are declared, only those needed to detect locations or to apply patches
#####################################

@dataclass(frozen=True)
class Entity:
    zone: Zone # Zone in which is the entity
    name: str # Unique name
    hotspot_id: int  # ID of hotspot in current zone
    mult_object_id: int = None # ID of mult object in current zone

ENTITIES: tuple[Entity, ...] = (
    Entity(ZONE_BY_KEY["STS"], "STS_Can", 11),
    Entity(ZONE_BY_KEY["STS"], "STS_Bean", 12),
    Entity(ZONE_BY_KEY["STS"], "STS_Window", 15),
    Entity(ZONE_BY_KEY["STS"], "STS_Morphoplastoc_Eye", 17),

    Entity(ZONE_BY_KEY["AZI"], "AZI_Button", 19, 15),

    Entity(ZONE_BY_KEY["SAD"], "SAD_Woman", 10),
    Entity(ZONE_BY_KEY["SAD"], "SAD_Rock", 12),

    Entity(ZONE_BY_KEY["BRS"], "BRS_Boot", 12, 14),
    Entity(ZONE_BY_KEY["BRS"], "BRS_Nut", 17, 15),

    Entity(ZONE_BY_KEY["WNO"], "WNO_Feathers", 13),
    Entity(ZONE_BY_KEY["WNO"], "WNO_Riri", 14),

    Entity(ZONE_BY_KEY["ADM"], "ADM_Tag", 8),
    Entity(ZONE_BY_KEY["ADM"], "ADM_Bluxtre_Pulp", 21),
    Entity(ZONE_BY_KEY["ADM"], "ADM_Meteorite", 25),

    Entity(ZONE_BY_KEY["HMC"], "HMC_Cartoon_Videotape", 17),
    Entity(ZONE_BY_KEY["HMC"], "HMC_Diva_Videotape", 18),
    Entity(ZONE_BY_KEY["HMC"], "HMC_Circus_Videotape", 19),
    Entity(ZONE_BY_KEY["HMC"], "HMC_Magnetoscopon", 20),

    Entity(ZONE_BY_KEY["TIT"], "TIT_Brush", 10),

    Entity(ZONE_BY_KEY["BAR"], "BAR_Barman_Pocket", 8),
    Entity(ZONE_BY_KEY["BAR"], "BAR_Coffee", 201, 15),
    Entity(ZONE_BY_KEY["BAR"], "BAR_JF_Sebastien", 202),

    Entity(ZONE_BY_KEY["BRO"], "BRO_Morphoplastoc_Finger", 9),
    Entity(ZONE_BY_KEY["BRO"], "BRO_Meteorite", 21),
    Entity(ZONE_BY_KEY["BRO"], "BRO_Bluxtre_Pulp", 24),

    Entity(ZONE_BY_KEY["CUI"], "CUI_Water_Reservoir", 202),

    Entity(ZONE_BY_KEY["RLD"], "RLD_Strul", 12),

    Entity(ZONE_BY_KEY["PLF"], "PLF_Public_Tobozon", 10),
    Entity(ZONE_BY_KEY["PLF"], "PLF_Talent_Wiseman", 12),

    Entity(ZONE_BY_KEY["BGA"], "BGA_Shirt", 10),
    Entity(ZONE_BY_KEY["BGA"], "BGA_Stain", 11),
    Entity(ZONE_BY_KEY["BGA"], "BGA_Trash_Bag", 12),
    Entity(ZONE_BY_KEY["BGA"], "BGA_Bluxtre_Pulp", 24),
    Entity(ZONE_BY_KEY["BGA"], "BGA_Meteorite", 25),

    Entity(ZONE_BY_KEY["SEC"], "SEC_Ceedeerom", 15),

    Entity(ZONE_BY_KEY["SDE"], "SDE_Fish_Imprint", 10),
    Entity(ZONE_BY_KEY["SDE"], "SDE_Stone_Arm", 14),
    Entity(ZONE_BY_KEY["SDE"], "SDE_Shell", 15),

    Entity(ZONE_BY_KEY["PRC"], "PRC_Rag", 11),

    Entity(ZONE_BY_KEY["TP1"], "TP1_Lid", 6),
    Entity(ZONE_BY_KEY["TP1"], "TP1_Gasoline", 11),

    Entity(ZONE_BY_KEY["TER"], "TER_Spiral_Imprint", 10),

    Entity(ZONE_BY_KEY["LAB"], "LAB_Schnaplure_Seed", 14),
    Entity(ZONE_BY_KEY["LAB"], "LAB_Tubes_1", 201),
    Entity(ZONE_BY_KEY["LAB"], "LAB_Tubes_2", 2000),

    Entity(ZONE_BY_KEY["PRT"], "PRT_Rope", 11),

    Entity(ZONE_BY_KEY["THR"], "THR_King", 10),
    Entity(ZONE_BY_KEY["THR"], "THR_Chewing_Gum", 13),
    Entity(ZONE_BY_KEY["THR"], "THR_Boozook_Formulas", 14),

    Entity(ZONE_BY_KEY["BGQ"], "BGQ_Clothes", 18),

    Entity(ZONE_BY_KEY["MEM"], "MEM_Armor", 9),

    Entity(ZONE_BY_KEY["PST"], "PST_Corn_Ear", 10),
    Entity(ZONE_BY_KEY["PST"], "PST_Trident", 14),
    Entity(ZONE_BY_KEY["PST"], "PST_Helmet", 17),

    Entity(ZONE_BY_KEY["TP3"], "TP3_Pet", 11),
)
ENTITY_BY_NAME: dict[str, Entity] = {e.name: e for e in ENTITIES}





#####################################
# ITEMS
# List of all inventory items
#####################################

@dataclass(frozen=True)
class Item:
    id: int  # Index of item in game inventory
    key: str   # Item name in game inventory
    name: str  # Item full name

ITEMS: tuple[Item, ...] = (
    Item(0, "BUTTON", "Button"),
    Item(1, "BOOT", "Boot"),
    Item(2, "PAIR OF BOOTS", "Pair of boots"),
    Item(3, "PHOTO AZIMUTH", "Azimuth photo"),
    Item(4, "NUT", "Nut"),
    Item(5, "BLUXTRE NUT", "Bluxtre nut"),
    Item(6, "BLUXTRE PULP", "Bluxtre pulp"),
    Item(7, "BRUSH", "Brush"),
    Item(8, "NUT WITH TAR", "Bluxtre nut with tar"),
    Item(9, "FEATHERS", "Feathers"),
    Item(10, "COFFEE", "Coffee"),
    Item(11, "IDENTITY PHOTO", "Identity photo"),
    Item(12, "WEATHER WATCH", "Weather watch"),
    Item(13, "BRUSH WITH TAR", "Brush with tar"),
    Item(14, "RUMMY RULES", "Rummy rules"),
    Item(15, "BEAN", "Bean"),
    Item(16, "CAN", "Can"),
    Item(17, "KITE", "Kite"),
    Item(18, "PLASTOC EYE", "Morphoplastoc eye"),
    Item(19, "\"A\" STONE", "\"A\" stone"),
    Item(20, "ARTICLE", "Azimuth article"),
    Item(21, "TOBOZON", "Tobozon"),
    Item(22, "BREATH.CERTIF.", "Breath certificate"),
    Item(23, "FORM.", "Prison form"),
    Item(24, "PLASTOC FINGER", "Morphoplastoc finger"),
    Item(25, "SHIRT FRONT", "Shirt"),
    Item(26, "GLASSES", "Glasses"),
    Item(27, "PLASTOC CHIN", "Morphoplastoc chin"),
    Item(28, "HAT", "Hat"),
    Item(29, "WATER HAT", "Water hat"),
    Item(30, "CHEWING-GUM", "Chewing-gum"),
    Item(31, "STRUL(S)", "Struls"),
    Item(32, "METEORITE", "Meteorite"),
    Item(33, "STONE FISH", "Stone fish"),
    Item(34, "KEY RING", "Keyring"),
    Item(35, "GASOLINE", "Gasoline"),
    Item(36, "STONE ARM", "Stone arm"),
    Item(37, "GRABBER", "Grabber"),
    Item(38, "SCHNAPL. SEED", "Schnaplure seed"),
    Item(39, "SCHNAPL. SPICE", "Schnaplure spice"),
    Item(40, "ANTIDOTE", "Antidote"),
    Item(41, "LID", "Lid"),
    Item(42, "TRIDENT", "Trident"),
    Item(43, "RED FISH", "Red fish"),
    Item(44, "HORN", "Horn"),
    Item(45, "CEEDEEROM", "Hypnotic ceedeerom"),
    Item(46, "PIECE OF CHAIN", "Piece of chain"),
    Item(47, "SCREW", "Screw"),
    Item(48, "RAG", "Rag"),
    Item(49, "EMPLOYM. CERT.", "Employment certificate"),
    Item(50, "CORN EAR", "Corn ear"),
    Item(51, "TRASH BAG", "Trash bag"),
    Item(52, "BOTTLE-OPENER", "Bottle opener"),
    Item(53, "TRANSPORTOZON", "Transportozon"),
    Item(54, "PHOTO BOX", "Photo box"),
    Item(55, "BOUZ. FORMULAE", "Boozook formulas"),
    # 56 Not used ("VIBLEFROTZER")
    Item(57, "VIBLEFROTZER2", "Viblefrotzer"),
    Item(58, "SCHPROTZNOG", "Schprotznog"),
    # 59 Not used ("CEEDEEROM2")
    Item(60, "USELESS PHOTO", "Useless photo"),
    Item(61, "ROTTEN PHOTO", "Rotten photo"),
    Item(62, "MEDIOCRE PHOTO", "Mediocre photo"),
    Item(63, "PASSABLE PHOTO", "Passable photo"),
    Item(64, "AVERAGE PHOTO", "Average photo"),
    Item(65, "PERFECT PHOTO", "Perfect photo"),
    Item(66, "MANTRA", "Mantra"),
    # 67 Not used ("67")
    Item(68, "SHELL", "Shell"),
    Item(69, "CARTOON VIDEO.", "Cartoon videotape"),
    Item(70, "DIVA VIDEOTAPE", "Diva videotape"),
    Item(71, "CIRCUS VIDEOT.", "Circus videotape"),
    Item(72, "MAGNETIC CARD", "Magnetic card"),
    Item(73, "BOUZOUIOLI", "Bouzouioli"),
    Item(74, "ACCESSOR. BOX", "Accessory box"),
    Item(75, "PAPER BOX", "Paper box"),
    Item(76, "MASTERS POWERS", "Masters powers"),
    # 77 Not used
    # 78 Not used
    # 79 Not used
    Item(80, "MEMORY FORM.", "Memory formula"),
    Item(81, "HAPPINESS FORM", "Happiness formula"),
    Item(82, "INSIGHT FORM.", "Insight formula"),
    Item(83, "GROWTH FORMUL.", "Growth formula"),
    Item(84, "PAST FORMULA", "Past formula"),
    Item(85, "STRENGHT FORM.", "Strength formula"),
    Item(86, "DIAGNOS. FORM.", "Diagnosis formula"),
    Item(87, "LEADING SYLLA.", "Leading syllable"),
    Item(88, "ADVICE SYLLAB.", "Advice syllable"),
    Item(89, "BASIC SYLLABLE", "Basic syllable"),
    Item(90, "TIME SYLLABLE", "Time syllable"),
    Item(91, "GREEN SYLLABLE", "Green syllable"),
    Item(92, "ARTISTIC SYLL.", "Artistic syllable"),
    Item(93, "HEALING SYLL.", "Healing syllable"),
    Item(94, "INTUITIVE SYLL", "Intuitive syllable"),
    Item(95, "ENERGY SYLLAB.", "Energy syllable"),
    Item(96, "SYLLABLES BAG", "Syllable bag"),
    Item(97, "POWERS BAG", "Powers bag"),
    Item(98, "CREATE FORMULA", "Create formula"),
    # 99 Not used ("99")
    Item(100, "AURICULAR CNTR", "Auricular control"),
    Item(101, "HAIR CONTROL", "Hair control"),
    Item(102, "OCULAR CONTROL", "Ocular control"),
    Item(103, "NASAL CONTROL", "Nasal control"),
    Item(104, "FACIAL CONTROL", "Facial control"),
    Item(105, "LEVITATION", "Levitation"),
)
ITEM_BY_NAME: dict[str, Item] = {i.name: i for i in ITEMS}
ITEM_BY_ID: dict[int, Item] = {i.id: i for i in ITEMS}
ITEM_MAX_ID = max(ITEM_BY_ID.keys())




#####################################
# FLAGS
# List of all flags in the game
# Flags determine game state in various aspects
#####################################

class Flag(IntEnum):
    OBJECT_HELD              =   0 # ID of used object, 255 if no item
    SKILL_BOOTS              =   1 # Status of boots. 0 = no boots, 1 = one boot in inventory, 2 = wear boots
    BRS_BEGGAR_DIAL          =   2 # Dialogue with Bridge beggar
                                   # 3 -- Used for something in Bridge
    BRS_NUT_STATE            =   4 # State of nut in Bridge. 0 = under box, 1 = box help up, 2 = outside
    ENTRY_POINT              =   5 # Entry point used to determinate Woodruff entrance animation
    WNO_SWITCH               =   6 # State of switch in Wino Alley. 0 = on, 1 = off, default = 1
    RIRI_MET                 =   7 # Indicate if Riri has been met in present or not. 0 = not met in Slammer's dead end, 1 = met, 2 = talked to in Wino Alley
    WNO_WINO_STATE           =   8 # State of wino in Wino Alley. 0 = drunk, 1 = after coffee, 2 = after restoring memory, 3 = after giving him photo
    WNO_DOOR_ANIM            =   9 # Animation of door to Bar of Friendship. 0 = not played, 1 = already played
    HAS_TOBOZON              =  10 # If player has recieved Tobozon
                                   # 11 -- Used for tobozon meteo
    BAR_TAXMAN_DIAL          =  12 # Dialogue with taxman in Bar music instruments
    BAR_IS_DOOR_OPENED       =  13 # State of door to Red Light District. 0 = blocked by bar owner, 1 = open
    BAR_JF_ACCESS            =  14 # Indicate if Woodruff knows the name of JF Sebastien and can have a dialogue with him
    BAR_BARMAN_HS_X          =  15 # Position of barman pocket Hotspot. Used to deactivate interaction after picking up bottle opener. Default = 292, after = 1000
                                   # 16 -- Used for barman
    STRULS                   =  17 # Number of struls
    BRO_ACCESSORY_WEAR       =  18 # Number of accessory weared when taking a brotoflatron photo
    HAS_PHOTO_0              =  19 # If player has simple identity photo. Used for brotoflatron photo and wino interaction
    HAS_SENT_PHOTO_4         =  20 # If player has sent photo 4 (4 accessories without smiling). Used for brotoflatron photo
    HAS_PHOTO_1              =  21 # If player has useless photo
    HAS_PHOTO_2              =  22 # If player has rotten photo
    BRO_FAN_ON               =  23 # Indicate if fan is running in Brotoflatron plazza. 0 = on, 1 = off
    WOODRUFF_STATE           =  24 # Indicate Woodruff state. 1 = normal, 4 = in cell ? Seems to control animations
    AZI_HOUSE_DIAL           =  25 # Dialogue when entering Azimuth house
    AZI_BOOT_TOP_PICKUP      =  26 # If top boot have been picked up. Used for interaction with boots
    AZI_BOOT_BOT_PICKUP      =  27 # If bottom boot have been picked up
    SKILL_READ               =  28 # Indicate if Woodruff learned reading. 0 = = no, 1 = yes
    AZI_ELEVATOR_ANIM        =  29 # Animation of Azimuth house elevator when Woodruff use it the first time after learning how to read. 0 = not played, 1 = already played
    AZI_ELEVATOR_DIAL        =  30 # Dialogue with Azimuth house elevator when Woodruff can't read
    AZI_TAXMAN_DIAL          =  31 # Dialogue with taxman in Azimuth house bin
                                   # 32 -- Used in Administration center
    ADM_TAXMAN_DIAL          =  33 # Dialogue with taxman in Administration center stall
    BLUXTRE_NUT_ACCESS       =  34 # Indicate if Woodruff knows about the bluxtre nut (spoke to Boozook temple keeper). Controls the interaction with nut merchant in Administration center and elevator blocked in Virtual trip
                                   # 35 -- Used in Administration center
    ADM_BREATH_CERTIF_ACCESS =  36 # Indicate if Woodruff is searching for breath certificate. 0 = no (didn't call recruitment number), 1 = yes, 2 = obtained
    ADM_PRISON_FORM_ACCESS   =  37 # Indicate if Woodruff is searching for prison administrative form. 0 = no (didn't try to reach prison), 1 = yes, 2 = obtained
    STS_CAN_STATE            =  38 # Can state in Stairs street. 0 = not kicked, 1 = kicked one time, 2 = kicked two times, 3 = picked up
    STS_PLASTOC_EYE_STATE    =  39 # Indicate plastoc eye location. 0 = not visible, 1 = in stairs street, 2 = picked up
                                   # 40 -- Used in Cui-cui store
                                   # 41 -- Used in Cui-cui store
    CUI_BIRD_STATE           =  42 # Jeff state in Cui-cui store. 0 = looking at woman poster, 1 = speech, 2 = gone to High Morals Club
    CUI_CHEWING_GUM_STATE    =  43 # Chewing-gum state for temporal syllable machine. 0 = none, 1 = on pipe
    CUI_FLOPPER_POS          =  44 # Position of flopper in Cui-cui store, 0 1 or 2. Good pos = 2
    CUI_GLAPPER_POS          =  45 # Position of glapper in Cui-cui-store, 0 1 or 2. Good pos = 1
    HAS_CALLED_RECRUIT       =  46 # Indicate if recruitment number has already been called
    TOB_COHCOTT_STATE        =  47 # State of relationship with Coh-cott using Tobozon. 0 = don't have number, 1 = probably not used, 2 = waiting for call, 3 = friendly, Riri met, 4 = captured by beast
    HAS_SENT_CERTIF          =  48 # Indicate if breath certificate has been sent by Tobozon to recruitment center
    METEO_1                  =  49 # Meteo possibility #1
    METEO_2                  =  50 # Meteo possibility #2
    METEO_3                  =  51 # Meteo possibility #3
    METEO_4                  =  52 # Meteo possibility #4
    METEO_5                  =  53 # Meteo possibility #5
    METEO_6                  =  54 # Meteo possibility #6
    METEO_METEORITE_STATE    =  55 # Used for meteo - meteorite (general)
    METEO_ADM_WIND_STATE     =  56 # Used for meteo - wind in Administration center
    METEO_BRO_METEORITE_ST   =  57 # Used for meteo - meteorite in Brotoflatron plazza
    METEO_BRO_RAIN_STATE     =  58 # Used for meteo - rain in Brotoflatron plazza
                                   # 59 -- Not used ?
    AZI_LOOKER_DIAL          =  60 # Dialogue with looker in Azimuth house
                                   # 61 -- Used for Azimuth house looker dialogue
                                   # 62 -- Used for Azimuth house looker dialogue
    SAD_BOOZOOK_DIAL         =  63 # Dialogue with sad boozook in Sad boozook street
    SAD_WOMAN_DIAL           =  64 # Dialogue with young woman in Sad boozook stree
    WNO_WINO_DIAL            =  65 # Dialogue with wino in Wino alley after restoring his memory
    BAR_OWNER_DIAL           =  66 # Dialogue with Bar owner
    BAR_JF_DIAL              =  67 # Dialogue with JF Sebastien in Bar
    BRS_BOX_STATE            =  68 # Used for Bridge box management. 0 = down, 1 = up
                                   # 69 -- Used for menu
                                   # 70 -- Used for menu
    BAR_TITLE_WARP_STATE     =  71 # Indicate if already warped to Title screen from Bar. 0 = no, 1 = yes
                                   # 72 -- Used for meteo
    COHCOTT_TOBOZON_DIAL     =  73 # Tobozon dialogue with Coh-cott (before Riri saved)
    HAS_SENT_GOOD_PHOTO      =  74 # Indicate if perfect photo has been sent by Tobozon to recruitment center
    VTT_IS_BOULD_REMOVED     =  75 # Indicate if boulder have been removed in Virtual trip tower (block access from Brotoflatron plazza). 0 = no, 1 = yes
    HAS_PHOTO_4              =  76 # If player has passable photo
    HAS_PHOTO_6              =  77 # If player has perfect photo
    HAS_PHOTO_5              =  78 # If player has average photo
    HAS_PHOTO_3              =  79 # If player has mediocre photo
    LAB_PROF_DIAL            =  80 # Dialogue with professor in Laboratory
    LAB_FERT_WISEMAN_DIAL    =  81 # Dialogue with Fertility Wiseman in Laboratory
    THR_STR_WISEMAN_DIAL     =  82 # Dialogue with Strength Wiseman in Throne room
    COH_COHCOTT_DIAL         =  83 # Dialogue with Coh-cott in Coh-cott quarters
    PAR_COHCOTT_DIAL         =  84 # Dialogue with Coh-cott during "Eye" party after she has been healed with antidote
    CEL_AZIMUTH_DIAL         =  85 # Dialogue with Azimuth in cell
    ADM_RIRI_STATE           =  86 # Controls the apparition of Riri in Administration center. 0 = not appeared, 1 = appeared. Will appear if RIRI_MET (7) is >= 1
    TP1_TASTE_WISEMAN_DIAL   =  87 # Dialogue with Taste Wiseman in Temple level 1
    TP3_PET_DIALOGUE         =  88 # Dialogue with Word Wiseman pet in Temple level 3
    TP2_WORD_WISEMAN_DIAL    =  89 # Dialogue with Word Wiseman in Temple level 2
    FAC_FOREMAN_DIAL         =  90 # Dialogue with Foreman in Factory
    FAC_FAIL_FOREMAN_REACT   =  91 # Controls reaction of Foreman in case of failure in Factory
    STS_BEAN_IS_VISIBLE      =  92 # Store if bean is visible in Stairs street. Only control the animation of Woodruff shooting on can
    ADM_BUREAUCRAT_DIAL      =  93 # Dialogue of the bureaucrat in Administration center. Also depend on state of breath certificate and prison form (36 and 37)
    TER_STATUE_DIAL          =  94 # Dialogue with statue in Aristocrats Terrace
    TER_DOORMAN_DIAL         =  95 # Dialogue with doorman in Aristocrats Terrace
    TOB_FIRST_CALL           =  96 # Status call when using Tobozon the first time. 0 = need to play Azimuth video, 1 = already played
    CUI_BIRD_DIAL            =  97 # Dialogue with Jeff in Cui-cui store before using brush
    WALK_RAND_SOUND          =  98 # Seems to be a rand to play one walking sound or another
                                   # 99 -- Not used ?
    RLD_RAND_MACHINE         = 100 # Store a random number to determine output of money machine in Red Light District. 0 = loose, 1 = win
    RIRI_SAVED               = 101 # Indicate if Riri has been saved in the past. Will control his apparition in Slammer's dead end
    RLD_IS_DOOR_OPENED       = 102 # State of door to Slammer's dead end. 0 = blocked by car, 1 = open. Opens the fist time Woodruff enters Slammer's dead end
    CGR_CHAMPION_DIAL        = 103 # Dialogue with the champion in cage in Clandestine game room. Will also control animation when Woodruff drinks
    CGR_TAXMAN_STATE         = 104 # Controls apparition of taxman when playing in Clandestine game room. Starts at 0, increased by 1 each time we bet on black. Appears at 2, then stays at 4. Can only appear 1 time and while betting on black
    CGR_RAND_GAME            = 105 # Store a random number to determine output of game in Clandestine game room. 0 = win, 1 = loose
    CGR_NPC_LOOKED_AT        = 106 # Store which NPC Woodruff is looking at, to determine animations
    PST_STATE                = 107 # State of the past. 0 = not visited, 1 = visited, 2 = fish put into armor / can get in present, 3 = already got the stone fish
    PST_KEYRING_USED         = 108 # Indicate if keyring has been shown to the boozook in the past. Determine his dialogue
    TIT_ANIM                 = 109 # Indicate if animation in title has been played. 0 = no, 1 = yes.
    VTT_RAND_GAME            = 110 # Store a random number to determine winning cup. 0 = left, 1 = middle, 2 = right. Yes, you can cheat now :D
    VTT_INSIGHT_USED         = 111 # If insight formula has been used on trick player. 0 = no, 1 = yes
    VTT_TRIP_COUNT           = 112 # Indicate the number of paid virtual trips Woodruff can do.
    FAN_STATE                = 113 # Indicate fan state in Fan's platform. 0 = off / no fuel, 1 = off / fuel, 2 = on / ready to go to HMC, 3 = gone to HMC, ready to go to Aristocrats Terrace. Can only go to HMC once.
                                   # 114 -- Not used ?
                                   # 115 -- Not used ?
    TER_DOOR_CODE            = 116 # Door digicode in Aristocrats Terrace. 0 / 1 / 2 / 3 = number of good digits, -1 = deactivated (after successful code).
    SDE_PANORAMA_DIAL        = 117 # Dialogue when interacting with panorama in Slammer's dead end
    SDE_PRISON_ACCESS        = 118 # Indicate if Woodruff is trying to enter the prison. 0 = no, 1 = yes (after restoring wino memory). Unlock access to prison form after talking to jailer
    PST_HORN_USED            = 119 # If Woodruff have used the horn in the past
    HMC_BIRD_STATE           = 120 # Indicate if Jeff is here or not (similar to CUI_BIRD_STATE = 2)
    HMC_BIRD_DIAL            = 121 # Dialogue with Jeff in High Morals Club.
    HMC_PRES_QUART_VISUALS   = 122 # Indicate if president's quarters are open visually
    HMC_PRES_DIAL            = 123 # Dialogue with president of High Morals Club. Both before and after giving him the button (reset to 0 at this time)
    HMC_CENSORS_DIAL         = 124 # Dialogue with High Morals Censors
    SEC_COMPUTER_STATE       = 125 # State of computer in Sect. Requested action is : 0 = computer (turned off), 1 = coin, 2 = computer (need password), 3 = coin, 4 = high priest (give password), 5 = computer, 6 = coin, 7 / 8 = computer
                                   # 126 -- Something in sect
    SEC_SEQUENCE_CODE        = 127 # Sequence code in Sect (good sequence is BBSBSS). 0 / 1 / 2 / 3 / 4 / 5 = number of good hits, 6 = OK
    SEC_CEREMONY_STATE       = 128 # State of ceremony in Sect. 0 = beginning, 1 = one mantra done successfully, 2 = two mantras, 3 = three mantras, 4 = levitated
    SEC_FAILED_MANTRAS       = 129 # Number of times Woodruff has failed to use mantra. Max is 3.
    SEC_NEXT_SPEAKER         = 130 # Indicate who should speak next during sect sequence. 0 = first man, 3 = high priest, 7 = Woodruff
    WORD_WISEMAN_STATE       = 131 # Status of Word Wiseman. 0 = no dialogue / in temple level 2, 1 = spoken to in level 2 / in temple front yard, 2 = basic syllable given
    FCF_NEWSPAPER_STATE      = 132 # Controls the apparition of newspaper in Factory front yard. 0 = no here / coh cott not called, 1 = here, 2 = already pîcked up
    FCF_SAD_WOODRUFF         = 133 # Indicate if Woodruff is sad for newspaper sequence. 0 = normal, 1 = sad (can't interact with anything)
    FCF_SAD_WOODRUFF_STATE   = 134 # State of sad Woodruff sequence. 0 = beginning, 1 = on bench, 2 = clicked Woodruff one time, 3 = two times, 4 = three times, 5 = four times, 6 = clicked bell one time, 7 = clicked bell two times / end
    TP3_THRONE_ROOM_CODE     = 135 # Digicode of throne room door. 0 / 1 / 2 / 3 = number of good digits, -1 = deactivated (after successful code).
    TP3_WORD_WISEMAN_CODE    = 136 # Digicode of Word Wiseman door in temple level 3. 0 / 1 / 2 / 3 = number of good digits, -1 = deactivated (after successful code).
    TP2_COUNCIL_CODE         = 137 # Digicode of Council Chamber door in temple level 2. 0 / 1 / 2 / 3 = number of good digits, -1 = deactivated (after successful code).
    TP2_FERT_WISEMAN_CODE    = 138 # Digicode of Fertility Wiseman door in temple level 2. 0 / 1 / 2 / 3 = number of good digits
    TP2_FERT_WISEMAN_DIAL    = 139 # Dialogue with Fertility Wiseman's wife in temple level 2
    TP2_TALENT_WISEMAN_CODE  = 140 # Digicode of Talent Wiseman door in temple level 2. 0 / 1 / 2 / 3 = number of good digits
    TP2_TALENT_WISEMAN_DIAL  = 141 # Dialogue with Talent Wiseman's wife in temple level 2
    TP1_HEALTH_WISEMAN_CODE  = 142 # Digicode of Health Wiseman door in temple level 1. 0 / 1 / 2 / 3 = number of good digits, -1 = deactivated (after successful code).
    TP1_HEALTH_WISEMAN_ANIM  = 143 # Animation in Health Wiseman chamber to indicate he is in Virtual Trip Tower. 0 = not played, 1 = already played
    TP1_TASTE_WISEMAN_CODE   = 144 # Digicode of Taste Wiseman door in temple level 1. 0 / 1 / 2 / 3 = number of good digits
    ASY_WOODRUFF_STATE       = 145 # State of Woodruff in Asylum cell. From 0 to 5.
    HOH_NURSE_STATE          = 146 # State of nurse in Home of happiness. 0 = here, 1 = knocked out
    HOH_AUTIS_STATE          = 147 # State of autistic man in Home of happiness. 0 = base, 1 = happiness formula given
    HOH_CLOSET_OPEN          = 148 # Indicate if closet is open in Home of happiness (if screw has been putted in).
    VTT_SAFE_STATE           = 149 # Indicate state of safe in Virtual Trip Tower. 0 = base, 1 = meteorite given, 2 = fallen
    LAB_FERT_WISEMAN_STATE   = 150 # Fertility Wiseman state in Laboratory. 0 = base, 1 = syllable given, 2 = free
    LAB_FERT_WISEMAN_FREE    = 151 # Indicate if Fertility Wiseman is free in Laboratory
    COHCOTT_STATE            = 152 # Coh-cott state during "Eye" party. 0 = sick, 1 = looking for antidote, 2 = antidote ready, 3 = healed, 4 = end / at home. Also determine if Aristocrats terrace goes to Party or Coh-cott's quarters
    LAB_RAND_EXP             = 153 # Random (3) to determine Laboratory experiment output
    BGA_STORE_STATE          = 154 # State of store in Bigwig's area. 0 = base, 1 = want to buy glasses, 2 = glasses bought, 3 = want to buy chin, 4 = chin bought
    FCF_MANTRA_ACCESS        = 155 # Determine if Woodruff can access Mantra when talking to sect leader in Factory front yard. Change during "Eye" party. 0 = no, 1 = yes.
    THR_KING_DIAL            = 156 # Dialogue with the King in Throne room.
    WORD_WISEMAN_COUNCIL     = 157 # Indicate if Word Wiseman is present in Council Chamber
    TASTE_WISEMAN_COUNCIL    = 158 # Indicate if Taste Wiseman is present in Council Chamber
    FERT_WISEMAN_COUNCIL     = 159 # Indicate if Fertility Wiseman is present in Council Chamber
    HEALTH_WISEMAN_COUNCIL   = 160 # Indicate if Health Wiseman is present in Council Chamber
    STREN_WISEMAN_COUNCIL    = 161 # Indicate if Strength Wiseman is present in Council Chamber
    TALENT_WISEMAN_COUNCIL   = 162 # Indicate if Talent Wiseman is present in Council Chamber
    VTT_WISEMAN_ACCESS       = 163 # Determine if Health Wiseman can be saved in Virtual Trip Tower. 0 = no, 1 = yes.
    THR_CHEST_CODE           = 164 # Digicode of chest in Throne room. 0 / 1 / 2 / 3 = number of good digits, -1 = deactivated (after successful code).
                                   # 165 -- Used for meteo
    BGA_PORTRAIT_OPEN        = 166 # If Bigwig's portrait has been opened in Bigwig's area.
                                   # 167 -- Not used ?
    CNC_STATE                = 168 # Indicate the state of Council. 0 = base, 1 = after all wisemen discussion, 2 = schprotznog created
                                   # 169 -- Not used ?
                                   # 170 -- Not used ?
                                   # 171 -- Not used ?
                                   # 172 -- Not used ?
                                   # 173 -- Not used ?
                                   # 174 -- Not used ?
    FAC_HAT_TYPE             = 175 # Indicate hat type in Factory. Rand (10), hat is good if rand > 5. 1 = bad, 2 = good.
    FAC_BOX_NEW              = 176 # Indicate if there is a new bow on the ground. 0 = no (button clickable), 1 = yes
    FAC_GOOD_HAT_SENT        = 177 # Number of good hat sent in Factory. Determine if Woodruff can proceed to next sequence (Asylum)
    FAC_HAT_IN_INVENTORY     = 178 # Indicate if Woodruff has a hat in inventory. Block the action to get another and reset in case of failure or if Woodruff throw away his hat
    FAC_READY_TO_SEND        = 179 # Indicate that the box is ready to send (need to click on the node)
    FAC_HAT_WEARED           = 180 # If Woodruff tested the hat in front of mirror
    PLF_SCHNAP_STATE         = 181 # Schnaplure state in Place of the fountain. 0 = fountain empty, 1 = seed in fountain
                                   # 182 -- Not used ?
                                   # 183 -- Not used ?
    PLC_SCHNAP_TAKEN         = 184 # Indicate if Woodruff took the Schnaplure spice in Place of the fountain. 0 = no, 1 = yes
                                   # 185 -- Not used ?
    PRC_RUMMY_PLAY_STATE     = 186 # State of rummy in Prison courtyard. 0 = not playing, 1 = Woodruff playing, 2 = robot playing
                                   # 187 -- Not used ?
                                   # 188 -- Not used ?
    PRT_RIRI_STATE           = 189 # State of Riri in Prison Tower. 0 = not met, 1 = met
    PRT_WALL_OPEN            = 190 # Indicate if wall to Azimuth cell is opened in Prison tower.
                                   # 191 -- Not used ?
    PRC_PLAYING_RUMMY        = 192 # Indicate if Woodruff is playing rummy in Prison courtyard. 0 = no, 1 = yes
                                   # 193 - Not used ?
    BGQ_BIGWIG_STATE         = 194 # State of Bigwig in Bigwig's quarters. 0 = normal, 1 = trying to kill Woodruff, 2 = hypnotized
    BGQ_RIRI_ANIM            = 195 # Indicate if Riri animation has been played when interacting with force field. 0 = not played, 1 = already played
    BGQ_VIBLEFROTZER_USED    = 196 # If Viblefrotzer has been used on Bigwig
    BGQ_CHEWING_GUM_STATE    = 197 # Chewing-gum state in Bigwig's quarters. 0 = not present, 1 = on schprotznog
    BGQ_SCHPROTZNOG_USED     = 198 # Indicate if Schprotznog has been used
    BGQ_BOUZOUIOLI_COUNTDOWN = 199 # Countdown to use bouzouioli. Starts at 0, 3 = game over
    VTT_TRICK_PLAYER_DIAL    = 200 # Dialogue with trick player in Virtual Trip Tower.
    VTT_OWNER_DIAL_2         = 201 # Dialogue with Virtual Trip owner after destroying his safe
    PST_COMMANDER_DIAL       = 202 # Dialogue with commander in the past
    PST_BOOZOOK_DIAL         = 203 # Dialogue with dying boozook in the past
    PST_RIRI_DIAL_1          = 204 # Dialogue with Riri in the past (first boulder removed)
    PST_RIRI_DIAL_2          = 205 # Dialogue with Riri in the past (second boulder removed)
    TPF_GUARD_DIAL           = 206 # Dialogue with temple guard in Temple frontyard
    TPF_WORD_WISEMAN_DIAL    = 207 # Dialogue with Word Wiseman outside the temple
    TPF_BLUXTRE_NUT_GIVEN    = 208 # Indicate if Woodruff tried to give bluxtre nut (not pulp) to temple guard
    BGA_SLAVE_DIAL           = 209 # Dialogue with boozook slave in Bigwig's area
    RLD_WOMAN_DIAL           = 210 # Dialogue with woman in Red Light District
    RLD_FLIPPER_STATE        = 211 # State of flipper in Red Light District. 0 = not played, 1 = played one time, 2 = played two times
    FCF_LEADER_DIAL          = 212 # Dialogue with sect leader in Factory frontyard (before access to Mantra)
    FCF_GUARD_DIAL           = 213 # Dialogue with Factory guard
    SEC_INIT_CHAMBER_ANIM    = 214 # Indicate if "warning" animation has been played when trying to enter initiation chamber. 0 = not played, 1 = already played
    PLC_WORKER_DIAL          = 215 # Dialogue with worker in Place of the fountain.
    PLC_WISEMAN_DIAL         = 216 # Dialogue with Talent Wiseman in Place of the fountain
    PLC_WISEMAN_SUBDIAL_1    = 217 # Dialogue with Talent Wiseman in Place of the fountain (before entering his chamber)
    PLC_WISEMAN_SUBDIAL_2    = 218 # Dialogue with Talent Wiseman in Place of the fountain (after entering his chamber)
    PRC_GUARDS_DIAL          = 219 # Dialogue with guards in Prison courtyard (before playing rummy)
    PRC_ROBOT_DIAL           = 220 # Dialogue with robot in Prison courtyard
    PRC_RUMMY_COUNTDOWN      = 221 # Countdown to game over while playing rummy. Starts at 0, 4 = game over
    CNC_TIME_WISEMAN_DIAL_1  = 222 # Dialogue with Time Wiseman in Council Chamber before giving him the time syllable
    CNC_TIME_WISEMAN_SYLL    = 223 # Indicate if Woodruff gave the time syllable to Time Wiseman
    CNC_TIME_WISEMAN_DIAL_2  = 224 # Dialogue with Time Wiseman in Council Chamber after giving him the time syllable
    CNC_WORD_WISEMAN_DIAL    = 225 # Dialogue with Word Wiseman in Council Chamber before schprotnzog
    CNC_TALENT_WISEMAN_DIAL  = 226 # Dialogue with Talent Wiseman in Council Chamber before schprotnzog
    CNC_HEALTH_WISEMAN_DIAL  = 227 # Dialogue with Health Wiseman in Council Chamber before schprotnzog
    CNC_FERT_WISEMAN_DIAL    = 228 # Dialogue with Fertility Wiseman in Council Chamber before schprotnzog
    CNC_STREN_WISEMAN_DIAL   = 229 # Dialogue with Strength Wiseman in Council Chamber before schprotnzog
    CNC_TASTE_WISEMAN_DIAL   = 230 # Dialogue with Taste Wiseman in Council Chamber before schprotnzog
                                   # 231 - Not used ?
                                   # 232 - Not used ?
                                   # 233 - Not used ?
                                   # 234 - Not used ?
    VTT_OWNER_DIAL_1         = 235 # Dialogue with Virtual Trip owner before destroying his safe
                                   # 236 - Not used ?
                                   # 237 - Not used ?
                                   # 238 - Not used ?
                                   # 239 - Not used ?
                                   # 240 - Not used ?
                                   # 241 - Not used ?
                                   # 242 - Not used ?
                                   # 243 - Not used ?
                                   # 244 - Not used ?
                                   # 245 - Not used ?
                                   # 246 - Not used ?
                                   # 247 - Not used ?
                                   # 248 - Not used ?
                                   # 249 - Not used ?
    BGQ_BIGWIG_COUNTDOWN     = 250 # Countdown for the Bigwig to kill Woodruff. Starts at 0, 3 = game over
    BGQ_WOODRUFF_POSSESSED   = 251 # Indicate if Woodruff is possessed by the beast
                                   # 252 -- Use in Bigwigs's quarters
    BGQ_SCHPROTZNOG_HOOKED   = 253 # Indicate if Schprotznog has been hooked
    BGQ_BEAST_COUNTDOWN      = 254 # Countdown for the beast to kill Woodruff. Starts at 0, 4 = game over





#####################################
# LOCATIONS
# List of locations to detect in the game. They are mainly item pickups
# There are multiple detection methods for it :
# - FlagCheck : check that a Flag is between two values
# - InteractionCheck : check that we're currently interacting with an entity / hotspot
# - HotspotPositionCheck : check that hotspot is at a specified position (X / Y)
#
# A location is a combination of one or multiple checks, and can have multiple methods of detection
# Locations with specific Zone can will only be detected in this Zone. Locations with "None" are checked everywhere
#####################################

@dataclass(frozen=True)
class FlagCheck:
    flag: int  # Flag to check
    min: int   # Minimum value
    max: int  # Maximum value

@dataclass(frozen=True)
class InteractionCheck:
    entity: Entity  # Entity to check interaction with

@dataclass(frozen=True)
class HotspotPositionCheck:
    entity: Entity  # Entity to check position
    x: int  # Position X
    y: int  # Position Y

Check = FlagCheck | InteractionCheck | HotspotPositionCheck

@dataclass(frozen=True)
class Location:
    id: int # ID for Archipelago
    zone_key: str | None # Zone in which the location is
    name: str # Unique name
    checks: tuple[tuple[Check, ...], ...] # List of checks to do in memory to validate location



EMPTY_HANDS = FlagCheck(Flag.OBJECT_HELD, -1, -1)

LOCATIONS = [
    Location(1000, "AZI", "Item: Button", (
        ( HotspotPositionCheck(ENTITY_BY_NAME["AZI_Button"], 1000, 1000), ),
    )),
    # Location(1001, "BRI", "Item: Boot", (
    #     ( HotspotPositionCheck(ENTITY_BY_NAME["BRI_Boot"], 1000, 346), ),
    # )),
    Location(1003, "AZI", "Item: Azimuth photo", (
        ( FlagCheck(Flag.AZI_BOOT_TOP_PICKUP, 1, 4), FlagCheck(Flag.AZI_BOOT_BOT_PICKUP, 1, 4), ),
    )),
    # Location(1004, "BRI", "Item: Nut", (
    #     ( HotspotPositionCheck(ENTITY_BY_NAME["BRI_Nut"], 1000, 329), ),
    # )),
    Location(1005, None, "Item: Bluxtre nut", (
        ( FlagCheck(Flag.VTT_SAFE_STATE, 1, 2), ),
    )),
    Location(1006, None, "Item: Bluxtre pulp", (
        ( HotspotPositionCheck(ENTITY_BY_NAME["ADM_Bluxtre_Pulp"], 1000, 164), ),
        ( HotspotPositionCheck(ENTITY_BY_NAME["BRO_Bluxtre_Pulp"], 1000, 164), ),
        ( HotspotPositionCheck(ENTITY_BY_NAME["BGA_Bluxtre_Pulp"], 1000, 164), ),
    )),
    Location(1007, "TIT", "Item: Brush", (
        ( HotspotPositionCheck(ENTITY_BY_NAME["TIT_Brush"], 1000, 1000), ),
    )),
    Location(1009, "WNO", "Item: Feathers", (
        ( InteractionCheck(ENTITY_BY_NAME["WNO_Feathers"]), EMPTY_HANDS, ),
    )),
    Location(1010, "BAR", "Item: Coffee", (
        ( InteractionCheck(ENTITY_BY_NAME["BAR_Coffee"]), EMPTY_HANDS, ),
        ( InteractionCheck(ENTITY_BY_NAME["BAR_JF_Sebastien"]), EMPTY_HANDS, ),
    )),
    Location(1011, "BRO", "Item: Identity photo", (
        ( FlagCheck(Flag.HAS_PHOTO_0, 1, 1), ),
        ( FlagCheck(Flag.HAS_PHOTO_1, 2, 2), ),
        ( FlagCheck(Flag.HAS_PHOTO_2, 3, 3), ),
        ( FlagCheck(Flag.HAS_PHOTO_3, 4, 4), ),
        ( FlagCheck(Flag.HAS_PHOTO_4, 5, 5), ),
        ( FlagCheck(Flag.HAS_PHOTO_5, 8, 8), ),
        ( FlagCheck(Flag.HAS_PHOTO_6, 6, 6), ),
    )),
    Location(1012, "WNO", "Item: Weather watch", (
        ( FlagCheck(Flag.WNO_WINO_STATE, 1, 3), ),
    )),
    Location(1014, "WNO", "Item: Rummy rules", (
        ( FlagCheck(Flag.WNO_WINO_STATE, 3, 3), ),
    )),
    Location(1015, "STS", "Item: Bean", (
        ( HotspotPositionCheck(ENTITY_BY_NAME["STS_Bean"], 1000, 100), ),
    )),
    Location(1016, "STS", "Item: Can", (
        ( HotspotPositionCheck(ENTITY_BY_NAME["STS_Can"], 1000, 100), ),
    )),
    Location(1017, "STS", "Item: Kite", (
        ( HotspotPositionCheck(ENTITY_BY_NAME["STS_Window"], 1000, 100), ),
    )),
    Location(1018, "STS", "Item: Morphoplastoc eye", (
        ( HotspotPositionCheck(ENTITY_BY_NAME["STS_Morphoplastoc_Eye"], 1000, 100), ),
    )),
    Location(1019, "BAR", "Item: \"A\" stone", (
        ( FlagCheck(Flag.BAR_OWNER_DIAL, 4, 6), ),
    )),
    Location(1020, "BAR", "Item: Azimuth article", (
        ( InteractionCheck(ENTITY_BY_NAME["SAD_Woman"]), FlagCheck(Flag.OBJECT_HELD, ITEM_BY_NAME["Azimuth photo"].id, ITEM_BY_NAME["Azimuth photo"].id), ),
        # TODO : Can be missed
    )),
    Location(1021, "SAD", "Item: Tobozon", (
        ( HotspotPositionCheck(ENTITY_BY_NAME["SAD_Rock"], 1000, 10), ),
    )),
    Location(1022, "ADM", "Item: Breath certificate", (
        ( FlagCheck(Flag.ADM_BREATH_CERTIF_ACCESS, 2, 2), ),
    )),
    Location(1023, "ADM", "Item: Prison form", (
        ( FlagCheck(Flag.ADM_PRISON_FORM_ACCESS, 2, 2), ),
    )),
    Location(1024, "BRO", "Item: Morphoplastoc finger", (
        ( HotspotPositionCheck(ENTITY_BY_NAME["BRO_Morphoplastoc_Finger"], 1000, 44), ),
    )),
    Location(1025, "BGA", "Item: Shirt", (
        ( HotspotPositionCheck(ENTITY_BY_NAME["BGA_Shirt"], 1000, 1000), ),
    )),
    Location(1026, "BGA", "Item: Glasses", (
        ( FlagCheck(Flag.BGA_STORE_STATE, 2, 4), ),
    )),
    Location(1027, "BGA", "Item: Morphoplastoc chin", (
        ( FlagCheck(Flag.BGA_STORE_STATE, 4, 4), ),
    )),
    Location(1028, "PLC", "Item: Hat", (
        ( InteractionCheck(ENTITY_BY_NAME["PLF_Talent_Wiseman"]), FlagCheck(Flag.OBJECT_HELD, ITEM_BY_NAME["Struls"].id, ITEM_BY_NAME["Struls"].id), FlagCheck(Flag.STRULS, 2, 255), ),
        ( FlagCheck(Flag.TALENT_WISEMAN_COUNCIL, 1, 1), ), # Fallback in case of Wiseman not here
        # TODO : Add hat pickup in factory
    )),
    Location(1030, "THR", "Item: Chewing-gum", (
        ( HotspotPositionCheck(ENTITY_BY_NAME["THR_Chewing_Gum"], 1000, 1000), ),
    )),
    Location(1031, "RLD", "Item: Struls", (
        ( HotspotPositionCheck(ENTITY_BY_NAME["RLD_Strul"], 1000, 1000), ),
    )),
    Location(1032, None, "Item: Meteorite", (
        ( InteractionCheck(ENTITY_BY_NAME["ADM_Meteorite"]), EMPTY_HANDS, ),
        ( InteractionCheck(ENTITY_BY_NAME["BRO_Meteorite"]), EMPTY_HANDS, ),
        ( InteractionCheck(ENTITY_BY_NAME["BGA_Meteorite"]), EMPTY_HANDS, ),
    )),
    Location(1033, "MEM", "Item: Stone fish", (
        ( HotspotPositionCheck(ENTITY_BY_NAME["MEM_Armor"], 1000, 1000), FlagCheck(Flag.PST_STATE, 2, 3), ),
    )),
    Location(1034, "THR", "Item: Keyring", (
        ( InteractionCheck(ENTITY_BY_NAME["THR_King"]), FlagCheck(Flag.OBJECT_HELD, ITEM_BY_NAME["Bottle opener"].id, ITEM_BY_NAME["Bottle opener"].id), ),
        # TODO : Can be missed
    )),
    Location(1035, "TP1", "Item: Gasoline", (
        ( HotspotPositionCheck(ENTITY_BY_NAME["TP1_Gasoline"], 1000, 1000), ),
    )),
    Location(1036, "SDE", "Item: Stone arm", (
        ( HotspotPositionCheck(ENTITY_BY_NAME["SDE_Stone_Arm"], 1000, 1000), FlagCheck(Flag.RIRI_SAVED, 1, 2), ),
    )),
    Location(1037, "PRT", "Item: Grabber", (
        ( HotspotPositionCheck(ENTITY_BY_NAME["PRT_Rope"], 1000, 1000), ),
    )),
    Location(1038, "LAB", "Item: Schnaplure seed", (
        ( HotspotPositionCheck(ENTITY_BY_NAME["LAB_Schnaplure_Seed"], 1000, 1000), ),
    )),
    Location(1039, "PLC", "Item: Schnaplure spice", (
        ( FlagCheck(Flag.PLC_SCHNAP_TAKEN, 1, 1), ),
    )),
    Location(1040, "LAB", "Item: Antidote", (
        ( InteractionCheck(ENTITY_BY_NAME["LAB_Tubes_1"]), FlagCheck(Flag.COHCOTT_STATE, 1, 4), EMPTY_HANDS, ),
        ( InteractionCheck(ENTITY_BY_NAME["LAB_Tubes_2"]), FlagCheck(Flag.COHCOTT_STATE, 1, 4), EMPTY_HANDS, ),
    )),
    Location(1041, "TP1", "Item: Lid", (
        ( HotspotPositionCheck(ENTITY_BY_NAME["TP1_Lid"], 1000, 1000), ),
    )),
    Location(1042, "PST", "Item: Trident", (
        ( HotspotPositionCheck(ENTITY_BY_NAME["PST_Trident"], 1000, 1000), ),
    )),
    Location(1043, "PST", "Item: Red fish", (
        ( HotspotPositionCheck(ENTITY_BY_NAME["PST_Helmet"], 1000, 1000), ),
    )),
    Location(1044, "PST", "Item: Horn", (
        ( FlagCheck(Flag.PST_KEYRING_USED, 1, 1), ),
    )),
    Location(1045, "SEC", "Item: Hypnotic ceedeerom", (
        ( HotspotPositionCheck(ENTITY_BY_NAME["SEC_Ceedeerom"], 1000, 1000), ),
    )),
    Location(1048, "PRC", "Item: Rag", (
        ( HotspotPositionCheck(ENTITY_BY_NAME["PRC_Rag"], 1000, 1000), ),
    )),
    Location(1049, None, "Item: Employment certificate", (
        ( FlagCheck(Flag.HAS_SENT_GOOD_PHOTO, 1, 1), FlagCheck(Flag.HAS_SENT_CERTIF, 1, 1), ),
    )),
    Location(1050, "PST", "Item: Corn ear", (
        ( HotspotPositionCheck(ENTITY_BY_NAME["PST_Corn_Ear"], 1000, 1000), ),
    )),
    Location(1051, "BGA", "Item: Trash bag", (
        ( HotspotPositionCheck(ENTITY_BY_NAME["BGA_Stain"], 1000, 1000), HotspotPositionCheck(ENTITY_BY_NAME["BGA_Tash_Bag"], 1000, 1000), ),
    )),
    Location(1052, "BAR", "Item: Bottle opener", (
        ( HotspotPositionCheck(ENTITY_BY_NAME["BAR_Barman_Pocket"], 1000, 76), ),
    )),
    Location(1053, "SGE", "Item: Transportozon", (
        (HotspotPositionCheck(ENTITY_BY_NAME["SDE_Fish_Imprint"], 1000, 1000), ),
    )),
    Location(1055, "THR", "Item: Boozook formulas", (
        ( HotspotPositionCheck(ENTITY_BY_NAME["THR_Boozook_Formulas"], 1000, 1000), ),
    )),
    Location(1057, "CEL", "Item: Viblefrotzer", (
        ( FlagCheck(Flag.CEL_AZIMUTH_DIAL, 1, 5), ),
    )),
    Location(1058, "CNC", "Item: Schprotznog", (
        ( FlagCheck(Flag.CNC_STATE, 2, 2), ),
    )),
    Location(1060, "BRO", "Item: Useless photo", (
        ( FlagCheck(Flag.HAS_PHOTO_1, 2, 2), ),
        ( FlagCheck(Flag.HAS_PHOTO_2, 3, 3), ),
        ( FlagCheck(Flag.HAS_PHOTO_3, 4, 4), ),
        ( FlagCheck(Flag.HAS_PHOTO_4, 5, 5), ),
        ( FlagCheck(Flag.HAS_PHOTO_5, 8, 8), ),
        ( FlagCheck(Flag.HAS_PHOTO_6, 6, 6), ),
    )),
    Location(1061, "BRO", "Item: Rotten photo", (
        ( FlagCheck(Flag.HAS_PHOTO_2, 3, 3), ),
        ( FlagCheck(Flag.HAS_PHOTO_3, 4, 4), ),
        ( FlagCheck(Flag.HAS_PHOTO_4, 5, 5), ),
        ( FlagCheck(Flag.HAS_PHOTO_5, 8, 8), ),
        ( FlagCheck(Flag.HAS_PHOTO_6, 6, 6), ),
    )),
    Location(1062, "BRO", "Item: Mediocre photo", (
        ( FlagCheck(Flag.HAS_PHOTO_3, 4, 4), ),
        ( FlagCheck(Flag.HAS_PHOTO_4, 5, 5), ),
        ( FlagCheck(Flag.HAS_PHOTO_5, 8, 8), ),
        ( FlagCheck(Flag.HAS_PHOTO_6, 6, 6), ),
    )),
    Location(1063, "BRO", "Item: Passable photo", (
        ( FlagCheck(Flag.HAS_PHOTO_4, 5, 5), ),
        ( FlagCheck(Flag.HAS_PHOTO_5, 8, 8), ),
        ( FlagCheck(Flag.HAS_PHOTO_6, 6, 6), ),
    )),
    Location(1064, "BRO", "Item: Average photo", (
        ( FlagCheck(Flag.HAS_PHOTO_5, 8, 8), ),
        ( FlagCheck(Flag.HAS_PHOTO_6, 6, 6), ),
    )),
    Location(1065, "BRO", "Item: Perfect photo", (
        ( FlagCheck(Flag.HAS_PHOTO_6, 6, 6), ),
    )),
    Location(1066, "FCF", "Item: Mantra", (
        ( FlagCheck(Flag.FCF_LEADER_DIAL, 3, 3), ),
    )),
    Location(1068, "SDE", "Item: Shell", (
        ( HotspotPositionCheck(ENTITY_BY_NAME["SDE_Shell"], 1000, 1000), FlagCheck(Flag.RIRI_SAVED, 1, 2), ),
    )),
    Location(1069, "HMC", "Item: Cartoon videotape", (
        ( HotspotPositionCheck(ENTITY_BY_NAME["HMC_Magnetoscopon"], 582, 68), HotspotPositionCheck(ENTITY_BY_NAME["HMC_Cartoon_Videotape"], 1000, 1000), ),
    )),
    Location(1070, "HMC", "Item: Diva videotape", (
        ( HotspotPositionCheck(ENTITY_BY_NAME["HMC_Magnetoscopon"], 582, 68), HotspotPositionCheck(ENTITY_BY_NAME["HMC_Diva_Videotape"], 1000, 1000), ),
    )),
    Location(1071, "HMC", "Item: Circus videotape", (
        ( HotspotPositionCheck(ENTITY_BY_NAME["HMC_Magnetoscopon"], 582, 68), HotspotPositionCheck(ENTITY_BY_NAME["HMC_Circus_Videotape"], 1000, 1000), ),
    )),
    Location(1072, "BGQ", "Item: Magnetic card", (
        ( HotspotPositionCheck(ENTITY_BY_NAME["BGQ_Clothes"], 1000, 1000), FlagCheck(Flag.BGQ_VIBLEFROTZER_USED, 1, 1), ),
    )),
    Location(1073, "TP1", "Item: Bouzouioli", (
        ( FlagCheck(Flag.TASTE_WISEMAN_COUNCIL, 1, 1), ),
    )),

    # TODO : For formulas, need an additional detection method. Maybe using var16_20312 to var16_20318

    Location(1087, "THR", "Item: Leading syllable", (
        ( FlagCheck(Flag.THR_KING_DIAL, 1, 4), ),
    )),
    Location(1088, "CNC", "Item: Advice syllable", (
        ( FlagCheck(Flag.CNC_TIME_WISEMAN_DIAL_2, 1, 2), ),
    )),
    Location(1089, "TP3", "Item: Basic syllable", (
        ( FlagCheck(Flag.TP3_WORD_WISEMAN_CODE, -1, -1), HotspotPositionCheck(ENTITY_BY_NAME["TP3_Pet"], 1000, 1000), ),
    )),
    Location(1090, "CUI", "Item: Time syllable", (
        ( InteractionCheck(ENTITY_BY_NAME["CUI_Water_Reservoir"]), FlagCheck(Flag.OBJECT_HELD, ITEM_BY_NAME["Water hat"].id, ITEM_BY_NAME["Water hat"].id), FlagCheck(Flag.CUI_CHEWING_GUM_STATE, 1, 1), ),
    )),
    Location(1091, "HOH", "Item: Green syllable", (
        ( FlagCheck(Flag.HOH_AUTIS_STATE, 1, 1), ),
    )),
    Location(1092, "HMC", "Item: Artistic syllable", (
        ( InteractionCheck(ENTITY_BY_NAME["HMC_Magnetoscopon"]), FlagCheck(Flag.OBJECT_HELD, ITEM_BY_NAME["Diva videotape"].id, ITEM_BY_NAME["Diva videotape"].id), ),
        # TODO : Can be missed
    )),
    Location(1093, "VTT", "Item: Healing syllable", (
        ( FlagCheck(Flag.HEALTH_WISEMAN_COUNCIL, 1, 1), ),
    )),
    Location(1094, "TER", "Item: Intuitive syllable", (
        ( HotspotPositionCheck(ENTITY_BY_NAME["TER_Spiral_Imprint"], 1000, 1000), ),
    )),
    Location(1095, "THR", "Item: Energy syllable", (
        ( FlagCheck(Flag.THR_CHEST_CODE, -1, -1), ),
    )),
    Location(1100, "THR", "Item: Auricular control", (
        ( FlagCheck(Flag.RIRI_MET, 1, 2),),
    )),
    Location(1101, "WNO", "Item: Hair control", (
        ( HotspotPositionCheck(ENTITY_BY_NAME["WNO_Riri"], 1000, 1000), ),
    )),
    Location(1102, "PLF", "Item: Ocular control", (
        ( InteractionCheck(ENTITY_BY_NAME["PLF_Public_Tobozon"]), FlagCheck(Flag.RIRI_MET, 1, 2), EMPTY_HANDS, ),
    )),
    Location(1103, "ADM", "Item: Nasal control", (
        ( InteractionCheck(ENTITY_BY_NAME["ADM_Tag"]), FlagCheck(Flag.RIRI_MET, 1, 2), EMPTY_HANDS, ),
    )),
    Location(1104, "PRT", "Item: Facial control", (
        ( FlagCheck(Flag.PRT_RIRI_STATE, 1, 1), ),
    )),

    # TODO : For levitation, need an additional detection method as well. Or maybe send it based on if other Riri locations has been sent ?


    Location(2000, "BAR", "Reading skill", (
        ( FlagCheck(Flag.BAR_OWNER_DIAL, 6, 6), ),
    )),

]


