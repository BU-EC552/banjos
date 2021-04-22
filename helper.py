import json
import csv

''' Function used to parse the input.json from celloapi2
    input: full path of input.json file'''
def parseInput(filename):
    data = None
    with open(filename) as f:
        data = json.load(f)

    data_parse = {}
    for idx in range(len(data)):
        # If collection == "models", there are ymin, ymax, alpha, and beta
        if data[idx]['collection'] == 'models':
            info = []
            for val_idx, val in enumerate(data[idx]['parameters']):
                info.append(val)

            key = str(data[idx]['name'])
            data_parse[key] = info


    ######## Example of data_parse output ########
    # 'LacI_sensor_model': 
    #     [{'name': 'ymax', 'value': 2.8, 'description': 'Maximal transcription'}, 
    #     {'name': 'ymin', 'value': 0.0034, 'description': 'Minimal transcription'}, 
    #     {'name': 'alpha', 'value': 0.73, 'description': 'Tandem parameter'}, 
    #     {'name': 'beta', 'value': 0.04, 'description': 'Tandem parameter'}]
    return data_parse
######################################################################


'''readXMLparts function. Used to parse the XML parts file for the part_name and dna sequence
input: full path to xml file'''
def readXMLparts(filename):
    file1 = open('xml_parts.xml', 'r')
    Lines = file1.readlines()

    parts = {}
    
    # Strips the newline character
    count = 0
    partName = None
    for line in Lines:
        if "<field name=\"part_name\">" in line.strip():
            str1 = line.strip()
            c1 = str1.find(">")
            c2 = c1
            while str1[c2] != "<":
                c2 += 1

            partName = str1[c1+1:c2]

        elif "<field name=\"sequence\">" in line.strip():
            if partName != None:
                str1 = line.strip()
                c1 = str1.find(">")
                c2 = c1
                while str1[c2] != "<":
                    c2 += 1

                parts[partName] = str1[c1+1:c2]
                partName = None

    return parts


''' Function used to find the GC content
input: string-> DNA sequence '''
def GC_function(DNA_sequence):
	length = len(DNA_sequence)
	A_count = 0
	G_count = 0
	T_count = 0
	C_count = 0
	#print(length)
	for i in range(length):
		if DNA_sequence[i] == "A":
			A_count = A_count + 1

		elif DNA_sequence[i] == "G":
			G_count = G_count + 1

		elif DNA_sequence[i] == "T":
			T_count = T_count + 1 

		elif DNA_sequence[i] == "C":
			C_count = C_count + 1


	print("Number of A's: {}" .format(A_count))
	print("Number of G's: {}" .format(G_count))
	print("Number of T's: {}" .format(T_count))
	print("Number of C's: {}" .format(C_count))
	print("The total number of bases is: {}." .format(length))

	GC_content = ((G_count+C_count)/length)*100
	print("The GC content is {}" .format(GC_content))

	return GC_content