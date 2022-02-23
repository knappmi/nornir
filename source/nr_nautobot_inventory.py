
from nornir import InitNornir

def getInventory():
    nb_inv = InitNornir(
        inventory={
            "plugin" : "NautobotInventory",
            "options" : {
                "nautobot_url" : "https://192.168.128.15",
                "nautobot_token" : "1603955357328ffa4a08b6a7014dd866a2a8d5ba",
                "ssl_verify": False
            },
        },
    )

    print(nb_inv.inventory.hosts.keys())

getInventory()