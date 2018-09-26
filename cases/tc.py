server='10.12.205.224'
workdir='/labhome/jackmin/Works/dpdk.jackmin/build'
cmd='sudo ./app/dpdk-testpmd -l 5,7 -w 81:00.1,representor=\[0,1\] -n 4 --proc-type=primary  -- --forward-mode=rxonly -i --auto-start --flow-isolate-all'
tests=[
        ('flow create 0 transfer ingress pattern eth / ipv4 / udp dst is 7000 / end actions set_mac_dst mac_addr dd:00:aa:11:bb:33 / set_mac_src mac_addr bb:00:cc:11:aa:22 / set_ipv4_src ipv4_addr 172.168.0.1 / set_ipv4_dst ipv4_addr 172.168.10.1 / set_tp_dst port 9000 / set_tp_src port 700 / port_id id 1 / end', 'created'),
        ('flow create 0 transfer ingress pattern eth / ipv4 / udp dst is 7001 / end actions set_mac_dst mac_addr dd:00:aa:11:bb:33 / set_mac_src mac_addr bb:00:cc:11:aa:22 / dec_ttl / set_ipv4_dst ipv4_addr 172.168.10.1 / set_tp_dst port 9001 / port_id id 1 / end', 'created'),
        ('flow create 0 transfer ingress pattern eth / ipv4 / udp / end actions set_mac_dst mac_addr dd:00:aa:11:bb:33 / set_mac_src mac_addr bb:00:cc:11:aa:22 / set_ipv4_src ipv4_addr 172.168.0.1 / set_ipv4_dst ipv4_addr 172.168.10.1 / set_tp_dst port 9000 / set_tp_src port 700 / set_ttl ttl_value 0x10 / port_id id 1 / end', 'failed to create TC flow rule'),
        ('flow create 0 transfer ingress pattern eth / ipv6 / udp / end actions set_mac_dst mac_addr dd:00:aa:11:bb:33 / set_ipv4_dst ipv4_addr 172.168.0.1 / port_id id 1 / end', 'no ipv4 item found in pattern'),
        ('flow create 0 transfer ingress pattern eth / ipv4 / udp / end actions set_mac_dst mac_addr dd:00:aa:11:bb:33 / set_ipv6_dst ipv6_addr ::1234 / port_id id 1 / end', 'no ipv6 item found in pattern'),
        ('flow create 0 transfer ingress pattern eth / ipv4 / end actions set_mac_dst mac_addr dd:00:aa:11:bb:33 / set_ipv4_dst ipv4_addr 172.168.0.1 / set_tp_dst port 9000 / port_id id 1 / end', 'no TCP/UDP item found in pattern'),
        ]
