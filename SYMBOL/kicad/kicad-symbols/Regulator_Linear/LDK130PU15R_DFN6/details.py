
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LDK130PU15R_DFN6"
    hexID = "SZKREGULATORLINEARLDK13PU15RDFN6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LDK130PU08R_DFN6', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LDK130PU15R_DFN6', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-6_1.3x1.2mm_P0.4mm', 'kicadSymbolDatasheet': 'http://www.st.com/content/ccc/resource/technical/document/datasheet/29/10/f7/87/2f/66/47/f4/DM00076097.pdf/files/DM00076097.pdf/jcr:content/translations/en.DM00076097.pdf', 'kicadSymbolki_keywords': 'linear regulator ldo fixed positive low noise low quienscent current', 'kicadSymbolki_description': '300mA low dropout linear regulator, low quiescent current very, low noise, shutdown pin, fixed 1.5V positive output, DFN-6', 'kicadSymbolki_fp_filters': 'DFN*1.3x1.2mm*P0.4mm*'}])
    newPart['name'].append('LDK130PU15R_DFN6')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

