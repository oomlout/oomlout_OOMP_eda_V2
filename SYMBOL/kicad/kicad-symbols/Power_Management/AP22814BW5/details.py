
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "AP22814BW5"
    hexID = "SZKPOWERMANAGEMENTAP22814BW5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AP2161W', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AP22814BW5', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/AP22804_14.pdf', 'kicadSymbolki_keywords': 'Limit USB Active Low', 'kicadSymbolki_description': 'Current limited 3A power switch, single channel, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Power_Management : AP22814BW5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

