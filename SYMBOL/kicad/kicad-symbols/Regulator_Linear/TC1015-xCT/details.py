
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TC1015-xCT"
    hexID = "SZKREGULATORLINEARTC115XCT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TC1014-xCT', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TC1015-xCT', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'https://ww1.microchip.com/downloads/aemDocuments/documents/APID/ProductDocuments/DataSheets/21335e.pdf', 'kicadSymbolki_keywords': 'LDO Linear Voltage Regulator', 'kicadSymbolki_description': '100 mA CMOS LDOs with Shutdown and Reference Bypass, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Linear : TC1015-xCT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

