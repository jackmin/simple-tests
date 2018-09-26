server='10.12.205.223'
workdir='/labhome/jackmin/Works/dpdk.jackmin/ofed4.5'
cmd='sudo ./app/testpmd -l 5,7 -w 81:00.1,representor=\[0,1\] -n 4 --proc-type=primary  -- --forward-mode=rxonly -i --auto-start --flow-isolate-all'
tests=[
        ('flow create 0 ingress pattern eth / ipv4 / udp dst is 7000 / end actions set_mac_dst mac_addr dd:00:aa:11:bb:33 / set_mac_src mac_addr bb:00:cc:11:aa:22 / set_ipv4_src ipv4_addr 172.168.0.1 / set_ipv4_dst ipv4_addr 172.168.10.1 / set_tp_dst port 9000 / set_tp_src port 700 / queue index 0 / end', 'created'),
        ('flow create 0 ingress pattern eth / ipv4 / udp / end actions set_mac_dst mac_addr dd:00:aa:11:bb:33 / set_mac_src mac_addr bb:00:cc:11:aa:22 / set_ipv4_src ipv4_addr 172.168.0.1 / set_ipv4_dst ipv4_addr 172.168.10.1 / set_tp_dst port 9000 / set_tp_src port 700 / set_ttl ttl_value 0x10 / queue index 0 / end', 'created'),
        ('flow create 0 ingress pattern eth / ipv6 / udp / end actions set_mac_dst mac_addr dd:00:aa:11:bb:33 / set_ipv4_dst ipv4_addr 172.168.0.1 / queue index 0 / end', 'no ipv4 item in pattern'),
        ('flow create 0 ingress pattern eth / ipv4 / udp / end actions set_mac_dst mac_addr dd:00:aa:11:bb:33 / set_ipv6_dst ipv6_addr ::1234 / queue index 0 / end', 'no ipv6 item in pattern'),
        ('flow create 0 ingress pattern eth / ipv4 / end actions set_mac_dst mac_addr dd:00:aa:11:bb:33 / set_ipv4_dst ipv4_addr 172.168.0.1 / set_tp_dst port 9000 / queue index 0 / end', 'no transport layer in pattern'),
        ('flow create 0 ingress pattern eth / ipv4 / end actions set_mac_dst mac_addr dd:00:aa:11:bb:33 / set_ipv4_dst ipv4_addr 172.168.0.1 / vxlan_l3_decap / queue index 0 / end', 'action confilicts'),
        ('flow create 0 ingress pattern eth / ipv4 / udp dst is 4789 / vxlan / eth / ipv4 / udp dst is 7099 / end actions set_mac_dst mac_addr dd:00:aa:11:bb:33 / set_ipv4_dst ipv4_addr 172.168.0.1 / vxlan_decap / queue index 0 / end', 'decap must before modify'),
        ('flow create 0 ingress pattern eth / ipv4 / end actions set_ipv4_dst ipv4_addr 172.168.0.1 / vxlan_l3_decap / queue index 0 / end', 'after decap no ipv4 item in pattern'),
        ('flow create 0 ingress pattern eth / ipv4 / udp dst is 250 / vxlan / ipv4 / udp dst is 7100 / end actions set_ipv4_dst ipv4_addr 172.168.0.1 / vxlan_l3_decap / queue index 0 / end', 'decap must before modify'),
        ('flow create 0 ingress pattern eth / ipv4 / udp dst is 250 / vxlan / ipv4 / udp dst is 7100 / end actions vxlan_l3_decap / set_ipv4_dst ipv4_addr 172.168.0.1 / queue index 0 / end', 'created'),
	]
