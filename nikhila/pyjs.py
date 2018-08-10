import json
with open('show_data.json', 'r') as f:
	distros_dict = json.load(f)

for distro in distros_dict:
    print(distro['title'])
	

   
                    

