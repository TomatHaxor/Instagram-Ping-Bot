
import re


def separate_baik_benar(text: str):
	"""Return two lists: occurrences of 'baik' and 'benar' (case-insensitive)."""
	words = re.findall(r"\b(baik|benar)\b", text, flags=re.IGNORECASE)
	baik = [w for w in words if w.lower() == 'baik']
	benar = [w for w in words if w.lower() == 'benar']
	return baik, benar


def main():
	sample = "Baik dan benar. baik, BENAR! tidak baik sekali"
	baik, benar = separate_baik_benar(sample)
	print('baik:', baik)
	print('benar:', benar)


if __name__ == "__main__":
	main()
