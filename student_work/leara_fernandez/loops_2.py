"""
===============================================================================
PYTHON CORE LOGIC MASTERCLASS: FROM IF-STATEMENTS TO LOOPS & BEYOND
===============================================================================
This file demonstrates how basic logic structures build upon each other.
Read through the code and comments, run it in your terminal, and observe how
simple building blocks create powerful applications!
===============================================================================
"""

# =============================================================================
# SECTION 1: IF STATEMENTS & BOOLEAN LOGIC
# =============================================================================
print("--- SECTION 1: IF STATEMENTS ---")

energy_level = 75
has_coffee = True

# --- BAD LOGIC EXAMPLES ---
# 1. Redundant boolean check (`== True`).
# 2. Duplicate nested checks that make code hard to follow.
if has_coffee == True:
    if energy_level > 50:
        status_bad = "Ready to code!"
    else:
        status_bad = "Needs more coffee."

# --- GOOD LOGIC EXAMPLES ---
# 1. Clean boolean evaluation without `== True`.
# 2. Combining conditions using logical operators (`and`, `or`).
if has_coffee and energy_level > 50:
    status_good = "Ready to code!"
elif has_coffee:
    status_good = "Needs more coffee."
else:
    status_good = "Exhausted."

print(f"Good Logic Output: {status_good}\n")


# =============================================================================
# SECTION 2: WHILE LOOPS (Condition-Based Repetition)
# =============================================================================
print("--- SECTION 2: WHILE LOOPS ---")

# --- BAD LOGIC EXAMPLES ---
# Using a manual break flag when a direct condition or `while True` with clear exit is cleaner.
counter = 0
keep_going = True
while keep_going:
    if counter >= 3:
        keep_going = False  # Delayed state mutation causes extra loop checks
    else:
        print(f"Bad loop step: {counter}")
        counter += 1

print()

# --- GOOD LOGIC EXAMPLES ---
# Clear loop condition directly expressing intent.
attempt = 0
max_attempts = 3

while attempt < max_attempts:
    print(f"Connecting to server... Attempt {attempt + 1}/{max_attempts}")
    attempt += 1

print("\nConnection established!\n")


# =============================================================================
# SECTION 3: FOR LOOPS (Sequence-Based Repetition)
# =============================================================================
print("--- SECTION 3: FOR LOOPS ---")

tools = ["Python", "Git", "Docker", "SQL"]

# --- BAD LOGIC EXAMPLES ---
# Using `range(len(...))` to iterate over list indices when index isn't needed.
print("Bad Logic Iteration:")
for i in range(len(tools)):
    print(f"Tool: {tools[i]}")

print()

# --- GOOD LOGIC EXAMPLES ---
# Direct iteration over elements. Use `enumerate` if you need the index!
print("Good Logic Iteration:")
for index, tool in enumerate(tools, start=1):
    print(f"{index}. {tool}")

print("\n")


# =============================================================================
# SECTION 4: COMBINING LOOPS & IF STATEMENTS
# =============================================================================
print("--- SECTION 4: FILTERING & PROCESSING DATA ---")

scores = [45, 88, 92, 60, 30, 100, 74]

# --- BAD LOGIC EXAMPLES ---
# Deeply nested conditional logic inside loops (Pyramid of Doom).
print("Bad Logic Processing:")
for score in scores:
    if score >= 50:
        if score >= 90:
            print(f"Score {score}: High Distinction")
        else:
            print(f"Score {score}: Pass")
    else:
        print(f"Score {score}: Fail")

print()

# --- GOOD LOGIC EXAMPLES ---
# Using Guard Clauses / Early Exit inside loops to keep code clean and readable.
print("Good Logic Processing:")
for score in scores:
    if score < 50:
        print(f"Score {score:3d}: Fail")
        continue  # Skip to the next iteration immediately

    # Rest of code runs only for passing scores
    grade = "High Distinction" if score >= 90 else "Pass"
    print(f"Score {score:3d}: {grade}")

print("\n" + "="*70 + "\n")


# =============================================================================
# SECTION 5: GRAND FINALE - CYBERPUNK HACKATHON SIMULATOR
# Connecting If Statements, While Loops, For Loops, Lists, and Functions!
# =============================================================================
import random
import time

def run_hackathon_sim():
    print("🚀 WELCOME TO THE NIGHT CITY HACKATHON SIMULATOR 🚀")
    print("Objective: Complete 3 network hacks before running out of RAM or Time!\n")

    # State variables
    ram_gb = 16
    time_remaining_hrs = 8
    hacks_completed = 0
    required_hacks = 3

    servers = [
        {"name": "Mainframe Gateway", "difficulty": 30, "ram_cost": 3},
        {"name": "Data Vault Alpha", "difficulty": 60, "ram_cost": 5},
        {"name": "AI Core Processor", "difficulty": 85, "ram_cost": 8},
    ]

    # MAIN LOOP: Game continues while conditions are met
    while hacks_completed < required_hacks and ram_gb > 0 and time_remaining_hrs > 0:
        target = servers[hacks_completed]

        print(f"--- STATUS: RAM {ram_gb}GB | Time Left: {time_remaining_hrs}h | Hacks: {hacks_completed}/{required_hacks} ---")
        print(f"Current Target: {target['name']} (Diff: {target['difficulty']}%, RAM Cost: {target['ram_cost']}GB)")

        # Action prompt loop
        print("\nChoose Action:")
        print("1. Launch Cyber-Attack")
        print("2. Optimize Memory (Restore RAM)")
        print("3. Take a Nap (Restore Time/RAM)")

        # Simulating automated strategic decisions
        # (In interactive mode, this could be input())
        if ram_gb < target['ram_cost']:
            action = "2"
        elif time_remaining_hrs <= 2:
            action = "1"  # Desperation attack
        else:
            action = "1"

        print(f"> Selected Choice: {action}")
        time.sleep(0.5)

        # BRANCHING LOGIC: Evaluate Action
        if action == "1":
            # Attempt Hack
            ram_gb -= target['ram_cost']
            time_remaining_hrs -= 1

            # Roll random success percentage
            hack_power = random.randint(1, 100)
            print(f"Executing exploit... Hack Power Rolled: {hack_power}%")

            if hack_power >= target['difficulty']:
                print(f"✅ SUCCESS! {target['name']} breached!\n")
                hacks_completed += 1
            else:
                print(f"❌ FAIL! Intrusion Detected. RAM consumed.\n")

        elif action == "2":
            # Restore RAM
            restored = random.randint(3, 6)
            ram_gb = min(16, ram_gb + restored)
            time_remaining_hrs -= 1
            print(f"🧹 Cleaned system memory. Restored {restored}GB RAM.\n")

        elif action == "3":
            # Rest
            time_remaining_hrs -= 2
            ram_gb = 16
            print("💤 Took a quick nap. RAM fully restored to 16GB, but lost 2 hours!\n")

    # END GAME LOGIC: Evaluating win/loss conditions
    print("="*50)
    if hacks_completed == required_hacks:
        print("🎉 VICTORY! You successfully hacked all systems and won the Hackathon!")
    elif ram_gb <= 0:
        print("💥 SYSTEM CRASH! Out of RAM. Your system froze up!")
    else:
        print("⏰ TIME OUT! The hackathon ended before you finished.")
    print("="*50)

# Run the simulation
if __name__ == "__main__":
    run_hackathon_sim()
