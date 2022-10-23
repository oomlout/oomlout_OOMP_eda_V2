
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "CRE1S0505DC"
    hexID = "SZKREGULATORSWITCHINGCRE1S55DC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CRE1S0505DC', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_Murata_CRE1xxxxxxDC_THT', 'kicadSymbolDatasheet': 'http://power.murata.com/datasheet?/data/power/ncl/kdc_cre1.pdf', 'kicadSymbolki_keywords': 'Murata isolated isolation dc-dc converter transformer', 'kicadSymbolki_description': '5V to 5V 200mA DC-DC Converter with 1kV isolation, DC-package', 'kicadSymbolki_fp_filters': 'Converter*DCDC*Murata*CRE1xxxxxxDC*'}])
    newPart['name'].append('CRE1S0505DC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

