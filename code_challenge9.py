# 🦜 PARROT SIMULATOR – THE ECHO CHAMBER!

print("🦜 PARROT SIMULATOR – THE ECHO CHAMBER!")

phrase = input("What do you want your parrot to say? ")
times = int(input("How many times should the parrot squawk it? "))

print("\nListen to your parrot:")

for i in range(times):
    print(f"🦜 Squawk! {phrase}")
