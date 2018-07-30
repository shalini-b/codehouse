import json

facts = [
    {
        'name': 'animal',
        'children': [
            {
                'name': 'A snail can sleep for three years'
            },
            {
                'name': 'Slugs have four noses'
            },
            {
                'name': 'A rhinoceros\' horn is made of hair'
            }
        ]
    },
    {
        'name': 'mammal',
        'children': [
            {
                'name': 'The human brain is over three times as big as the brain of other mammals that are of similar body size.'
            },
            {
                'name': 'All mammals have hair, even dolphins and whales that live in the ocean'
            },
            {
                'name': 'Koalas sleep the longest of any animal. They sleep 22 hours a day'
            },
            {
                'name': 'Bats are the only mammals that can fly.'
            }
        ]
    },
    {
        'name': 'water',
        'children': [
            {
                'name': 'There is the same amount of water on Earth as there was when the Earth was formed'
            },
            {
                'name': 'Somewhere between 70 and 75 percent of the earth\'s surface is covered with water.'
            },
            {
                'name': 'An ice cube takes up about 9% more volume than the water used to make it.'
            },
            {
                'name': 'Unlike many substances, water expands as it freezes'
            }
        ]
    },
    {
        'name': 'dog',
        'children': [
            {
                'name': 'If your dog’s acting funny, get out the umbrella! Stormy weather is on the way'
            },
            {
                'name': 'Watch that plate of cookies! A Dog’s sense of smell is 10,000 – 100,000 times stronger'
            },
            {
                'name': 'Dalmatian puppies are pure white when they are born and develop their spots as they grow older'
            },
            {
                'name': 'The twitching and paw movements that occur during their sleep are signs that your dog is dreaming'
            }
        ]
    },
    {
        'name': 'bird',
        'children': [
            {
                'name': 'Ostriches have the largest eyes of any land animal'
            },
            {
                'name': 'Most hummingbirds weigh less than a nickel.'
            }
        ]
    },
    {
        'name': 'cat',
        'children': [
            {
                'name': 'Cats knead with their paws when they are happy.'
            },
            {
                'name': 'A cat can jump approximately seven times its height'
            }
        ]
    },
    {
        'name': 'standing',
        'children': [
            {
                'name': 'Standing the majority of the day has been said to increase concentration'
            },
            {
                'name': 'Standing for most of the day has the potential to burn 30,000 more calories in a year'
            }
        ]
    },
    {
        'name': 'food',
        'children': [
            {
                'name': 'Arachibutyrophobia is the fear of peanut butter sticking to the roof of your mouth.'
            },
            {
                'name': 'The tea bag was created by accident, as tea bags were originally sent as samples.'
            }
        ]
    },
    {
        'name': 'flower',
        'children': [
            {
                'name': 'Sunflowers move throughout the day in response to the movement of the sun from east to west.'
            },
            {
                'name': 'Moon flowers bloom only at night, closing during the day.'
            },
            {
                'name': 'The juice from bluebell flowers was used historically to make glue.'
            }
        ]
    },
    {
        'name': 'person',
        'children': [
            {
                'name': 'Astronauts can grow up to two inches taller in space.'
            },
            {
                'name': 'When listening to music, your heartbeat will sync with the rhythm.'
            },
            {
                'name': 'Gravity changes how much the person weighs on a planet.'
            }
        ]
    },
    {
        'name': 'computer',
        'children': [
            {
                'name': 'Your brain is more powerful, more complex and more clever than any computer ever built'
            },
            {
                'name': 'The first actual computer “bug” was a dead moth which was stuck in a computer.'
            },
            {
                'name': 'The first computer of the world, the ENIAC, weighed around 27 tonnes and occupied an entire hall'
            },
            {
                'name': 'Only about 10% of the world’s currency is physical money, the rest only exists on computers'
            }
        ]
    },
    {
        'name': 'ball',
        'children': [
            {
                'name': 'Football, the most played and most watched sport on earth originated in China'
            },
            {
                'name': 'The very first game of basketball was played with a soccer ball'
            }
        ]
    },
    {
        'name': 'smiling',
        'children': [
            {
                'name': 'It\'s easier to smile than frown.'
            },
            {
                'name': 'Smiling can reduce blood pressure.'
            }
        ]
    },
    {
        'name': 'earth',
        'children': [
            {
                'name': '97% of water on Earth is salty and not usable. 2% is frozen. That leaves us with just 1% of usable water!'
            },
            {
                'name': 'As Earth spins, gravity points toward the center of our planet, and a centrifugal force pushes outward'
            }
        ]
    },
    {
        'name': 'sun',
        'children': [
            {
                'name': 'The Sun contains 99.86 percent of the Solar System\'s known mass, with Jupiter and Saturn making up making up most of the rest.'
            },
            {
                'name': 'The energy created by the Sun\’s core is nuclear fusion'
            }
        ]
    },
    {
        'name': 'periodic_table',
        'children': [
            {
                'name': 'The only letter that doesn’t appear on the periodic table is J.'
            }
        ]
    },
    {
        'name': 'mathematics',
        'children': [
            {
                'name': 'The Fibonacci sequence is encoded in the number 1/89'
            },
            {
                'name': 'If you shuffle a pack of cards properly, chances are that exact order has never been seen before in the whole history of the universe'
            },
            {
                'name': 'The spiral shapes of sunflowers follow a Fibonacci sequence'
            },
            {
                'name': 'Zero is the only number that can\'t be represented in Roman numerals'
            }
        ]
    },
    {
        'name': 'book',
        'children': [
            {
                'name': 'Love the smell of books? Bibliosmia is what this passion is known as.'
            },
            {
                'name': 'The Term “Bookworm” came from insects who would feast on the binding of books'
            }
        ]
    },
]

files = [
    {
        "name": "animal_facts.jpeg",
        "children": [
            "outdoor",
            "animal",
            "mammal",
            "water",
            "sitting",
            "standing",
            "looking",
            "brown",
            "small",
            "large",
            "dirt",
            "dog",
            "bird",
            "dirty",
            "cat",
            "field"
        ],
        "image_caption": "A close up of an animal"
    },
    {
        "name": "birds.jpeg",
        "children": [
            "bird",
            "sitting",
            "small",
            "green",
            "colorful",
            "little",
            "branch",
            "black",
            "table",
            "perched",
            "standing",
            "yellow",
            "food",
            "wooden",
            "red",
            "white",
            "blue",
            "flower",
            "group"
        ],
        "image_caption": "A small bird sitting on a branch"
    },
    {
        "name": "chemistry.jpeg",
        "children": [
            "drawing",
            "chemistry",
            "experiments",
            "water",
            "periodic_table"
        ],
        "image_caption": "A drawing of a face"
    },
    {
        "name": "laptop.jpeg",
        "children": [
            "laptop",
            "person",
            "computer",
            "sitting",
            "man",
            "front",
            "using",
            "table",
            "woman",
            "holding",
            "young",
            "bed"
        ],
        "image_caption": "A person using a laptop computer"
    },
    {
        "name": "mathkid.jpg",
        "children": [
            "text",
            "kid",
            "mathematics",
            "book"
        ],
        "image_caption": "A close up of text on a white background"
    },
    {
        "name": "rocket.jpg",
        "children": [
            "person",
            "boy",
            "young",
            "child",
            "holding",
            "playing",
            "little",
            "man",
            "table",
            "front",
            "small",
            "bat",
            "standing",
            "yellow",
            "smiling",
            "wearing",
            "swinging",
            "ball",
            "computer",
            "game",
            "baseball",
            "player",
            "sign",
            "white"
        ],
        "image_caption": "A young boy holding a sign"
    },
    {
        "name": "solar.jpeg",
        "children": [
            "table",
            "sitting",
            "group",
            "earth",
            "sun"
        ],
        "image_caption": "A group of objects on a table"
    },
    {
        "name": "web.jpeg",
        "children": [
            "cat",
            "indoor",
            "lying",
            "laying",
            "watching",
            "computer",
            "kitchen",
            "woman",
            "table",
            "man",
            "standing",
            "dog",
            "room",
            "holding",
            "living",
            "bed"
        ],
        "image_caption": "A person holding a cat"
    }
]

fact_dict = {}
for fact in facts:
    tag = fact['name']
    fact_list = fact['children']
    fact_dict.update({tag: fact_list})


for _file in files:
    file_name = _file['name'].split('.')[0]
    pic_tags = set(_file['children']).intersection(fact_dict)
    json_body = {
        'name': 'image',
        'children': [],
        'image_caption': _file['image_caption']
    }
    tag_info = json_body['children']
    for _tag in pic_tags:
        tag_info.append(
            {
                'name': _tag,
                'children': fact_dict[_tag]
            }
        )

    with open("{}.json".format(file_name), "w") as fp:
        json.dump(json_body, fp, indent=4)
