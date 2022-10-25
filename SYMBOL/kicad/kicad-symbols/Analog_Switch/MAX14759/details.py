
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_Switch"
    oIndex = "MAX14759"
    hexID = "SZKANALOGSWITCHMAX14759"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX14759', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_3x3mm_P0.65mm_EP1.55x2.4mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX14759-MAX14763.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'analog switch low resistance above below rails', 'kicadSymbolki_description': 'Above- and Below-the-Rails Low On-Resistance Analog Switches, max 2 Ohms On-Resistance, TDFN-8', 'kicadSymbolki_fp_filters': 'DFN*3x3mm*P0.65mm*'}])
    newPart['name'].append('Analog_Switch : MAX14759')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

