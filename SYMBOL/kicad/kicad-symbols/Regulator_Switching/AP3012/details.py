
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "AP3012"
    hexID = "SZKREGULATORSWITCHINGAP312"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SC4503TSK', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AP3012', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/AP3012.pdf', 'kicadSymbolki_keywords': 'Step-Up Boost Voltage Regulator', 'kicadSymbolki_description': '500mA, Adjustable Step-Up Voltage Regulator, 1.5MHz Frequency, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Switching : AP3012')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

