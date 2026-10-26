marks=int(input("Enter student marks:"))
if marks >= 90:
    print(f"Grade A (Marks={marks})")
elif marks >= 80:
    print(f"Grade B (marks={marks})")
elif marks >= 70:
    print(f"Grade C (marks={marks})")
else:
    print(f"Grade D (marks={marks})")