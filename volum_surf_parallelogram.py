#!/usr/bin/env python3
# Created By: Sam V
# Date: Oct 10th, 2026
# Calculates the height of a parallelogram from its area and base.

import math


def calculate_height():
    print("--- Parallelogram Height Calculator ---")

    try:
        area = float(input("Enter the area of the parallelogram: "))
        base = float(input("Enter the base length of the parallelogram: "))
    except ValueError:
        print("Error: Please enter valid numbers.")
        return

    if not math.isfinite(area) or not math.isfinite(base):
        print("Error: Area and base must be finite numbers.")
        return

    if area < 0:
        print("Error: Area cannot be negative.")
        return

    if base <= 0:
        print("Error: Base must be greater than zero.")
        return

    # Calculate height: h = area / base
    height = area / base

    print("\n--- Results ---")
    print(f"Area:   {area:.2f}")
    print(f"Base:   {base:.2f}")
    print(f"Height: {height:.2f}")


if __name__ == "__main__":
    calculate_height()
