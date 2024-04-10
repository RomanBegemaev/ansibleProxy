import subprocess
import json

# Запрос ввода IP адресов серверов, разделенных запятыми
ip_addresses = input("Enter server IP addresses: ")
ip_list = [ip.strip() for ip in ip_addresses.split()]

# Запрос ввода доменных имен серверов, разделенных запятыми
domains = input("Enter server domain names: ")
domain_list = [domain.strip() for domain in domains.split()]

# Проверка, что количество IP адресов и доменных имен совпадает
if len(ip_list) != len(domain_list):
    print("Error: Number of IP addresses and domain names should match.")
    exit(1)

inventory = {
    'all': {
        'hosts': {}
    }
}

# Добавление IP-адресов и доменных имен в инвентарь
for i in range(len(ip_list)):
    inventory['all']['hosts'][ip_list[i]] = {
        'ansible_host': ip_list[i],
        'domain': domain_list[i]
    }

# Запись инвентаря в файл
with open('dynamic_inventory.json', 'w') as file:
    json.dump(inventory, file, indent=4)

print("Dynamic inventory has been created successfully.")



# Команда для запуска плейбука с указанием инвентаря и дополнительных переменных
command = f'ansible-playbook -i {"./dynamic_inventory.json"} {"nginxConf.yml"} '

# Запуск команды субпроцессом
process = subprocess.Popen(command, shell=True)
process.wait()