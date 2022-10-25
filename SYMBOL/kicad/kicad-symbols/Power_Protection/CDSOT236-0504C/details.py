
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "CDSOT236-0504C"
    hexID = "SZKPOWERPROTECTIONCDSOT23654C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SRV05-4', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CDSOT236-0504C', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-6', 'kicadSymbolDatasheet': 'https://www.bourns.com/docs/product-datasheets/cdsot236-0504c.pdf', 'kicadSymbolki_keywords': 'ESD protection diodes', 'kicadSymbolki_description': 'Low capacitance ESD diode / steering Diode Array, SOT23-6', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Power_Protection : CDSOT236-0504C')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

