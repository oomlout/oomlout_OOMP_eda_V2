
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "NXE1S0305MC"
    hexID = "SZKREGULATORSWITCHINGNXE1S35MC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NXE2S0505MC', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NXE1S0305MC', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_Murata_NXExSxxxxMC_SMD', 'kicadSymbolDatasheet': 'https://www.murata.com/products/productdata/8807031865374/kdc-nxe1.pdf', 'kicadSymbolki_keywords': 'isolated isolation dc-dc converter transformer', 'kicadSymbolki_description': '1W 3.3V to 5V 200mA DC-DC Converter with 3kV isolation', 'kicadSymbolki_fp_filters': 'Converter*DCDC*Murata*NXExSxxxxMC*'}])
    newPart['name'].append('NXE1S0305MC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

