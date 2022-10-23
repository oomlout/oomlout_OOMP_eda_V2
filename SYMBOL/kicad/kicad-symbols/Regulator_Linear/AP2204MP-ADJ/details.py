
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "AP2204MP-ADJ"
    hexID = "SZKREGULATORLINEARAP224MPADJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AP2204MP-ADJ', 'kicadSymbolFootprint': 'Package_SO:Diodes_PSOP-8', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/AP2204.pdf', 'kicadSymbolki_keywords': 'linear regulator ldo adjustable positive', 'kicadSymbolki_description': '150mA low dropout adjustable linear regulator, wide input voltage range, PSOP-8 package', 'kicadSymbolki_fp_filters': 'Diodes*PSOP*'}])
    newPart['name'].append('AP2204MP-ADJ')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

