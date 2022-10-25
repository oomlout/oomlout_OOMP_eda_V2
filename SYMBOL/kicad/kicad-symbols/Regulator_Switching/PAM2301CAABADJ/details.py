
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "PAM2301CAABADJ"
    hexID = "SZKREGULATORSWITCHINGPAM231CAABADJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PAM2301CAABADJ', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TSOT-23-5', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/products_inactive_data/PAM2301.pdf', 'kicadSymbolki_keywords': 'Voltage regulator switching buck fixed output analog', 'kicadSymbolki_description': '800mA, Step-Down DC/DC-Converter, Adjustable Output Voltage, 1.5MHz, TSOT-23-5', 'kicadSymbolki_fp_filters': 'TSOT?23*'}])
    newPart['name'].append('Regulator_Switching : PAM2301CAABADJ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

