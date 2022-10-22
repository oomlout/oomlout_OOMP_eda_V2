
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "NCS1S2403SC"
    hexID = "SZKCONNCS1S243SC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NCS1S1203SC', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NCS1S2403SC', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_Murata_NCS1SxxxxSC_THT', 'kicadSymbolDatasheet': 'https://power.murata.com/data/power/ncl/kdc_ncs1.pdf', 'kicadSymbolki_keywords': 'Murata isolated isolation dc-dc converter step-down', 'kicadSymbolki_description': 'Isolated 1W 4:1 input DC/DC converter module, 9-36V input voltage, 3.3V output voltage, SIP', 'kicadSymbolki_fp_filters': 'Converter*DCDC*Murata*NCS1SxxxxSC*'}])
    newPart['name'].append('NCS1S2403SC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

