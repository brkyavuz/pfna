from django.shortcuts import render
from .models import Host
from nornir import InitNornir
import yaml

def inventoryView(request):

    hosts_obj = Host.objects.all().values()

    hosts = {host["name"]:host for host in hosts_obj}
    with open("hosts.yaml", "w") as hosts_file:
        dumped = yaml.dump(hosts, hosts_file)

    nr = InitNornir()
    
    data = []

    for host in nr.inventory.hosts:
        host_dict = nr.inventory.hosts[host].dict()
        print(host_dict)
        device_data = [
            host_dict["name"],
            host_dict["hostname"],
            host_dict["platform"],
            ",".join(host_dict["groups"]),
            ",".join(host_dict["data"]),
            ",".join(host_dict["connection_options"])
        ]
        data.append(device_data)

    context = {
        "active_page":"inventory",
        "data": data
    }
    return render(request, 'views/inventory.html', context=context)
