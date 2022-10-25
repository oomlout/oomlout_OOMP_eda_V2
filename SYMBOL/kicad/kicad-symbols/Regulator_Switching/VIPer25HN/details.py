
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "VIPer25HN"
    hexID = "SZKREGULATORSWITCHINGVIPER25HN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'VIPer25LN', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'VIPer25HN', 'kicadSymbolFootprint': 'Package_DIP:PowerIntegrations_PDIP-8B', 'kicadSymbolDatasheet': 'http://www.st.com/internet/com/TECHNICAL_RESOURCES/TECHNICAL_LITERATURE/DATASHEET/CD00231127.pdf', 'kicadSymbolki_keywords': 'SMPS Controller with MOSFET 12W AC-DC', 'kicadSymbolki_description': '12W SMPS Controller, AC-DC, PDIP-7', 'kicadSymbolki_fp_filters': '*PDIP*8B*'}])
    newPart['name'].append('Regulator_Switching : VIPer25HN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

