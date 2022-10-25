
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "MEE3S1212SC"
    hexID = "SZKCONMEE3S1212SC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MEE3S0505SC', 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'MEE3S1212SC', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_Murata_MEE3SxxxxSC_THT', 'kicadSymbolDatasheet': 'https://power.murata.com/pub/data/power/ncl/kdc_mee3.pdf', 'kicadSymbolki_keywords': 'murata DC/DC isolated converter', 'kicadSymbolki_description': '3W, 1000 VDC isolated DC/DC converter, 12V input, 12V output, SIP', 'kicadSymbolki_fp_filters': 'Converter*DCDC*Murata*MEE3SxxxxSC*THT*'}])
    newPart['name'].append('Converter_DCDC : MEE3S1212SC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

