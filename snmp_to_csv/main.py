from functions import get_network_traffic, get_name

# Segun la plataforma, habra que colocar
# el path absoluto en el nombre del archivo
get_network_traffic('hosts.json', 'in')
get_network_traffic('hosts.json', 'out')
