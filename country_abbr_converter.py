import pycountry

def main():
	print("There are {0} countries in total".format(len(pycountry.countries)))

	write_str = ""

	# Import csv file
	data_path = "filenaja.csv"
	with open(data_path) as f:
		lines = f.readlines()

		# Header
		write_str += lines[0].strip() + ",Country (Full)\n"

		for line in lines[1:]:
			line = line.strip()
			
			# Convert
			abbr = line.split(',')[7].upper()
			try:
				country_name = pycountry.countries.get(alpha_2=abbr).name
				print("From {0} to {1}".format(abbr, country_name))

				write_str += line + "," + country_name + '\n'

			except Exception as e:
				print("Exception with abbr: " + abbr)
				write_str += line + "," + '\n'	# Write empty

	write_file = "country_converted.csv"
	with open(write_file, 'w') as f:
		f.write(write_str)

if __name__ == "__main__":
	main()