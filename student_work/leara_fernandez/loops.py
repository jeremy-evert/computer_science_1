"""
===============================================================================
    PYTHON FOUNDATIONS: FROM DECISIONS TO LOOPS & CREATIVE SYSTEMS
===============================================================================

Welcome! Python is built around readability and logic. This guide takes you from
making simple single decisions to orchestrating complex loops and structures.
"""

# =============================================================================
# PART 1: CONDITIONAL LOGIC (IF / ELIF / ELSE)
# =============================================================================
# Programs use conditional statements to evaluate expressions that return
# Boolean values: True or False.

player_score = 85

# A basic if/elif/else chain checks conditions top-to-bottom and executes
# only the first block whose condition evaluates to True.
if player_score >= 90:
    rank = "Master"
elif player_score >= 80:
    rank = "Expert"
elif player_score >= 70:
    rank = "Apprentice"
else:
    rank = "Novice"

print(f"Score: {player_score} -> Rank: {rank}")


# =============================================================================
# PART 2: THE FOR LOOP (ITERATING OVER SEQUENCES)
# =============================================================================
# A 'for' loop is used when you know in advance how many times you want to iterate,
# or when you want to step through a sequence (like a list, string, or range).

print("\n--- Basic For Loop with range() ---")
# range(start, stop) generates numbers from start up to (but not including) stop.
for step in range(1, 5):
    print(f"Step {step} completed.")

print("\n--- Iterating over a List ---")
inventory = ["torch", "potion", "shield", "map"]
for item in inventory:
    print(f"Inventory Item: {item}")


# =============================================================================
# PART 3: THE WHILE LOOP (CONDITION-BASED ITERATION)
# =============================================================================
# A 'while' loop repeats as long as a specified condition remains True.
# Always ensure the condition will eventually become False to prevent infinite loops!

print("\n--- While Loop Example ---")
energy = 30

while energy > 0:
    print(f"Action taken! Energy remaining: {energy}")
    energy -= 10  # Decrement energy to eventually terminate the loop.

print("Energy depleted! Resting...")


# =============================================================================
# PART 4: CONNECTING LOOPS AND IF STATEMENTS
# =============================================================================
# Combining loops with conditionals allows you to filter, modify, or react to
# data dynamically during iteration.

print("\n--- Filtering Data inside a Loop ---")
scores = [45, 88, 92, 60, 71, 95]
passing_scores = []

for score in scores:
    if score >= 70:
        passing_scores.append(score)
        print(f"Score {score}: PASSED")
    else:
        print(f"Score {score}: Needs Improvement")

print(f"Total passing scores: {passing_scores}")


# =============================================================================
# PART 5: CREATIVE INTEGRATION — PROCEDURAL WORLD MAP GENERATOR
# =============================================================================
# Here we combine conditionals, nested loops (loops inside loops), lists, and
# dictionaries to build a procedural ASCII map rendering engine.

print("\n=================================================================")
print("          PROCEDURAL WORLD MAP GENERATOR (GRID & TILE SYSTEM)      ")
print("=================================================================\n")

# Define grid dimensions
WIDTH = 20
HEIGHT = 8

# Define visual representations for tile types
TILES = {
    "WATER": "~",
    "SAND": ".",
    "GRASS": '"',
    "FOREST": "T",
    "MOUNTAIN": "^"
}

# Nested loop to generate rows (y) and columns (x)
for y in range(HEIGHT):
    row_visuals = []

    for x in range(WIDTH):
        # Determine tile type using coordinate rules and conditionals

        # 1. Outer boundary is deep ocean / water
        if y == 0 or y == HEIGHT - 1 or x == 0 or x == WIDTH - 1:
            tile_symbol = TILES["WATER"]

        # 2. Coastal shoreline rule (adjacent to boundaries)
        elif y == 1 or y == HEIGHT - 2 or x == 1 or x == WIDTH - 2:
            tile_symbol = TILES["SAND"]

        # 3. Central features based on coordinates
        else:
            # Create a mountain range in the upper-right section
            if x > 12 and y < 4:
                tile_symbol = TILES["MOUNTAIN"]
            # Create a forest area in the middle-left section
            elif x < 8 and 2 <= y <= 5:
                tile_symbol = TILES["FOREST"]
            # Default land cover
            else:
                tile_symbol = TILES["GRASS"]

        row_visuals.append(tile_symbol)

    # Print the constructed row as a single string
    print(" ".join(row_visuals))

print("\nMap Legend:")
for name, symbol in TILES.items():
    print(f"  {symbol} : {name}")
