
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "CRE1S0505S3C"
    hexID = "SZKREGULATORSWITCHINGCRE1S55S3C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CRE1S0505S3C', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_Murata_CRE1xxxxxx3C_THT', 'kicadSymbolDatasheet': 'http://power.murata.com/datasheet?/data/power/ncl/kdc_cre1.pdf', 'kicadSymbolki_keywords': 'Murata isolated isolation dc-dc converter transformer', 'kicadSymbolki_description': '5V to 5V 200mA, Isolated 2W Single-Output DC-DC Converter Modules with 3kV isolation, SIP-4', 'kicadSymbolki_fp_filters': 'Converter*DCDC*Murata*CRE1xxxxxx3C*'}])
    newPart['name'].append('Regulator_Switching : CRE1S0505S3C')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

