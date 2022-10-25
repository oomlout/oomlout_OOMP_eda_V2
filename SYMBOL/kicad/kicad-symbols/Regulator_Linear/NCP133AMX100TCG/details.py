
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "NCP133AMX100TCG"
    hexID = "SZKREGULATORLINEARNCP133AMX1TCG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NCP133AMX100TCG', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/NCP133-D.PDF', 'kicadSymbolki_keywords': 'Single Output LDO', 'kicadSymbolki_description': '500  mA  VLDO  equipped  with  NMOS  pass transistor  and  a  separate  bias  supply  voltage', 'kicadSymbolki_fp_filters': 'DFN?6?1EP*1.2x1.2mm*P0.4mm*'}])
    newPart['name'].append('Regulator_Linear : NCP133AMX100TCG')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

