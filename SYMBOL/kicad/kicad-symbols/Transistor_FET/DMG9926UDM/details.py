
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "DMG9926UDM"
    hexID = "SZKTRANSISTORFETDMG9926UDM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'DMG9926UDM', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-6', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/ds31770.pdf', 'kicadSymbolki_keywords': 'Dual Half Bridge N-Channel MOSFET Logic Level Common Drain', 'kicadSymbolki_description': '4.2A Id, 20V Vds, Common-Drain, Dual Half Bridge N-Channel MOSFET, 28mOhm Ron, SOT-23-6', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Transistor_FET : DMG9926UDM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

