
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "ST1S14PHR"
    hexID = "SZKREGULATORSWITCHINGST1S14PHR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ST1S14PHR', 'kicadSymbolFootprint': 'Package_SO:TI_SO-PowerPAD-8', 'kicadSymbolDatasheet': 'http://www.st.com/internet/com/TECHNICAL_RESOURCES/TECHNICAL_LITERATURE/DATASHEET/CD00285678.pdf', 'kicadSymbolki_keywords': 'DC/DC Buck Conwerter 3A', 'kicadSymbolki_description': '3A step-down switching regulator, Adjustable Output Voltage, 5.5-48V Input Voltage, 850kHz, PowerSO-8', 'kicadSymbolki_fp_filters': 'TI*SO*PowerPAD*'}])
    newPart['name'].append('Regulator_Switching : ST1S14PHR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

