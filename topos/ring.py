#!/usr/bin/python

import os, sys
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel, info, debug
from mininet.node import Host, RemoteController

class TreeTopo( Topo ):
    "Tree topology"

    def build( self ):
        # Read ring.in
        # Load configuration of Hosts, Switches, and Links
        # You can write other functions as you need.
        lines = []
        with open('ring.in') as f:
            lines = [line.strip() for line in f]
        no_hosts, no_switches = list(map(int, lines[0].split()))
        links = [(line.split()[0], line.split()[0]) for line in lines[1:]]

        # Add hosts
        # > self.addHost('h%d' % [HOST NUMBER])
        for i in range(1, no_hosts + 1):
            self.addHost('h%d' % i)

        # Add switches
        # > sconfig = {'dpid': "%016x" % [SWITCH NUMBER]}
        # > self.addSwitch('s%d' % [SWITCH NUMBER], **sconfig)
        for i in range(1, no_switches + 1):
            sconfig = {'dpid': '%016x' % i}
            self.addSwitch('s%d' % i, **sconfig)

        # Add links
        # > self.addLink([HOST1], [HOST2])
        for node1, node2 in links:
            self.addLink(node1, node2)
        
                    
topos = { 'sdnip' : ( lambda: TreeTopo() ) }

if __name__ == '__main__':
    sys.path.insert(1, '/home/sdn/onos/topos')
    from onosnet import run
    run( TreeTopo() )