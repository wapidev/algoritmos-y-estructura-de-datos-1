import re

texto = "l14kil5"
pattern = "[0-9]+"
# \d+ => encuentra números de uno o más dígitos
numeros = re.findall(pattern, texto)
# numeros = re.findall(r"\d+", texto)

print(numeros)  # ['14', '5']