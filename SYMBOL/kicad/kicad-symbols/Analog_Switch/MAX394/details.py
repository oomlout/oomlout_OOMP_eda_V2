
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_Switch"
    oIndex = "MAX394"
    hexID = "SZKANALOGSWITCHMAX394"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX333A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX394', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX394.pdf', 'kicadSymbolki_keywords': 'CMOS Analog Switch', 'kicadSymbolki_description': 'Quad SPDT CMOS Analog Switch, 35Ohm Ron, DIP-20/SOIC-20/SSOP-20/TSSOP-20', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x6.5mm*P0.65mm* SSOP*5.3x7.2mm*P0.65mm* SOIC*7.5x10.3mm*P1.27mm* DIP*W7.62mm* SOIC*7.5x12.8mm*P1.27mm*'}])
    newPart['name'].append('Analog_Switch : MAX394')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

