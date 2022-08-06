Zoo=["lion","tiger","deer","elephant","Rhino"]
# for animals in Zoo:
#     print(animals)

for animals in Zoo:
    if animals == "Dinosaurs":
        break
    if animals == "Rhino":
        break

else:
    print("This else statement is executed because FOR loop ended without break statement")