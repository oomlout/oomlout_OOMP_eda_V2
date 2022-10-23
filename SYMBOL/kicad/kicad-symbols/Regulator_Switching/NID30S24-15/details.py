
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "NID30S24-15"
    hexID = "SZKREGULATORSWITCHINGNID3S2415"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NID30S24-05', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NID30S24-15', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_MeanWell_NID30_THT', 'kicadSymbolDatasheet': 'http://www.meanwell.com/webapp/product/search.aspx?prod=nid30', 'kicadSymbolki_keywords': 'Step-Down Converter Module DC/DC', 'kicadSymbolki_description': '2.5A/30W Step Down Converter Module, fixed 15V Output Voltage, 250kHz, 20-53V Input Voltage', 'kicadSymbolki_fp_filters': 'Converter*DCDC*MeanWell*NID30*THT*'}])
    newPart['name'].append('NID30S24-15')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

