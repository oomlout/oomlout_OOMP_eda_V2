
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "Raspberry_Pi_2_3"
    hexID = "SZKCNRASPBERRYPI23"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'Raspberry_Pi_2_3', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.raspberrypi.org/documentation/hardware/raspberrypi/schematics/rpi_SCH_3bplus_1p0_reduced.pdf', 'kicadSymbolki_keywords': 'raspberrypi gpio', 'kicadSymbolki_description': 'expansion header for Raspberry Pi 2 & 3', 'kicadSymbolki_fp_filters': 'PinHeader*2x20*P2.54mm*Vertical* PinSocket*2x20*P2.54mm*Vertical*'}])
    newPart['name'].append('Connector : Raspberry_Pi_2_3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

