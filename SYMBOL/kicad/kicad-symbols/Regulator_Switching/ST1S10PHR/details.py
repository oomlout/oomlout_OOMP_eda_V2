
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "ST1S10PHR"
    hexID = "SZKREGULATORSWITCHINGST1S1PHR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ST1S10PHR', 'kicadSymbolFootprint': 'Package_SO:TI_SO-PowerPAD-8', 'kicadSymbolDatasheet': 'http://www.st.com/internet/com/TECHNICAL_RESOURCES/TECHNICAL_LITERATURE/DATASHEET/CD00169322.pdf', 'kicadSymbolki_keywords': 'DC/DC Buck Conwerter 3A Low Voltage Input', 'kicadSymbolki_description': '3A monolithic synchronous step-down regulator, Adjustable Output Voltage, 2.5-18V Input Voltage, 900kHz, PowerSO-8', 'kicadSymbolki_fp_filters': 'TI*SO*PowerPAD*'}])
    newPart['name'].append('ST1S10PHR')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

