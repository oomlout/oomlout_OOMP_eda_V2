
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "MEE3S0509SC"
    hexID = "SZKCONMEE3S59SC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MEE3S0505SC', 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'MEE3S0509SC', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_Murata_MEE3SxxxxSC_THT', 'kicadSymbolDatasheet': 'https://power.murata.com/pub/data/power/ncl/kdc_mee3.pdf', 'kicadSymbolki_keywords': 'murata DC/DC isolated converter', 'kicadSymbolki_description': '3W, 1000 VDC isolated DC/DC converter, 5V input, 9V output, SIP', 'kicadSymbolki_fp_filters': 'Converter*DCDC*Murata*MEE3SxxxxSC*THT*'}])
    newPart['name'].append('MEE3S0509SC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

