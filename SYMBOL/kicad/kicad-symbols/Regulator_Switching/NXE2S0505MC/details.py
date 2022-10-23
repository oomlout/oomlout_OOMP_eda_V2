
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "NXE2S0505MC"
    hexID = "SZKREGULATORSWITCHINGNXE2S55MC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NXE2S0505MC', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_Murata_NXExSxxxxMC_SMD', 'kicadSymbolDatasheet': 'https://www.murata.com/products/productdata/8807031898142/kdc-nxe2.pdf', 'kicadSymbolki_keywords': 'isolated isolation dc-dc converter transformer', 'kicadSymbolki_description': '2W 5V to 5V 400mA DC-DC Converter with 3kV isolation', 'kicadSymbolki_fp_filters': 'Converter*DCDC*Murata*NXExSxxxxMC*'}])
    newPart['name'].append('NXE2S0505MC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

