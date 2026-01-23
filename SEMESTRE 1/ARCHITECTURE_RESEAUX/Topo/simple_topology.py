from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def simpleTopology():
    "Création d'une topologie simple"
    net = Mininet(controller=Controller)

    info('*** Ajout du contrôleur\n')
    net.addController('c0')

    info('*** Ajout des hôtes\n')
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')

    info('*** Ajout du commutateur\n')
    s1 = net.addSwitch('s1')

    info('*** Création des liens\n')
    net.addLink(h1, s1)
    net.addLink(h2, s1)

    info('*** Démarrage du réseau\n')
    net.start()

    info('*** Exécution de la CLI\n')
    CLI(net)

    info('*** Arrêt du réseau\n')
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    simpleTopology()