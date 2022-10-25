
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "ST1S10PUR"
    hexID = "SZKREGULATORSWITCHINGST1S1PUR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ST1S10PUR', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_4x4mm_P0.8mm_EP2.5x3.6mm', 'kicadSymbolDatasheet': 'http://www.st.com/internet/com/TECHNICAL_RESOURCES/TECHNICAL_LITERATURE/DATASHEET/CD00169322.pdf', 'kicadSymbolki_keywords': 'DC/DC Buck Conwerter 3A Low Voltage Input', 'kicadSymbolki_description': '3A monolithic synchronous step-down regulator, Adjustable Output Voltage, 2.5-18V Input Voltage, 900kHz, DFN-8', 'kicadSymbolki_fp_filters': 'DFN*EP*4x4mm*P0.8mm*'}])
    newPart['name'].append('Regulator_Switching : ST1S10PUR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

