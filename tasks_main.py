import yaml

data = [{'name': 'Generate configuration files',
         'hosts': 'all',
         'with_items': '{{ test_router}}'}]

with open('/etc/ansible/lab_template/roles/router/tasks/main.yml', 'w') as f:
    f.write('---\n')
    yaml.dump(data, f, default_flow_style=False):