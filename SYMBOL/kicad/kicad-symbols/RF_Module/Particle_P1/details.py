
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Module"
    oIndex = "Particle_P1"
    hexID = "SZKRFMOPARTICLEP1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'Particle_P1', 'kicadSymbolFootprint': 'RF_Module:Particle_P1', 'kicadSymbolDatasheet': 'https://docs.particle.io/datasheets/p1-datasheet/', 'kicadSymbolki_keywords': 'Wi-Fi module', 'kicadSymbolki_description': 'Wi-Fi module, 1MB flash, 128KB RAM', 'kicadSymbolki_fp_filters': 'Particle*P1*'}])
    newPart['name'].append('Particle_P1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

