notes = ["C0", "C#0", "D0", "D#0", "E0", "F0", "F#0", "G0", "G#0", "A0", "A#0", "B0",
 "C1", "C#1", "D1", "D#1", "E1", "F1", "F#1", "G1", "G#1", "A1", "A#1", "B1",
 "C2", "C#2", "D2", "D#2", "E2", "F2", "F#2", "G2", "G#2", "A2", "A#2", "B2",
 "C3", "C#3", "D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3", "A#3", "B3",
 "C4"]
def subharmonic_finder(fundamental):
    i = notes.index(fundamental)
    subharmonic = int(input("which subharmonic do u wanna see: "))
    drop = 12 + (subharmonic - 1)*6
    sub = notes[i-drop]
    print(f"your subharmonic drops {drop} semitones and should be a {sub}")
while True:
    fundamental = input("enter your fundamental note (or 'quit' to exit): ").upper()
    if fundamental == "QUIT":
        break
    if len(fundamental) == 2 or len(fundamental) == 3:
        valid_octave = False
        for number in "1234":
            if number in fundamental:
                if fundamental in notes:
                    subharmonic_finder(fundamental)
                else:
                    print("note not in range (C0 to C4)")
                valid_octave = True
                break
        if not valid_octave:
            print("invalid octave (must be 1-4)")
    else:
        print("invalid input format (e.g., C2 or C#3)")
