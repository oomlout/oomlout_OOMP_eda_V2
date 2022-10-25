
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "PAM2305AAB250"
    hexID = "SZKREGULATORSWITCHINGPAM235AAB25"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PAM2305AAB330', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PAM2305AAB250', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TSOT-23-5', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/PAM2305.pdf', 'kicadSymbolki_keywords': 'Voltage regulator switching buck fixed output analog', 'kicadSymbolki_description': '1A, Step-Down DC/DC-Converter, 2.5V Fixed Output Voltage, 1.5MHz, TSOT-23', 'kicadSymbolki_fp_filters': 'TSOT?23*'}])
    newPart['name'].append('Regulator_Switching : PAM2305AAB250')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

