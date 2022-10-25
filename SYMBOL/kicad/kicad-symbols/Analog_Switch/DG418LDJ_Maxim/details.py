
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_Switch"
    oIndex = "DG418LDJ_Maxim"
    hexID = "SZKANALOGSWITCHDG418LDJMAXIM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DG418LDJ_Maxim', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/DG417-DG419.pdf', 'kicadSymbolki_keywords': 'CMOS Analog Switch', 'kicadSymbolki_description': 'Single SPST 3V Logic Compatible CMOS Analog Switch, normally OFF, 35Ohm Ron, Maxim-variant without Vlogic, DIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Analog_Switch : DG418LDJ_Maxim')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

