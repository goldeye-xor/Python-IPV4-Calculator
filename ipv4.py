# demander l'ip
ip = input("Entrez l'ip (1.1.1.1/8) : ")
# cidr = ip apres le /
cidr = ip.split("/")[1]
ip = ip.split("/")[0]

def ip_to_bin(ip):
    # Cette fonction convertit une ip en binaire
    ip_bin = ""
    for i in ip.split("."):
        ip_bin += "{0:08b}".format(int(i))
    return ip_bin

ip_bin = ip_to_bin(ip)

def getclass(ip):
    # Cette fonction retourne la classe de l'ip
    # si la premiere bit est 0, la classe est A
    if ip[0] == "0":
        return "A"
    # si la premiere bit est 10, la classe est B
    elif ip[0] == "1" and ip[1] == "0":
        return "B"
    # si la premiere bit est 110, la classe est C
    elif ip[0] == "1" and ip[1] == "1" and ip[2] == "0":
        return "C"
    # si la premiere bit est 1110, la classe est D
    elif ip[0] == "1" and ip[1] == "1" and ip[2] == "1" and ip[3] == "0":
        return "D"
    # si la premiere bit est 1111, la classe est E
    elif ip[0] == "1" and ip[1] == "1" and ip[2] == "1" and ip[3] == "1":
        return "E"

ip_class = getclass(ip_bin)

def cidr_to_bin(cidr):
    # Cette fonction convertit un cidr en binaire et la retourne en string
    cidr_bin = ""
    for i in range(int(cidr)):
        cidr_bin += "1"
    for i in range(32 - int(cidr)):
        cidr_bin += "0"
    return cidr_bin

cidr_bin = cidr_to_bin(cidr)

def net_addr(ip_bin, cidr_bin):
    # Cette fonction retourne l'adresse de la network
    net_addr = ""
    for i in range(0, 32):
        if cidr_bin[i] == "1":
            # on ajoute le bit de l'ip
            net_addr += ip_bin[i]
        else:
            # on ajoute le bit de l'cidr
            net_addr += cidr_bin[i]
    return net_addr

ip_net_bin = net_addr(ip_bin, cidr_bin)

def bin_to_ip(ip):
    # Cette fonction convertit une ip binaire en ip et la retourne en string
    ip_str = ""
    for i in range(0, 32, 8):
        ip_str += str(int(ip[i:i+8], 2)) + "."
    return ip_str[:-1]

ip_net = bin_to_ip(ip_net_bin)

def ip_brc(ip_bin, cidr_bin):
    # Cette fonction retourne l'adresse de la broadcast
    ip_brc = ""
    for i in range(0, 32):
        if cidr_bin[i] == "1":
            # on ajoute le bit de l'ip
            ip_brc += ip_bin[i]
        else:
            # on ajoute le bit de l'cidr
            ip_brc += "1"
    return ip_brc

ip_brc_bin = ip_brc(ip_bin, cidr_bin)
ip_brc = bin_to_ip(ip_brc_bin)

def ip_range_s(ip_bin, cidr_bin):
    # Cette fonction retourne la première adresse de la plage d'adresses
    ip_range_s = ""
    for i in range(0, 32):
        if cidr_bin[i] == "1":
            # on ajoute le bit de l'ip
            ip_range_s += ip_bin[i]
        else:
            if i == 31:
                # on ajoute le bit de l'cidr
                ip_range_s += "1"
            else:
                # on ajoute le bit de l'cidr
                ip_range_s += "0"

    return ip_range_s

ip_range_s_bin = ip_range_s(ip_bin, cidr_bin)
ip_range_s = bin_to_ip(ip_range_s_bin)

def ip_range_e(ip_bin, cidr_bin):
    # Cette fonction retourne la dernière adresse de la plage d'adresses
    ip_range_e = ""
    for i in range(0, 32):
        if cidr_bin[i] == "1":
            # on ajoute le bit de l'ip
            ip_range_e += ip_bin[i]
        else:
            if i == 31:
                # on ajoute le bit de l'cidr
                ip_range_e += "0"
            else:
                # on ajoute le bit de l'cidr
                ip_range_e += "1"

    return ip_range_e

ip_range_e_bin = ip_range_e(ip_bin, cidr_bin)
ip_range_e = bin_to_ip(ip_range_e_bin)

def ip_priv(ip_bin):
    # Cette fonction retourne si l'ip est privé
    if ip_bin[0:8] == "01111111":
        return "Loopback"
    # si les 8 premiers bits forme 10
    elif ip_bin[0:8] == "00001010":
        return "Prive"
    elif ip_bin[0:12] == "101011000001":
        return "Prive"
    elif ip_bin[0:16] == "1100000010101000":
        return "Prive"
    else :
        return "Public"

ip_priv = ip_priv(ip_bin)

mask = bin_to_ip(cidr_bin)

def reform_bin(bin):
    # cette fonction met un espace entre chaque octet
    bin_str = ""
    for i in range(0, 32, 8):
        bin_str += bin[i:i+8] + " "
    return bin_str[:-1]

ip_bin = reform_bin(ip_bin)
cidr_bin = reform_bin(cidr_bin)
ip_net_bin = reform_bin(ip_net_bin)
ip_brc_bin = reform_bin(ip_brc_bin)
ip_range_s_bin = reform_bin(ip_range_s_bin)
ip_range_e_bin = reform_bin(ip_range_e_bin)

print("------- Bin ---------------------------------------------")
print("@           :", ip_bin)
print("Mask        :", cidr_bin)
print("@ net       :", ip_net_bin)
print("@ broadcast :", ip_brc_bin)
print("First @     :", ip_range_s_bin)
print("Last @      :", ip_range_e_bin)
print("------- Address ---------------------------------------------")
print("@           :", ip)
print("Classe      :", ip_class)
print("CIDR        :", cidr)
print("Mask        :", mask)
print("Type        :", ip_priv)
print("------- Network ---------------------------------------------")
print("@ net       :", ip_net)
print("@ broadcast :", ip_brc)
print("First @     :", ip_range_s)
print("Last @      :", ip_range_e)





