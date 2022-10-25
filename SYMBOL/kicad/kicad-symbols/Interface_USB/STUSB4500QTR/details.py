
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "STUSB4500QTR"
    hexID = "SZKINTERFACEUSTU45QTR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STUSB4500QTR', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-24-1EP_4x4mm_P0.5mm_EP2.7x2.7mm', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/stusb4500.pdf', 'kicadSymbolki_keywords': 'USB PD Type C Sink', 'kicadSymbolki_description': 'Stand-alone USB PD controller (with sink Auto-run mode), QFN-24', 'kicadSymbolki_fp_filters': 'QFN*4x4mm*P0.5mm*'}])
    newPart['name'].append('Interface_USB : STUSB4500QTR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

