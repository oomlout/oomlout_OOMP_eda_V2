
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "ST1S12XX"
    hexID = "SZKREGULATORSWITCHINGST1S12XX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ST1S12XX', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TSOT-23-5', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/st1s12xx.pdf', 'kicadSymbolki_keywords': 'DC/DC Buck Converter 0.7A', 'kicadSymbolki_description': '0.7A synchronous step-down regulator, Adjustable Output Voltage, 2.5-5.5V Input Voltage, 1.7MHz, TSOT-23-5', 'kicadSymbolki_fp_filters': 'TSOT?23*'}])
    newPart['name'].append('Regulator_Switching : ST1S12XX')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

