
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_Switch"
    oIndex = "DG441xJ"
    hexID = "SZKANALOGSWITCHDG441XJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'DG309xJ', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DG441xJ', 'kicadSymbolFootprint': 'Package_DIP:DIP-16_W7.62mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/DG441-DG442.pdf', 'kicadSymbolki_keywords': 'CMOS Analog Switch', 'kicadSymbolki_description': 'Quad SPST Analog Switches, normally ON, 60Ohm Ron, DIP-16', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Analog_Switch : DG441xJ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

