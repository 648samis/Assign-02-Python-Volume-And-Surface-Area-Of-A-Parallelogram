#!/usr/bin/env python3
# Created By: Sam V
# Date: Oct 10th, 2026
# base and area of a parallelogram and calculates the height.
# of a parallelogram and calculates the area and perimeter of the parallelogram.

def calculate_height():
    print("--- Parallelogram Height Calculator ---")

    area = float(input("Enter the area of the parallelogram: "))
    base = float(input("Enter the base length of the parallelogram: "))
    
    if base <= 0:
        print("Error: Base must be greater than zero.")
        return

    # Calculate Height: h = area / base
    height = area / base
    
    print("\n--- Results ---")
    print(f"Area:   {area:.2f}")
    print(f"Base:   {base:.2f}")
    print(f"Height: {height:.2f}")

if __name__ == "__main__":
    calculate_height()