import yaml
import csv

with open('config.csv', 'r') as f:
    reader = csv.DictReader(f)
    data = []
    for row in reader:
        item = {}
        item['hostname'] = row['hostname']
        inters = []
        inter={}
        inter['InterfaceType'] = row['InterfaceType']
        inter['InterfaceIP'] = row['InterfaceIP']
        inter['ProcessID'] = int(row['ProcessID'])
        inter['ospfArea'] = row['ospfArea'].strip()
        inters.append(inter)
        item['inters'] = inters
        data.append(item)

output_data = {'test_router': data}

with open('/etc/ansible/lab_template/roles/router/vars/main.yml', 'w') as f:
    f.write('---\n')
    yaml.dump(output_data, f)