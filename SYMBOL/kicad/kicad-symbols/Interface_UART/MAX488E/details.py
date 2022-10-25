
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "MAX488E"
    hexID = "SZKINTERFACEUARTMAX488E"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX488E', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX1487E-MAX491E.pdf', 'kicadSymbolki_keywords': 'Full duplex RS-485/RS-422, 0.25 Mbps, ±15kV electro-static discharge (ESD) protection, slew-rate limited, no low-power shutdown, no with receiver/driver enable, 32 receiver drive kapacitity, 0 to +70 degree Celsius, DIP-8 and SOIC-8', 'kicadSymbolki_description': 'Full duplex RS-485/RS-422, 0.25 Mbps, ±15kV electro-static discharge (ESD) protection, slew-rate limited, no low-power shutdown, no with receiver/driver enable, 32 receiver drive kapacitity, 0 to +70 degree Celsius, DIP-8 and SOIC-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Interface_UART : MAX488E')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

