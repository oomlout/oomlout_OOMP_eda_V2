
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Ethernet"
    oIndex = "ENC424J600-PT"
    hexID = "SZKINTERFACEETHERNETENC424J6PT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ENC424J600-PT', 'kicadSymbolFootprint': 'Package_QFP:TQFP-44_10x10mm_P0.8mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/39935c.pdf', 'kicadSymbolki_keywords': 'ENC Ethernet', 'kicadSymbolki_description': 'Stand-Alone 10/100 Ethernet Controller with SPI or Parallel Interface, TQFP-44', 'kicadSymbolki_fp_filters': 'TQFP*44*10x10mm*P0.8mm*'}])
    newPart['name'].append('Interface_Ethernet : ENC424J600-PT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

