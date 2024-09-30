import pulp

# Define the decision variables for the five food items
food_items = ['Oats', 'Oatmilk', 'PeanutButter', 'Spinach', 'Salmon']
costs = {'Oats': 0.25, 'Oatmilk': 0.70, 'PeanutButter': 0.18, 'Spinach': 0.56, 'Salmon': 1.16}
nutrition = {
    'Energy': {'Oats': 150, 'Oatmilk': 120, 'PeanutButter': 190, 'Spinach': 30, 'Salmon': 100},
    'Protein': {'Oats': 5, 'Oatmilk': 3, 'PeanutButter': 8, 'Spinach': 3, 'Salmon': 17},
    'Sodium': {'Oats': 0, 'Oatmilk': 140, 'PeanutButter': 120, 'Spinach': 80, 'Salmon': 260},
    'VitaminD': {'Oats': 0, 'Oatmilk': 3.6, 'PeanutButter': 0, 'Spinach': 0, 'Salmon': 15.9},
    'Calcium': {'Oats': 0, 'Oatmilk': 350, 'PeanutButter': 0, 'Spinach': 130, 'Salmon': 200},
    'Iron': {'Oats': 1.7, 'Oatmilk': 0, 'PeanutButter': 0.5, 'Spinach': 1.7, 'Salmon': 0.4},
    'Potassium': {'Oats': 140, 'Oatmilk': 390, 'PeanutButter': 200, 'Spinach': 260, 'Salmon': 280}
}

# Define the problem
prob = pulp.LpProblem("PersonalizedDiet", pulp.LpMinimize)

# Define the decision variables
servings = pulp.LpVariable.dicts("Servings", food_items, lowBound=1, cat='Continuous')

# Define the objective function to minimize the cost
prob += pulp.lpSum([costs[i] * servings[i] for i in food_items]), "Total Cost"

# Define the weekly nutritional constraints
prob += pulp.lpSum([nutrition['Energy'][i] * servings[i] for i in food_items]) >= 2000 * 7, "Energy"
prob += pulp.lpSum([nutrition['Protein'][i] * servings[i] for i in food_items]) >= 50 * 7, "Protein"
prob += pulp.lpSum([nutrition['Sodium'][i] * servings[i] for i in food_items]) <= 5000 * 7, "Sodium"
prob += pulp.lpSum([nutrition['VitaminD'][i] * servings[i] for i in food_items]) >= 20 * 7, "VitaminD"
prob += pulp.lpSum([nutrition['Calcium'][i] * servings[i] for i in food_items]) >= 1300 * 7, "Calcium"
prob += pulp.lpSum([nutrition['Iron'][i] * servings[i] for i in food_items]) >= 18 * 7, "Iron"
prob += pulp.lpSum([nutrition['Potassium'][i] * servings[i] for i in food_items]) >= 4700 * 7, "Potassium"

# Solve the linear programming problem
prob.solve()

# Print the solution with serving sizes and minimum cost
print("Status:", pulp.LpStatus[prob.status])
print("Minimum Cost: ${:.2f}".format(pulp.value(prob.objective)))
for v in prob.variables():
    print("{}: {:.2f} servings".format(v.name, v.varValue))
