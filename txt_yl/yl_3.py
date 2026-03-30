def right_score(wrong_score, correction) ->float:
    return wrong_score + correction / 100


file_name = input("Sisesta faili nimi: ")
correction = float(input("Sisesta parandus sentimeetrites: "))

wrong_scores = []
with open (file_name, "r") as f:
    for line in f:
        wrong_scores.append((float(line.strip())))

corrected_score = []
for score in wrong_scores:
    corrected_score.append(right_score(score, correction))


print("Õiged tulemused")
for t in corrected_score:
    print(f"{t:.2f}")

normative = float(input("Sisesta normatiiv meetrites: "))

qualified = [t for t in corrected_score if t >= normative]

print(f"Normatiivi täitis {len(qualified)} võistlejat.")

if qualified:
    average = sum(qualified) / len(qualified)
    print(f"Kvalifitseerunute keskmine on {average:.2f}")