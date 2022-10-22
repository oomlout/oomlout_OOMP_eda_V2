
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "L_Ferrite_Coupled_1342"
    hexID = "SZKDEVICELFERRITECOUPL1342"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'L', 'kicadSymbolValue': 'L_Ferrite_Coupled_1342', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'inductor choke coil reactor magnetic coupled', 'kicadSymbolki_description': 'Coupled inductor with ferrite core', 'kicadSymbolki_fp_filters': 'Choke_* *Coil* Inductor_* L_*'}])
    newPart['name'].append('L_Ferrite_Coupled_1342')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

