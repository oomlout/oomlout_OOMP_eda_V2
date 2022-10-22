
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "MEE1S1505SC"
    hexID = "SZKCONMEE1S155SC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MEE1S0303SC', 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'MEE1S1505SC', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_Murata_MEE1SxxxxSC_THT', 'kicadSymbolDatasheet': 'https://power.murata.com/pub/data/power/ncl/kdc_mee1.pdf', 'kicadSymbolki_keywords': 'murata DC/DC isolated converter', 'kicadSymbolki_description': '1W, 1000 VDC isolated DC/DC converter, 15V input, 5V output, SIP', 'kicadSymbolki_fp_filters': 'Converter*DCDC*Murata*MEE1SxxxxSC*THT*'}])
    newPart['name'].append('MEE1S1505SC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

