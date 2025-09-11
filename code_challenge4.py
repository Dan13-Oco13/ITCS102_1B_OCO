print("Welcome to the Exercise Plan Recommender!")
print("Answer a few questions to get your workout suggestion")

# user inputs
exercise = input("What kind of exercise do you want to do? (Calisthenics/Gym/Hybrid): "))
place = input("Where do you plan to exercise? (Indoor gym/Outdoor gym/At home): "))
level = input("What level can you handle? (Light/Heavy): "))

# Calisthenics recommendations
if exercise == 'calisthenics':
    if place == 'at home':
        if level == 'light':
            print("We Recommend You: Basic Push-Ups and Planks")
        elif level == 'heavy':
            print("We Recommend You: Handstand Push-Ups and Muscle-Ups")
        else:
            print("INVALID level")
    elif place == 'outdoor gym':
        if level == 'light':
            print("We Recommend You: Pull-Ups and Dips")
        elif level == 'heavy':
            print("We Recommend You: Weighted Pull-Ups and Front Lever Training")
        else:
            print("INVALID level")
    elif place == 'indoor gym':
        if level == 'light':
            print("We Recommend You: Assisted Pull-Ups and Parallel Bar Dips")
        elif level == 'heavy':
            print("We Recommend You: One-Arm Pull-Ups and Planche Progressions")
        else:
            print("INVALID level")
    else:
        print("INVALID place")

# Gym recommendations
elif exercise == 'gym':
    if place == 'indoor gym':
        if level == 'light':
            print("We Recommend You: Treadmill Walk + Light Dumbbell Workout")
        elif level == 'heavy':
            print("We Recommend You: Deadlifts and Bench Press Routine")
        else:
            print("INVALID level")
    elif place == 'outdoor gym':
        if level == 'light':
            print("We Recommend You: Bodyweight Squats and Resistance Bands")
        elif level == 'heavy':
            print("We Recommend You: Weighted Squats and Tire Flips")
        else:
            print("INVALID level")
    elif place == 'at home':
        if level == 'light':
            print("We Recommend You: Jumping Jacks + Dumbbell Press")
        elif level == 'heavy':
            print("We Recommend You: Home Barbell Training")
        else:
            print("INVALID level")
    else:
        print("INVALID place")

# Hybrid recommendations
elif exercise == 'hybrid':
    if place == 'indoor gym':
        if level == 'light':
            print("We Recommend You: 20 min Cardio + Push-Ups + Dumbbell Curls")
        elif level == 'heavy':
            print("We Recommend You: Squats + Pull-Ups + Bench Press Circuit")
        else:
            print("INVALID level")
    elif place == 'outdoor gym':
        if level == 'light':
            print("We Recommend You: Jogging + Dips + Light Resistance Bands")
        elif level == 'heavy':
            print("We Recommend You: Sprints + Muscle-Ups + Weighted Squats")
        else:
            print("INVALID level")
    elif place == 'at home':
        if level == 'light':
            print("We Recommend You: Yoga + Push-Ups + Sit-Ups")
        elif level == 'heavy':
            print("We Recommend You: Burpees + Pull-Ups + Weighted Squats (if equipment available)")
        else:
            print("INVALID level")
    else:
        print("INVALID place")

else:
    print("INVALID exercise type")
