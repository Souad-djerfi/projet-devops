#!/bin/bash

#  les adresses IP des machines virtuelles à tester
# déclarer une variable système dans /etc/environment vm_ips=("192.168.56.10" "192.168.56.11" "192.168.56.12")

# Boucle sur les adresses IP des machines virtuelles
for vm_ip in "${vm_ips[@]}"; do
  # Utilisez la commande ping pour tester la connexion
  ping -c 4 $vm_ip

  # Vérifiez la sortie de la commande ping pour déterminer si la connexion est réussie
  if [ $? -eq 0 ]; then
    echo "La machine virtuelle $vm_ip est joignable"
  else
    echo "La machine virtuelle $vm_ip n'est pas joignable, demarrage"
    cd vagrant
    vagrant up $vm_ip
  fi
done
