from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
class CustTop(Topo):   
    def build(self):
        # Add switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        # Add hosts
        h1 = self.addHost('h1', ip='192.76.0.1/24')
        h2 = self.addHost('h2', ip='192.76.0.2/24')
        h3 = self.addHost('h3', ip='192.76.0.3/24')
        h4 = self.addHost('h4', ip='192.76.0.4/24')

        # Add links with specified properties
        self.addLink(h1, s1, bw=15, delay='10ms')
        self.addLink(h2, s1, bw=15, delay='10ms')
        self.addLink(h3, s2, bw=15, delay='10ms')
        self.addLink(h4, s2, bw=15, delay='10ms')
        self.addLink(s1, s2, bw=20, delay='45ms')
# Create an instance of the topology
topo=CustTop()
# Create Mininet network with custom topology and link settings
net = Mininet(topo=topo, link=TCLink)
# Start the network
net.start()
# Open Mininet CLI for interaction
net.interact()
