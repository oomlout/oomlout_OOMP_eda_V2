
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Ethernet"
    oIndex = "W5100"
    hexID = "SZKINTERFACEETHERNETW51"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'W5100', 'kicadSymbolFootprint': 'Package_QFP:LQFP-80_10x10mm_P0.4mm', 'kicadSymbolDatasheet': 'http://www.wiznet.io/wp-content/uploads/wiznethome/Chip/W5100/Document/W5100_Datasheet_v1.2.7.pdf', 'kicadSymbolki_keywords': 'Wiznet Ethernet controller', 'kicadSymbolki_description': '10/100Mb Ethernet controller with TCP/IP stack, LQFP-80', 'kicadSymbolki_fp_filters': 'LQFP*10x10mm*P0.4mm*'}])
    newPart['name'].append('Interface_Ethernet : W5100')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

