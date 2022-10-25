
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Ethernet"
    oIndex = "ENC28J60x-SS"
    hexID = "SZKINTERFACEETHERNETENC28J6XSS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ENC28J60x-SS', 'kicadSymbolFootprint': 'Package_SO:SSOP-28_5.3x10.2mm_P0.65mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/39662e.pdf', 'kicadSymbolki_keywords': 'ENC Ethernet', 'kicadSymbolki_description': 'ENC28J60 Single Chip Ethernet Interface, SSOP-28', 'kicadSymbolki_fp_filters': 'SSOP*28*5.3x10.2mm*P0.65mm*'}])
    newPart['name'].append('Interface_Ethernet : ENC28J60x-SS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

