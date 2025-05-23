def get_raw_packet_4_tcp_http():
    # Paquete de ejemplo (Ethernet + IPv4 + TCP + HTTP)
    raw_packet_4_tcp_http = (
        b'\x00\x0c\x29\x12\x34\x56\x00\x0c\x29\xab\xcd\xef\x08\x00'  # Ethernet
        b'\x45\x00\x00\x3c\x00\x00\x40\x00\x40\x06\x00\x00\xc0\xa8\x01\x01\x93\x18\xd8\x22'  # IPv4
        b'\xd4\x31\x00\x50\x00\x00\x00\x00\x00\x00\x00\x00'  # TCP
        b'GET /index.html HTTP/1.1\r\nHost: example.com\r\n\r\n'  # HTTP
    )
    
def get_raw_packet_6_udp_dns():
    # Paquete IPv6 + UDP + DNS
    raw_packet_6_udp_dns = (
        b'\x00\x0c\x29\x12\x34\x56\x00\x0c\x29\xab\xcd\xef\x86\xdd'  # Ethernet (IPv6)
        b'\x60\x00\x00\x00\x00\x48\x11\xff\xfe\x80\x00\x00\x00\x00\x00\x00'  # IPv6
        b'\x02\x0c\x29\xff\xfe\xab\xcd\xef\x20\x01\x48\x60\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x01'  # Direcciones IP
        b'\x02\x22\x00\x35\x00\x48\x00\x00'  # UDP (puerto 53)
        b'\x2e\xf0\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x07\x65\x78\x61'  # DNS
        b'\x6d\x70\x6c\x65\x03\x63\x6f\x6d\x00\x00\x01\x00\x01'
    )

def get_raw_packet_6_tcp_http():
    # Ethernet (IPv6) + IPv6 + TCP + HTTP
    raw_packet_6_tcp_http = (
        # Ethernet (dest_mac, src_mac, ethertype=0x86DD)
        b'\x00\x0c\x29\x12\x34\x56\x00\x0c\x29\xab\xcd\xef\x86\xdd'
        # IPv6 (version=6, next_header=6=TCP)
        b'\x60\x00\x00\x00\x00\x24\x06\xff\x20\x01\x0d\xb8\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x01\x20\x01\x0d\xb8\x00\x00\x00\x00'
        b'\x00\x00\x00\x00\x00\x00\x00\x02'
        # TCP (src_port=54321, dst_port=80)
        b'\xd4\x31\x00\x50\x00\x00\x00\x00\x00\x00\x00\x00\x50\x02\xff\xff'
        b'\x00\x00\x00\x00'
        # HTTP
        b'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n'
    )
    
def get_raw_packet_4_tcp_http_2():
    #Paquete de Prueba (Ethernet + IPv4 + TCP + HTTP)
    raw_packet = (
        # Ethernet (14 bytes)
        b'\x00\x0c\x29\x12\x34\x56'  # Destino MAC: 00:0c:29:12:34:56
        b'\x00\x0c\x29\xab\xcd\xef'  # Origen MAC: 00:0c:29:ab:cd:ef
        b'\x08\x00'                  # EtherType: 0x0800 (IPv4)

        # IPv4 (20 bytes)
        b'\x45\x00\x00\x54'          # Versión 4, IHL=5, Longitud total=84
        b'\x00\x00\x40\x00'          # ID=0, Flags=DF, Offset=0
        b'\x40\x06\x00\x00'          # TTL=64, Protocolo=6 (TCP), Checksum=0 (simplificado)
        b'\xc0\xa8\x01\x01'          # IP Origen: 192.168.1.1
        b'\x93\x18\xd8\x22'          # IP Destino: 147.24.216.34 (ejemplo.com)

        # TCP (20 bytes + opciones)
        b'\xd4\x31\x00\x50'          # Puerto Origen=54321, Destino=80 (HTTP)
        b'\x00\x00\x00\x00'          # Número de secuencia
        b'\x00\x00\x00\x00'          # Número de ACK
        b'\x50\x02\xff\xff'          # Longitud cabecera=20, Flags=SYN
        b'\x00\x00\x00\x00'          # Ventana=65535, Checksum=0 (simplificado)

        # HTTP (24 bytes)
        b'GET / HTTP/1.1\r\n'        # Petición HTTP
        b'Host: example.com\r\n\r\n'  # Cabecera Host + doble CRLF
    )