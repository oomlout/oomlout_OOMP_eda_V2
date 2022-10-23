
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "MAX490E"
    hexID = "SZKINTERFACEUARTMAX49E"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX488E', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX490E', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX1487E-MAX491E.pdf', 'kicadSymbolki_keywords': 'Full duplex RS-485/RS-422, 2.5 Mbps, ±15kV electro-static discharge (ESD) protection, no slew-rate limited, no low-power shutdown, no with receiver/driver enable, 32 receiver drive kapacitity, -40 to +85 degree Celsius, DIP-8 and SOIC-8', 'kicadSymbolki_description': 'Full duplex RS-485/RS-422, 2.5 Mbps, ±15kV electro-static discharge (ESD) protection, no slew-rate limited, no low-power shutdown, no with receiver/driver enable, 32 receiver drive kapacitity, -40 to +85 degree Celsius, DIP-8 and SOIC-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('MAX490E')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

