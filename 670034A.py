polygon  = {"Icosahedron":20,
"Cube":6,
"Tetrahedron":4,
"Dodecahedron":12,
"Octahedron":8}
total = 0
test = int(input())
for i in range(test):
  shap = input()
  total += polygon[shap]
print(total)