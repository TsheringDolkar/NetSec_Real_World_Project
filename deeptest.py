import socket
s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW,socket.ntohs(0x0800))
i = 1



pkt = s.recvfrom(2048)
num = pkt[0][14].encode('hex')
ip_length = (int(num) % 10) * 4
ip_last_range = 14 + ip_length
ipheader = pkt[0][14:ip_last_range]
ip_hdr = struct.unpack("!12s4s4s",ipheader)
server_ip = socket.inet_ntoa(ip_hdr[1])
obtained_ip = socket.inet_ntoa(ip_hdr[2])



print("Obtained IP ",obtained_ip)
print("DHCP server IP ",server_ip)
dhcp_request = eth1/ip1/udp1/bootp1/dhcp2
dhcp_request[BOOTP].xid= 123456
name='master'+str(i)


i =i+1
dhcp_request[DHCP].options.append(("requested_addr", obtained_ip))
dhcp_request[DHCP].options.append(("server_id", server_ip))
dhcp_request[DHCP].options.append(("hostname", name))
dhcp_request[DHCP].options.append(("param_req_list",
b'x01x1cx02x03x0fx06x77x0cx2cx2fx1ax79x2a'))
dhcp_request[DHCP].options.append(("end"))


