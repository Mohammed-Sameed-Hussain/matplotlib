import pandas as pd

def generate_timetable():
    # Define the structure of the timetable
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    slots = [
        "9:00-9:55 (A)", "10:00-10:55 (B)", "11:00-11:55 (C)", "12:00-12:55 (D)",
        "12:55-14:30 (Lunch)", "14:30-15:55 (P)", "16:00-17:25 (Q)"
    ]

    # Initialize an empty timetable dictionary
    timetable = {day: ["" for _ in slots] for day in days}

    print("Enter the courses and their respective slots in the format <Course>:<Slot> (e.g., Physics:A). Type 'done' when finished.")
    course_slots = {}
    while True:
        entry = input("Enter course and slot: ").strip()
        if entry.lower() == "done":
            break
        try:    
            course, slot = entry.split(":")
            slot = slot.upper().strip()
            course = course.strip()
            if slot not in "ABCDEFGPQRSTU":
                print(f"Invalid slot: {slot}. Please use valid slots A to G or P to S.")
                continue
            course_slots[slot] = course
        except ValueError:
            print("Invalid format. Please use <Course>:<Slot>.")
    # This code does the following
    # Populate the timetable based on course_slots
    slot_to_index = {
        "A": 0, "B": 1, "C": 2, "D": 3,
        "P": 5, "Q": 6
    }
    day_slot_map = {
        "Monday": ["A", "B", "C", "D", "P", "Q"],
        "Tuesday": ["D", "E", "F", "G", "R", "S"],
        "Wednesday": ["B", "C", "A", "G", "F"],
        "Thursday": ["C", "A", "B", "E", "Q", "P"],
        "Friday": ["E", "F", "D", "G", "S", "R"]
    }
    
    for day, day_slots in day_slot_map.items():
        for slot in day_slots:
            if slot in course_slots:
                index = slot_to_index.get(slot, None)
                if index is not None:
                    timetable[day][index] = course_slots[slot]

    # Convert the timetable to a DataFrame for a better view
    timetable_df = pd.DataFrame(timetable, index=slots)
    print("\nGenerated Timetable:")
    print(timetable_df)

    # Save the timetable to a CSV file
    timetable_df.to_csv("generated_timetable.csv")
    print("\nTimetable saved as 'generated_timetable.csv'.")

# Run the function
generate_timetable()
