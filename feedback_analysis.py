def positive(ratings):
    if not ratings:
        return "No ratings available"    
    positive = sum(1 for r in ratings if r >= 4)
    percentage = (positive / len(ratings)) * 100
    return round(percentage, 2)
ratings = []
n = int(input("Enter number of customer ratings: "))

for i in range(n):
    rating = int(input(f"Enter rating {i+1} (1-5): "))
    if 1 <= rating <= 5:
        ratings.append(rating)
    else:
        print("Invalid rating! Please enter between 1 and 5.")
        rating = int(input(f"Re-enter rating {i+1} (1-5): "))
        ratings.append(rating)
result = positive(ratings)
if isinstance(result, str):
    print(result)
else:
    print(f"Positive Feedback: {result}%")