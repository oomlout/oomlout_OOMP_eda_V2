
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "CRE1S1205SC"
    hexID = "SZKREGULATORSWITCHINGCRE1S125SC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CRE1S0505SC', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CRE1S1205SC', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_Murata_CRE1xxxxxxSC_THT', 'kicadSymbolDatasheet': 'http://power.murata.com/datasheet?/data/power/ncl/kdc_cre1.pdf', 'kicadSymbolki_keywords': 'Murata isolated isolation dc-dc converter transformer', 'kicadSymbolki_description': '12V to 5V 200mA DC-DC Converter with 1kV isolation, SIP-4', 'kicadSymbolki_fp_filters': 'Converter*DCDC*Murata*CRE1xxxxxxSC*'}])
    newPart['name'].append('CRE1S1205SC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

