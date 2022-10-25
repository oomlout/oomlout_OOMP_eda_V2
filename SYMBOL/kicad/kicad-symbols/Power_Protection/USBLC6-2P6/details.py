
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "USBLC6-2P6"
    hexID = "SZKPOWERPROTECTIONULC62P6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'USBLC6-2P6', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-666', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/usblc6-2.pdf', 'kicadSymbolki_keywords': 'usb ethernet video', 'kicadSymbolki_description': 'Very low capacitance ESD protection diode, 2 data-line, SOT-666', 'kicadSymbolki_fp_filters': 'SOT?666*'}])
    newPart['name'].append('Power_Protection : USBLC6-2P6')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

