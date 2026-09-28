print()
print("=" * 70)
print("                    SURVIVING THE MALL")
print("=" * 70)
print()
print("A Choose-Your-Own-Adventure Shopping Expedition")
print()
print("You have entered a realm of bright lights, crowded hallways,")
print("suspicious food-court samples, pushy salespeople,")
print("determined customers, and extremely specific ferret supplies.")
print()
print("Your mission sounds simple:")
print()
print("  1. Buy ferret food.")
print("  2. Buy boxing gloves for your ferret.")
print("  3. Make it back to the parking lot.")
print()
print("Unfortunately, nothing at this mall is ever simple.")
print("=" * 70)
print()


player_name = input("What is your name, brave shopper? ").strip()

if player_name == "":
    player_name = "Mysterious Shopper"

ferret_name = input("What is the name of your ferret? ").strip()

if ferret_name == "":
    ferret_name = "Sir Nibbles"

print()
print("Welcome,", player_name + "!")
print(ferret_name, "the ferret is waiting at home.")
print()
print(ferret_name, "has left you a shopping list written in crayon.")
print("You are not certain how a ferret learned to write.")
print("You are even less certain where the ferret found a crayon.")
print()


money = 100
energy = 10
patience = 10
ferret_happiness = 5
mall_reputation = 0

has_ferret_food = False
has_boxing_gloves = False
has_mall_map = False
has_coupon = False
has_snack = False
has_sunglasses = False
has_emergency_pretzel = False

inventory = []
shopping_list = [
    "Ferret food",
    "Ferret-sized boxing gloves"
]

visited_stores = []
completed_objectives = 0
game_running = True
turn_number = 1


def wait_for_player_to_continue():
    input("\nPress Enter to continue...")


def print_section_divider():
    print()
    print("-" * 70)
    print()


def display_current_shopping_status():
    print_section_divider()
    print("CURRENT SHOPPING STATUS")
    print()
    print("Shopper:", player_name)
    print("Ferret:", ferret_name)
    print("Money: $" + str(money))
    print("Energy:", energy)
    print("Patience:", patience)
    print("Ferret happiness:", ferret_happiness)
    print("Mall reputation:", mall_reputation)

    print()
    print("Inventory:")

    if len(inventory) == 0:
        print("  Your shopping bag is empty.")
    else:
        for item in inventory:
            print("  -", item)

    print()
    print("Objectives:")

    if has_ferret_food:
        print("  [COMPLETE] Buy ferret food")
    else:
        print("  [INCOMPLETE] Buy ferret food")

    if has_boxing_gloves:
        print("  [COMPLETE] Buy boxing gloves for", ferret_name)
    else:
        print("  [INCOMPLETE] Buy boxing gloves for", ferret_name)

    print_section_divider()


def display_mall_directory():
    print_section_divider()
    print("MALL DIRECTORY")
    print()
    print("1. Pet store")
    print("   Ferret food, pet toys, and animals judging your decisions.")
    print()
    print("2. Sporting goods store")
    print("   Boxing gloves, exercise equipment, and competitive employees.")
    print()
    print("3. Food court")
    print("   Pretzels, pizza, mysterious samples, and crowded tables.")
    print()
    print("4. Sunglasses kiosk")
    print("   Stylish eyewear and a dangerously persuasive salesperson.")
    print()
    print("5. Customer service")
    print("   Mall maps, lost objects, coupons, and administrative mysteries.")
    print()
    print("6. Department store")
    print("   Clothing racks, perfume clouds, and wandering shoppers.")
    print()
    print("7. Check your status")
    print()
    print("8. Attempt to leave the mall")
    print_section_divider()


def end_game_if_player_resources_are_depleted():
    global game_running

    if energy <= 0:
        print()
        print("Your energy has reached zero.")
        print()
        print("You sit down on a decorative bench beside a plastic tree.")
        print("You tell yourself that you are only resting for one minute.")
        print()
        print("Three hours later, a security guard wakes you.")
        print("The mall is closing.")
        print()
        print("You have survived, but the shopping mission has failed.")
        game_running = False

    elif patience <= 0:
        print()
        print("Your patience has reached zero.")
        print()
        print("The next person who says, 'Can I interest you in a free sample?'")
        print("causes you to abandon your shopping cart and walk directly outside.")
        print()
        print("You have escaped the mall, but the mission has failed.")
        game_running = False

    elif money < 0:
        print()
        print("Your money has dropped below zero.")
        print()
        print("The laws of mathematics have started breaking down.")
        print("A mall accountant appears from behind a decorative fountain.")
        print()
        print("'We need to discuss your budget,' the accountant says.")
        print()
        print("Your adventure ends in a small office full of spreadsheets.")
        game_running = False


def visit_pet_store():
    global money
    global energy
    global patience
    global ferret_happiness
    global mall_reputation
    global has_ferret_food
    global has_coupon

    print_section_divider()
    print("THE PET STORE")
    print()
    print("A bell jingles as you enter the pet store.")
    print()
    print("To your left, a parrot is shouting:")
    print()
    print('"BUY THE EXPENSIVE BAG! BUY THE EXPENSIVE BAG!"')
    print()
    print("To your right, three hamsters stare at you as if they")
    print("know your complete Internet search history.")
    print()
    print("At the back of the store, you see the ferret-food aisle.")
    print("Unfortunately, another customer is blocking the entire aisle")
    print("with a shopping cart parked sideways.")
    print()
    print("The customer is loudly arguing with an employee.")
    print()
    print('"I need to speak to the manager," the customer says.')
    print('"This bag says it contains twelve servings, but my pet iguana')
    print('says it only contains eleven!"')
    print()
    print("You have encountered KAREN OF THE PET AISLE.")
    print()
    print("What do you do?")
    print()
    print("1. Politely ask Karen to move the cart.")
    print("2. Attempt to squeeze past the cart.")
    print("3. Pretend to be the store manager.")
    print("4. Distract Karen by pointing at the shouting parrot.")
    print("5. Leave the store.")

    choice = input("\nChoose 1, 2, 3, 4, or 5: ").strip()

    if choice == "1":
        print()
        print("You take a calm breath.")
        print()
        print('"Excuse me," you say. "Could I please get through?"')
        print()
        print("Karen slowly turns toward you.")
        print()
        print('"I was here first," she says.')
        print()
        print("You point out that standing in an aisle is not a formal")
        print("reservation system.")
        print()
        print("The employee tries not to laugh.")
        print("Karen moves the cart two whole inches.")
        print()
        print("It is not much, but it is enough.")
        patience -= 1
        mall_reputation += 1

    elif choice == "2":
        print()
        print("You turn sideways and attempt to squeeze past the cart.")
        print()
        print("Halfway through, your jacket catches on a display of")
        print("squeaky rubber chickens.")
        print()
        print("Thirty rubber chickens fall to the floor.")
        print()
        print("SQUEAK!")
        print("SQUEAK!")
        print("SQUEAK!")
        print()
        print("The entire store becomes silent.")
        print()
        print("Even the parrot looks embarrassed for you.")
        energy -= 1
        mall_reputation -= 1

    elif choice == "3":
        print()
        print("You straighten your posture and put on your most")
        print("administrative facial expression.")
        print()
        print('"I am the regional assistant manager of aisle access," you say.')
        print()
        print("Karen looks suspicious.")
        print()
        print('"That sounds like a fake job," she says.')
        print()
        print('"It is a very new department," you reply.')
        print()
        print("The employee nods seriously.")
        print()
        print('"Very new," the employee agrees.')
        print()
        print("Karen moves the cart.")
        mall_reputation += 2
        patience += 1

    elif choice == "4":
        print()
        print("You point dramatically across the store.")
        print()
        print('"Was that parrot asking to speak to the manager?" you shout.')
        print()
        print("Karen turns around immediately.")
        print()
        print("The parrot sees its opportunity.")
        print()
        print('"I WANT A REFUND!" the parrot screams.')
        print()
        print("Karen marches toward the bird.")
        print()
        print("The aisle is now open.")
        mall_reputation += 1
        ferret_happiness += 1

    elif choice == "5":
        print()
        print("You decide that today is not the day to challenge Karen.")
        print("You leave the pet store.")
        patience -= 1
        return

    else:
        print()
        print("You hesitate for too long.")
        print("Karen continues arguing.")
        print("Eventually, an employee carefully moves the cart.")
        patience -= 2

    print()
    print("You reach the ferret-food shelf.")
    print()
    print("There are three choices:")
    print()
    print("1. Budget Ferret Nuggets: $15")
    print("2. Premium Woodland Ferret Feast: $25")
    print("3. Kale's Legendary Ferret Food: $35")
    print()
    print("A handwritten sign says:")
    print()
    print('"Kale personally guarantees that a ferret will probably eat this."')

    food_choice = input("\nChoose 1, 2, or 3: ").strip()

    food_price = 0
    food_name = ""

    if food_choice == "1":
        food_price = 15
        food_name = "Budget Ferret Nuggets"
        ferret_happiness -= 1

    elif food_choice == "2":
        food_price = 25
        food_name = "Premium Woodland Ferret Feast"
        ferret_happiness += 1

    elif food_choice == "3":
        food_price = 35
        food_name = "Kale's Legendary Ferret Food"
        ferret_happiness += 3

    else:
        print()
        print("You cannot decide, so you select the premium food.")
        food_price = 25
        food_name = "Premium Woodland Ferret Feast"
        ferret_happiness += 1

    if has_coupon:
        print()
        print("You present your pet-store coupon.")
        print("The cashier examines it carefully.")
        print()
        print('"This coupon is shaped like a paw," the cashier says.')
        print('"That means it is legally adorable."')
        print()
        print("You receive a $5 discount.")
        food_price -= 5

    if money >= food_price:
        money -= food_price
        has_ferret_food = True

        if food_name not in inventory:
            inventory.append(food_name)

        print()
        print("You purchase", food_name + ".")
        print("It costs $" + str(food_price) + ".")
        print()
        print("PRIMARY OBJECTIVE COMPLETE:")
        print("You now have ferret food for", ferret_name + "!")

    else:
        print()
        print("You do not have enough money for that food.")
        print("The cashier sadly returns it to the shelf.")
        patience -= 1

    if "Pet Store" not in visited_stores:
        visited_stores.append("Pet Store")

    wait_for_player_to_continue()


def visit_sporting_goods_store():
    global money
    global energy
    global patience
    global ferret_happiness
    global mall_reputation
    global has_boxing_gloves

    print_section_divider()
    print("THE SPORTING GOODS STORE")
    print()
    print("You enter a store filled with basketballs, camping equipment,")
    print("running shoes, fishing poles, and at least one kayak that")
    print("could not possibly fit through the front door.")
    print()
    print("A salesperson wearing a whistle approaches immediately.")
    print()
    print('"WELCOME, ATHLETE!" the salesperson shouts.')
    print()
    print('"I am Coach Thunder! What sport are we conquering today?"')
    print()
    print("You explain that you need boxing gloves for a ferret.")
    print()
    print("Coach Thunder becomes completely silent.")
    print()
    print("A single tear appears in the corner of his eye.")
    print()
    print('"At last," he whispers. "A serious customer."')
    print()
    print("Coach Thunder leads you to the boxing section.")
    print()
    print("Unfortunately, the smallest normal gloves are still")
    print("approximately the size of", ferret_name + ".")
    print()
    print("Coach Thunder presents three possible solutions:")
    print()
    print("1. Buy tiny novelty boxing gloves for $20.")
    print("2. Buy children's boxing gloves for $30.")
    print("3. Ask Coach Thunder to make custom ferret gloves for $40.")
    print("4. Challenge Coach Thunder to a shopping trivia contest.")
    print("5. Leave the store.")

    choice = input("\nChoose 1, 2, 3, 4, or 5: ").strip()

    glove_price = 0
    glove_name = ""

    if choice == "1":
        glove_price = 20
        glove_name = "Tiny Novelty Boxing Gloves"
        ferret_happiness += 1

    elif choice == "2":
        glove_price = 30
        glove_name = "Children's Boxing Gloves"
        ferret_happiness += 2

    elif choice == "3":
        glove_price = 40
        glove_name = "Custom Ferret Boxing Gloves"
        ferret_happiness += 5
        mall_reputation += 1

    elif choice == "4":
        print()
        print("Coach Thunder raises one eyebrow.")
        print()
        print('"If you answer two questions correctly," he says,')
        print('"I will give you the custom gloves for $15."')
        print()
        print("QUESTION ONE:")
        print("How many boxing gloves normally make one pair?")
        print()
        print("1. One")
        print("2. Two")
        print("3. Seven")
        print("4. It depends on the ferret")

        answer_one = input("\nYour answer: ").strip()

        trivia_score = 0

        if answer_one == "2":
            print()
            print("Correct!")
            trivia_score += 1
        else:
            print()
            print("Incorrect. A normal pair contains two gloves.")

        print()
        print("QUESTION TWO:")
        print("What is the safest purpose for tiny ferret boxing gloves?")
        print()
        print("1. Starting fights in the food court")
        print("2. Challenging a bear")
        print("3. Wearing them for a silly photograph")
        print("4. Punching household appliances")

        answer_two = input("\nYour answer: ").strip()

        if answer_two == "3":
            print()
            print("Correct!")
            trivia_score += 1
        else:
            print()
            print("Incorrect. The answer is a silly photograph.")

        if trivia_score == 2:
            print()
            print("Coach Thunder blows his whistle.")
            print()
            print('"PERFECT SCORE!" he shouts.')
            print()
            print("You unlock the custom gloves for only $15.")
            glove_price = 15
            glove_name = "Discounted Custom Ferret Boxing Gloves"
            ferret_happiness += 5
            mall_reputation += 2
        else:
            print()
            print("Coach Thunder gives you an encouraging nod.")
            print()
            print('"You showed courage," he says.')
            print()
            print("He offers the novelty gloves for $20.")
            glove_price = 20
            glove_name = "Tiny Novelty Boxing Gloves"
            ferret_happiness += 1

    elif choice == "5":
        print()
        print("You leave before Coach Thunder can assign you twenty push-ups.")
        energy -= 1
        return

    else:
        print()
        print("Coach Thunder interprets your silence as a request")
        print("for the novelty gloves.")
        glove_price = 20
        glove_name = "Tiny Novelty Boxing Gloves"

    if money >= glove_price:
        money -= glove_price
        has_boxing_gloves = True

        if glove_name not in inventory:
            inventory.append(glove_name)

        print()
        print("You purchase", glove_name + ".")
        print("They cost $" + str(glove_price) + ".")
        print()
        print("PRIMARY OBJECTIVE COMPLETE:")
        print(ferret_name, "now has boxing gloves!")
        print()
        print("You imagine", ferret_name, "wearing them.")
        print("The image is magnificent and slightly concerning.")

    else:
        print()
        print("You do not have enough money.")
        print()
        print("Coach Thunder gives you a motivational speech about")
        print("budgeting, commitment, courage, and store credit cards.")
        patience -= 2

    if "Sporting Goods Store" not in visited_stores:
        visited_stores.append("Sporting Goods Store")

    wait_for_player_to_continue()


def visit_food_court():
    global money
    global energy
    global patience
    global mall_reputation
    global has_snack
    global has_emergency_pretzel

    print_section_divider()
    print("THE FOOD COURT")
    print()
    print("The smell of pizza, cinnamon, fried potatoes, and")
    print("questionable culinary decisions fills the air.")
    print()
    print("A worker stands in the center of the walkway holding")
    print("a tray of free samples.")
    print()
    print('"FREE CHICKEN-STYLE FOOD CUBES!" the worker announces.')
    print()
    print("You notice that the sign does not say chicken.")
    print("It says chicken-style.")
    print()
    print("Nearby, one empty table remains.")
    print()
    print("You begin walking toward it.")
    print()
    print("Another customer also notices the table.")
    print()
    print("He is wearing sunglasses indoors and carrying four")
    print("shopping bags from the same expensive shoe store.")
    print()
    print("You have encountered CHAD OF THE FOOD COURT.")
    print()
    print('"That table is mine," Chad says.')
    print()
    print("What do you do?")
    print()
    print("1. Let Chad have the table.")
    print("2. Race Chad to the table.")
    print("3. Suggest sharing the table.")
    print("4. Distract Chad with a free sample.")
    print("5. Ignore the table and buy an emergency pretzel.")

    choice = input("\nChoose 1, 2, 3, 4, or 5: ").strip()

    if choice == "1":
        print()
        print("You allow Chad to take the table.")
        print()
        print("Chad places one shopping bag on each chair.")
        print("He does not actually sit down.")
        print()
        print("Your patience decreases.")
        patience -= 2

    elif choice == "2":
        print()
        print("You sprint toward the table.")
        print()
        print("Chad sprints too.")
        print()
        print("A slow-motion shopping montage begins.")
        print()
        print("You dodge a stroller.")
        print("Chad jumps over a dropped French fry.")
        print("You slide past the free-sample worker.")
        print()
        print("You reach the table first!")
        print()
        print("The surrounding shoppers applaud.")
        energy -= 2
        mall_reputation += 2

    elif choice == "3":
        print()
        print('"There are several chairs," you say.')
        print('"We could share the table."')
        print()
        print("Chad looks confused.")
        print()
        print("No one has ever suggested cooperation to him before.")
        print()
        print("After a long pause, Chad agrees.")
        print()
        print("You both sit down.")
        print("Chad quietly offers you a coupon for athletic socks.")
        patience += 1
        mall_reputation += 1

    elif choice == "4":
        print()
        print("You point toward the sample tray.")
        print()
        print('"I heard those cubes are extremely exclusive," you say.')
        print()
        print("Chad immediately abandons the table.")
        print()
        print("You sit down in victory.")
        print()
        print("Chad returns several minutes later looking confused")
        print("and holding six chicken-style cubes.")
        mall_reputation += 1

    elif choice == "5":
        print()
        print("You walk to the pretzel counter.")
        print()
        print("For $8, you purchase a pretzel roughly the size")
        print("of a steering wheel.")

        if money >= 8:
            money -= 8
            energy += 3
            has_emergency_pretzel = True
            has_snack = True

            if "Emergency Pretzel" not in inventory:
                inventory.append("Emergency Pretzel")

            print()
            print("The pretzel restores three energy.")
        else:
            print()
            print("You cannot afford the pretzel.")
            patience -= 1

    else:
        print()
        print("You stand between Chad and the table while trying")
        print("to decide what to do.")
        print()
        print("A family of eight takes the table.")
        print()
        print("Both you and Chad lose.")
        patience -= 1

    print()
    print("Before leaving, you may buy a snack.")
    print()
    print("1. Pizza slice for $7")
    print("2. Cinnamon roll for $6")
    print("3. Suspicious free sample for $0")
    print("4. Buy nothing")

    snack_choice = input("\nChoose 1, 2, 3, or 4: ").strip()

    if snack_choice == "1":
        if money >= 7:
            money -= 7
            energy += 3
            has_snack = True
            inventory.append("Food Court Pizza Slice")
            print()
            print("The pizza restores three energy.")
        else:
            print()
            print("You cannot afford the pizza.")

    elif snack_choice == "2":
        if money >= 6:
            money -= 6
            energy += 2
            patience += 1
            has_snack = True
            inventory.append("Cinnamon Roll")
            print()
            print("The cinnamon roll restores two energy")
            print("and one patience.")
        else:
            print()
            print("You cannot afford the cinnamon roll.")

    elif snack_choice == "3":
        print()
        print("You eat the chicken-style food cube.")
        print()
        print("It tastes like chicken that heard a description")
        print("of another chicken from across a crowded room.")
        print()
        print("You gain one energy but lose one patience.")
        energy += 1
        patience -= 1

    elif snack_choice == "4":
        print()
        print("You decide to save your money.")

    else:
        print()
        print("You accidentally make eye contact with the sample worker.")
        print("A food cube is placed into your hand.")
        inventory.append("Unidentified Food Cube")

    if "Food Court" not in visited_stores:
        visited_stores.append("Food Court")

    wait_for_player_to_continue()


def visit_sunglasses_kiosk():
    global money
    global patience
    global mall_reputation
    global has_sunglasses

    print_section_divider()
    print("THE SUNGLASSES KIOSK")
    print()
    print("You walk past a kiosk covered with hundreds of sunglasses.")
    print()
    print("The salesperson spots you.")
    print()
    print('"HELLO, FASHIONABLE STRANGER!" the salesperson calls.')
    print()
    print("You make the mistake of slowing down.")
    print()
    print("The salesperson places three pairs of sunglasses")
    print("on the counter.")
    print()
    print('"These glasses will change your life," the salesperson says.')
    print()
    print("You explain that you only need ferret food and boxing gloves.")
    print()
    print('"Perfect!" the salesperson replies.')
    print('"Your ferret will respect you more if you look mysterious."')
    print()
    print("What do you do?")
    print()
    print("1. Politely say no.")
    print("2. Walk away without speaking.")
    print("3. Try on the most ridiculous pair.")
    print("4. Ask whether the sunglasses come in ferret size.")
    print("5. Buy sunglasses for $18.")

    choice = input("\nChoose 1, 2, 3, 4, or 5: ").strip()

    if choice == "1":
        print()
        print('"No, thank you," you say.')
        print()
        print("The salesperson begins another sales pitch.")
        print()
        print('"Still no, thank you," you repeat.')
        print()
        print("The salesperson begins a third sales pitch.")
        print()
        print('"No," you say with the strength of ten shoppers.')
        print()
        print("You escape.")
        patience -= 1
        mall_reputation += 1

    elif choice == "2":
        print()
        print("You continue walking.")
        print()
        print("The salesperson follows you for twelve steps.")
        print()
        print('"You forgot to improve your life!" they shout.')
        print()
        print("You successfully escape.")
        patience -= 1

    elif choice == "3":
        print()
        print("You try on sunglasses shaped like lightning bolts.")
        print()
        print("Every shopper nearby becomes silent.")
        print()
        print("The salesperson gasps.")
        print()
        print('"They have chosen you," the salesperson whispers.')
        print()
        print("You take them off before the prophecy can continue.")
        mall_reputation += 2

    elif choice == "4":
        print()
        print("The salesperson freezes.")
        print()
        print('"Ferret size?" they ask.')
        print()
        print("They search through six boxes.")
        print()
        print("At last, they produce a tiny pair of sunglasses.")
        print()
        print('"Take them," the salesperson says. "No charge."')
        print()
        print("You receive Tiny Ferret Sunglasses.")
        inventory.append("Tiny Ferret Sunglasses")
        mall_reputation += 2

    elif choice == "5":
        if money >= 18:
            money -= 18
            has_sunglasses = True
            inventory.append("Unnecessarily Dramatic Sunglasses")
            mall_reputation += 1

            print()
            print("You purchase the sunglasses.")
            print()
            print("You immediately look 40 percent more mysterious.")
            print()
            print("This statistic has not been independently verified.")
        else:
            print()
            print("You cannot afford the sunglasses.")
            print("The salesperson looks personally betrayed.")
            patience -= 1

    else:
        print()
        print("You become trapped in a seven-minute demonstration")
        print("about polarized lenses.")
        patience -= 2

    if "Sunglasses Kiosk" not in visited_stores:
        visited_stores.append("Sunglasses Kiosk")

    wait_for_player_to_continue()


def visit_customer_service_desk():
    global patience
    global mall_reputation
    global has_mall_map
    global has_coupon

    print_section_divider()
    print("CUSTOMER SERVICE")
    print()
    print("You approach the mall's customer-service desk.")
    print()
    print("A tired employee sits beneath a sign that says:")
    print()
    print('"WE ARE HAPPY TO HELP."')
    print()
    print("The employee does not look happy.")
    print()
    print('"How may I help you?" the employee asks.')
    print()
    print("What do you request?")
    print()
    print("1. Ask for a mall map.")
    print("2. Ask whether there are pet-store coupons.")
    print("3. Report Karen for blocking the pet-store aisle.")
    print("4. Report Chad for occupying food-court chairs with bags.")
    print("5. Ask where the exit is.")

    choice = input("\nChoose 1, 2, 3, 4, or 5: ").strip()

    if choice == "1":
        if not has_mall_map:
            has_mall_map = True
            inventory.append("Mall Map")

        print()
        print("The employee gives you a mall map.")
        print()
        print("The map is three feet wide and folds into")
        print("approximately nine hundred sections.")
        print()
        print("You gain one patience because you now feel organized.")
        patience += 1

    elif choice == "2":
        if not has_coupon:
            has_coupon = True
            inventory.append("Pet Store Coupon")

        print()
        print("The employee reaches beneath the desk.")
        print()
        print("You receive a $5 pet-store coupon.")
        mall_reputation += 1

    elif choice == "3":
        print()
        print("The employee begins filling out a form.")
        print()
        print('"Was the shopping cart horizontal, diagonal,')
        print('or aggressively perpendicular?" the employee asks.')
        print()
        print("You answer seventeen detailed questions.")
        print()
        print("You lose one patience but gain two mall reputation.")
        patience -= 1
        mall_reputation += 2

    elif choice == "4":
        print()
        print("The employee nods.")
        print()
        print('"Chad again," they say.')
        print()
        print("They stamp a form marked CHAD INCIDENT.")
        mall_reputation += 2

    elif choice == "5":
        print()
        print("The employee points toward a giant glowing EXIT sign.")
        print()
        print("You pretend that you already knew it was there.")
        mall_reputation -= 1

    else:
        print()
        print("You ask an unclear question involving ferrets,")
        print("boxing gloves, pretzels, and aisle jurisdiction.")
        print()
        print("The employee gives you a brochure about mall safety.")

        if "Mall Safety Brochure" not in inventory:
            inventory.append("Mall Safety Brochure")

    if "Customer Service" not in visited_stores:
        visited_stores.append("Customer Service")

    wait_for_player_to_continue()


def visit_department_store():
    global money
    global energy
    global patience
    global mall_reputation

    print_section_divider()
    print("THE DEPARTMENT STORE")
    print()
    print("You enter the department store.")
    print()
    print("Immediately, a cloud of perfume surrounds you.")
    print()
    print("You can no longer see the entrance.")
    print()
    print("Clothing racks stretch in every direction.")
    print()
    print("A sign above you says:")
    print()
    print('"CLEARANCE THIS WAY."')
    print()
    print("Another sign points in the opposite direction and also says:")
    print()
    print('"CLEARANCE THIS WAY."')
    print()
    print("You hear footsteps behind you.")
    print()
    print("A customer carrying twelve sweaters approaches.")
    print()
    print('"Are you using that coupon?" the customer asks.')
    print()
    print("You look down.")
    print("A coupon is stuck to your shoe.")
    print()
    print("What do you do?")
    print()
    print("1. Give the customer the coupon.")
    print("2. Keep the coupon.")
    print("3. Ask how the coupon became attached to your shoe.")
    print("4. Pretend the coupon is an ancient treasure map.")
    print("5. Attempt to find the exit.")

    choice = input("\nChoose 1, 2, 3, 4, or 5: ").strip()

    if choice == "1":
        print()
        print("You give the coupon to the customer.")
        print()
        print("The customer is stunned by your generosity.")
        print()
        print("In return, they give you a five-dollar bill.")
        money += 5
        mall_reputation += 2

    elif choice == "2":
        print()
        print("You keep the coupon.")
        print()
        print("It offers 10 percent off a decorative pillow")
        print("shaped like a baked potato.")
        print()
        print("You do not need such a pillow.")
        print()
        print("You suddenly want such a pillow.")
        inventory.append("Potato Pillow Coupon")
        patience -= 1

    elif choice == "3":
        print()
        print("You begin investigating the coupon.")
        print()
        print("You discover three more coupons stuck to your other shoe.")
        print()
        print("No one can explain this.")
        print()
        print("You sell the coupons to nearby bargain hunters for $6.")
        money += 6
        mall_reputation += 1

    elif choice == "4":
        print()
        print("You hold the coupon above your head.")
        print()
        print('"This map leads to the legendary Golden Clearance Rack!"')
        print()
        print("Five shoppers immediately follow you.")
        print()
        print("You accidentally become the leader of a clearance expedition.")
        print()
        print("After ten minutes, you escape behind a curtain display.")
        energy -= 2
        mall_reputation += 3

    elif choice == "5":
        print()
        print("You follow the EXIT signs.")
        print()
        print("They lead you past shoes, cookware, bedding, towels,")
        print("winter coats, and a piano no one remembers ordering.")
        print()
        print("Eventually, you find the doorway.")
        energy -= 1

    else:
        print()
        print("You become distracted by an automatic tie rack.")
        print()
        print("You watch it rotate for several minutes.")
        patience -= 1

    if "Department Store" not in visited_stores:
        visited_stores.append("Department Store")

    wait_for_player_to_continue()


def trigger_hallway_encounter():
    global money
    global energy
    global patience
    global mall_reputation

    print()
    print("As you travel through the mall...")

    encounter_number = turn_number % 5

    if encounter_number == 0:
        print()
        print("A miniature mall train passes in front of you.")
        print("The conductor waves.")
        print("A toddler wearing a crown waves back.")
        print("You regain one patience.")
        patience += 1

    elif encounter_number == 1:
        print()
        print("A salesperson offers you a free skin-care demonstration.")
        print("You say no.")
        print("The salesperson continues walking beside you.")
        print("You say no again.")
        print("The salesperson asks whether you are sure.")
        print("You lose one patience.")
        patience -= 1

    elif encounter_number == 2:
        print()
        print("You find a dollar near the decorative fountain.")
        print("You ask nearby shoppers whether they dropped it.")
        print("No one claims it.")
        print("You gain $1.")
        money += 1

    elif encounter_number == 3:
        print()
        print("A group of teenagers walks slowly across")
        print("the entire width of the hallway.")
        print("There is no way around them.")
        print("You lose one energy.")
        energy -= 1

    else:
        print()
        print("A mall security guard compliments your shopping bag.")
        print("You gain one mall reputation.")
        mall_reputation += 1


def attempt_to_leave_the_mall():
    global game_running
    global completed_objectives

    print_section_divider()
    print("THE FINAL ESCAPE")
    print()
    print("You stand near the main mall exit.")
    print()
    print("Beyond the glass doors lies the parking lot.")
    print()
    print("Fresh air.")
    print("Freedom.")
    print("Your vehicle.")
    print()
    print("Probably.")
    print()
    print("You check your shopping list.")

    completed_objectives = 0

    if has_ferret_food:
        completed_objectives += 1
        print()
        print("[COMPLETE] Ferret food")

    else:
        print()
        print("[MISSING] Ferret food")

    if has_boxing_gloves:
        completed_objectives += 1
        print("[COMPLETE] Ferret-sized boxing gloves")

    else:
        print("[MISSING] Ferret-sized boxing gloves")

    print()

    if completed_objectives == 2:
        print("You have completed both primary objectives.")
        print()
        print("However, one final obstacle blocks the exit.")
        print()
        print("A kiosk salesperson steps in front of you.")
        print()
        print('"Before you leave," the salesperson says,')
        print('"would you like to switch your phone provider?"')
        print()
        print("This is the final challenge.")
        print()
        print("1. Say, 'No, thank you,' and continue walking.")
        print("2. Pretend you do not own a telephone.")
        print("3. Begin explaining your entire ferret adventure.")
        print("4. Offer the salesperson the emergency pretzel.")
        print("5. Run.")

        final_choice = input("\nChoose 1, 2, 3, 4, or 5: ").strip()

        if final_choice == "1":
            print()
            print("You make eye contact.")
            print()
            print('"No, thank you," you say.')
            print()
            print("You do not stop walking.")
            print()
            print("The salesperson recognizes your confidence.")
            print("You pass through the exit.")

        elif final_choice == "2":
            print()
            print('"I have never heard of a telephone," you say.')
            print()
            print("The salesperson looks at the phone in your hand.")
            print()
            print('"This is a calculator," you explain.')
            print()
            print("The salesperson is too confused to stop you.")

        elif final_choice == "3":
            print()
            print("You begin at the pet store.")
            print()
            print("You explain Karen, the parrot, Coach Thunder,")
            print("the boxing gloves, Chad, the food court,")
            print("and every item currently in your inventory.")
            print()
            print("The salesperson slowly backs away.")
            print()
            print("The path to the exit is clear.")

        elif final_choice == "4":
            if has_emergency_pretzel:
                print()
                print("You present the emergency pretzel.")
                print()
                print("The salesperson accepts it.")
                print()
                print("No additional words are necessary.")
                print("The ancient mall bargain has been honored.")
            else:
                print()
                print("You reach into your bag.")
                print()
                print("You do not have an emergency pretzel.")
                print()
                print("You pretend to find one anyway.")
                print()
                print("The salesperson becomes uncomfortable")
                print("and allows you to pass.")

        elif final_choice == "5":
            print()
            print("You run.")
            print()
            print("Your shopping bags swing wildly.")
            print("The automatic doors open at the last possible moment.")
            print()
            print("You burst into the parking lot in triumph.")

        else:
            print()
            print("You simply continue walking.")
            print()
            print("Sometimes refusing to participate is the")
            print("most powerful choice of all.")

        print()
        print("=" * 70)
        print("                    MISSION ACCOMPLISHED")
        print("=" * 70)
        print()
        print(player_name, "has survived the mall.")
        print()
        print("You return home and place the shopping bags")
        print("in front of", ferret_name + ".")
        print()
        print(ferret_name, "investigates the ferret food.")
        print(ferret_name, "then examines the boxing gloves.")
        print()
        print("The ferret puts on the gloves.")
        print()
        print("For one dramatic moment, the room becomes silent.")
        print()
        print(ferret_name, "raises both tiny gloves into the air.")
        print()
        print("The training montage begins tomorrow.")
        print()
        print("For tonight, you are victorious.")

        game_running = False

    elif completed_objectives == 1:
        print("You completed one of the two primary objectives.")
        print()
        print("You can leave now, but the mission will only")
        print("be considered a partial success.")
        print()
        print("1. Leave the mall.")
        print("2. Return to shopping.")

        choice = input("\nChoose 1 or 2: ").strip()

        if choice == "1":
            print()
            print("You decide that surviving is more important")
            print("than completing every objective.")
            print()
            print("You leave the mall.")
            print()
            print("=" * 70)
            print("                     PARTIAL VICTORY")
            print("=" * 70)
            print()
            print(ferret_name, "is pleased with your effort,")
            print("but clearly expects another shopping trip.")
            game_running = False
        else:
            print()
            print("You turn away from the exit.")
            print("The adventure continues.")

    else:
        print("You have not completed either primary objective.")
        print()
        print("Leaving now would mean returning home empty-handed.")
        print()
        print("1. Leave anyway.")
        print("2. Return to shopping.")

        choice = input("\nChoose 1 or 2: ").strip()

        if choice == "1":
            print()
            print("You leave the mall.")
            print()
            print("When you arrive home,", ferret_name, "looks inside")
            print("the empty shopping bag.")
            print()
            print("The ferret looks at you.")
            print()
            print("You look at the ferret.")
            print()
            print("No words are spoken.")
            print()
            print("=" * 70)
            print("                      MISSION FAILED")
            print("=" * 70)
            game_running = False
        else:
            print()
            print("You refuse to surrender.")
            print("You return to the mall.")


print("It is Saturday morning.")
print()
print("You are sitting peacefully at home when", ferret_name)
print("runs into the room carrying a tiny clipboard.")
print()
print("The clipboard contains a shopping list:")
print()

for item in shopping_list:
    print("  -", item)

print()
print("At the bottom of the list, the ferret has added:")
print()
print('"DO NOT RETURN WITHOUT THE GLOVES."')
print()
print("You check your wallet.")
print("You have $" + str(money) + ".")
print()
print("You grab your keys and begin the expedition.")
wait_for_player_to_continue()

print_section_divider()

print("You arrive at the mall.")
print()
print("The parking lot appears to contain more vehicles")
print("than have ever been manufactured.")
print()
print("After circling the building three times, you find")
print("a parking place beside a cart-return station.")
print()
print("You enter through the main doors.")
print()
print("Cold air-conditioning hits you immediately.")
print()
print("Music echoes through the building.")
print()
print("A fountain launches water toward the ceiling.")
print()
print("Somewhere in the distance, a child demands a pretzel.")
print()
print("Your adventure has begun.")
wait_for_player_to_continue()


while game_running:
    end_game_if_player_resources_are_depleted()

    if not game_running:
        break

    print_section_divider()

    print("MALL TURN:", turn_number)
    print()
    print("Where would you like to go?")
    print()
    print("1. Pet store")
    print("2. Sporting goods store")
    print("3. Food court")
    print("4. Sunglasses kiosk")
    print("5. Customer service")
    print("6. Department store")
    print("7. Check status and inventory")
    print("8. View mall directory")
    print("9. Attempt to leave the mall")

    location_choice = input("\nChoose 1 through 9: ").strip()

    if location_choice == "1":
        visit_pet_store()

    elif location_choice == "2":
        visit_sporting_goods_store()

    elif location_choice == "3":
        visit_food_court()

    elif location_choice == "4":
        visit_sunglasses_kiosk()

    elif location_choice == "5":
        visit_customer_service_desk()

    elif location_choice == "6":
        visit_department_store()

    elif location_choice == "7":
        display_current_shopping_status()

    elif location_choice == "8":
        display_mall_directory()

    elif location_choice == "9":
        attempt_to_leave_the_mall()

    else:
        print()
        print("You study the mall directory but cannot decide")
        print("where to go.")
        print()
        print("A family walks around you.")
        print("A kiosk salesperson begins moving in your direction.")
        print()
        print("You should probably select a valid number.")
        patience -= 1

    if game_running and location_choice not in ["7", "8", "9"]:
        turn_number += 1
        trigger_hallway_encounter()
        end_game_if_player_resources_are_depleted()


print_section_divider()

print("FINAL SHOPPING REPORT")
print()
print("Shopper:", player_name)
print("Ferret:", ferret_name)
print("Money remaining: $" + str(money))
print("Energy remaining:", energy)
print("Patience remaining:", patience)
print("Ferret happiness:", ferret_happiness)
print("Mall reputation:", mall_reputation)
print("Mall turns completed:", turn_number)

print()
print("Locations visited:")

if len(visited_stores) == 0:
    print("  No locations were successfully visited.")
else:
    for store in visited_stores:
        print("  -", store)

print()
print("Final inventory:")

if len(inventory) == 0:
    print("  Your shopping bag is empty.")
else:
    item_number = 1

    for item in inventory:
        print(" ", str(item_number) + ".", item)
        item_number += 1

print()
print("Objective results:")

if has_ferret_food:
    print("  [COMPLETE] Ferret food acquired")
else:
    print("  [INCOMPLETE] Ferret food not acquired")

if has_boxing_gloves:
    print("  [COMPLETE] Ferret boxing gloves acquired")
else:
    print("  [INCOMPLETE] Ferret boxing gloves not acquired")

print()
print("Ending assessment:")

if has_ferret_food and has_boxing_gloves:
    if ferret_happiness >= 10:
        print("LEGENDARY ENDING:")
        print(ferret_name, "declares you the greatest shopper in history.")

    elif ferret_happiness >= 6:
        print("HAPPY FERRET ENDING:")
        print(ferret_name, "is pleased with your shopping success.")

    else:
        print("TECHNICALLY SUCCESSFUL ENDING:")
        print("You completed the mission, although", ferret_name)
        print("has several comments about your product selections.")

elif has_ferret_food:
    print("WELL-FED FERRET ENDING:")
    print(ferret_name, "has food but no boxing gloves.")
    print("The rematch has been postponed.")

elif has_boxing_gloves:
    print("HUNGRY BOXER ENDING:")
    print(ferret_name, "has boxing gloves but no ferret food.")
    print("This situation may require immediate attention.")

else:
    print("EMPTY SHOPPING BAG ENDING:")
    print("The mall defeated you this time.")

print()
print("=" * 70)
print("                 THANK YOU FOR PLAYING")
print("=" * 70)
print()
