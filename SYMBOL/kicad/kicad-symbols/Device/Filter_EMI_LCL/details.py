
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "Filter_EMI_LCL"
    hexID = "SZKDEVICEFILEMILCL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'FL', 'kicadSymbolValue': 'Filter_EMI_LCL', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.murata.com/~/media/webrenewal/support/library/catalog/products/emc/emifil/c31e.ashx?la=en-gb', 'kicadSymbolki_keywords': 'EMI T-filter', 'kicadSymbolki_description': 'EMI T-filter (LCL)', 'kicadSymbolki_fp_filters': 'Filter* Resonator*'}])
    newPart['name'].append('Device : Filter_EMI_LCL')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

