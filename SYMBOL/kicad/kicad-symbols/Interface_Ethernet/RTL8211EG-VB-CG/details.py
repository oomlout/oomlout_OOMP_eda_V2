
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Ethernet"
    oIndex = "RTL8211EG-VB-CG"
    hexID = "SZKINTERFACEETHERNETRTL8211EGVBCG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'RTL8211EG-VB-CG', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-64-1EP_9x9mm_P0.5mm_EP3.8x3.8mm', 'kicadSymbolDatasheet': 'https://datasheet.lcsc.com/szlcsc/Realtek-Semicon-RTL8211EG-VB-CG_C69264.pdf', 'kicadSymbolki_keywords': 'Ethernet Phy Gigabit', 'kicadSymbolki_description': '10/100/1000Mbps Ethernet Transceiver with RGMII/GMII/MII/RMII Interface, QFN-64', 'kicadSymbolki_fp_filters': 'QFN*1EP*9x9mm*P0.5mm*'}])
    newPart['name'].append('Interface_Ethernet : RTL8211EG-VB-CG')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

