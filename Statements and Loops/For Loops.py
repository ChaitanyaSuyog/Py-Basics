
cards = ["GTX 1080Ti", "RTX 3090", "RX6900 XT"]
for model in cards:
    print(model)

for index in range(2, 5):
    print(index)

for model in range(len(cards)):
    if model == 0:
        print("First iteration.")
    else:
        print("Not first.")
