# projectrefuge-dietproblemrev11

## Personalized Diet Problem

This repository contains a linear programming model to construct a personalized diet using current recommended dietary allowances from the U.S. Food and Drug Administration, updated to account for recent research on sodium intake and health.

### Problem Description

The constraints for this linear programming problem consider seven components of nutrition and their daily values, as shown in the following table:

| Component | Max/Min | Daily Amount and Measure |
|-----------|---------|--------------------------|
| Sodium    | Maximum | 5,000 milligrams (mg)    |
| Energy    | Minimum | 2,000 Calories (kilocalories, kcal) |
| Protein   | Minimum | 50 grams (g)             |
| Vitamin D | Minimum | 20 micrograms (mcg)      |
| Calcium   | Minimum | 1,300 milligrams (mg)    |
| Iron      | Minimum | 18 milligrams (mg)       |
| Potassium | Minimum | 4,700 milligrams (mg)    |

The problem is set up as a standard linear programming problem with decision variables taking any non-negative values. Partial servings are permitted. The nutritional constraints are set to satisfy a weekly diet by multiplying each daily requirement by seven (7).

### Food Items

To adapt the problem to a personal diet, nutrition facts from five packaged food items are collected. The goal is to find the minimum-cost diet that satisfies the nutritional requirements.

### Running the Script

To run the linear programming model, follow these steps:

1. Ensure you have Python and the PuLP library installed. You can install PuLP using pip:
   ```
   pip install pulp
   ```

2. Run the `diet_problem.py` script:
   ```
   python diet_problem.py
   ```

The script will output the solution with serving sizes and the minimum cost to satisfy the nutritional 