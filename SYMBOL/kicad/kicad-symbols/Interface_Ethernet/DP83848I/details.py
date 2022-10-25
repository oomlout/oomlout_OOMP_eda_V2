
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Ethernet"
    oIndex = "DP83848I"
    hexID = "SZKINTERFACEETHERNETDP83848I"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'DP83848C', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DP83848I', 'kicadSymbolFootprint': 'Package_QFP:LQFP-48_7x7mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/dp83848c.pdf', 'kicadSymbolki_keywords': 'Ethernet PHY MII RMII 10/100Mpbs', 'kicadSymbolki_description': 'MII/RMII Single 10/100Mbps Ethernet Physical Layer Transceiver, LQFP-48', 'kicadSymbolki_fp_filters': 'LQFP*7x7mm*P0.5mm*'}])
    newPart['name'].append('Interface_Ethernet : DP83848I')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

