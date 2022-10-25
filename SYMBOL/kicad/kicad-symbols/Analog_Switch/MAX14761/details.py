
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_Switch"
    oIndex = "MAX14761"
    hexID = "SZKANALOGSWITCHMAX14761"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX14761', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-10-1EP_3x3mm_P0.5mm_EP1.55x2.48mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX14759-MAX14763.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'analog switch low resistance above below rails', 'kicadSymbolki_description': 'Above- and Below-the-Rails Low On-Resistance Analog Switches, max 2 Ohm On resistor, TDFN-10', 'kicadSymbolki_fp_filters': 'DFN*3x3mm*P0.5mm*'}])
    newPart['name'].append('Analog_Switch : MAX14761')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

