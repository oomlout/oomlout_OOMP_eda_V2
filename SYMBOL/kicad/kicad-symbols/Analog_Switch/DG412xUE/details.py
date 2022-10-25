
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_Switch"
    oIndex = "DG412xUE"
    hexID = "SZKANALOGSWITCHDG412XUE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DG412xUE', 'kicadSymbolFootprint': 'Package_SO:TSSOP-16_4.4x5mm_P0.65mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/DG411-DG413.pdf', 'kicadSymbolki_keywords': 'CMOS Analog Switch', 'kicadSymbolki_description': 'Quad SPST Monolithic CMOS Analog Switches, normally OFF, 17Ohm Ron, TSSOP-16', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x5mm*P0.65mm*'}])
    newPart['name'].append('Analog_Switch : DG412xUE')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

