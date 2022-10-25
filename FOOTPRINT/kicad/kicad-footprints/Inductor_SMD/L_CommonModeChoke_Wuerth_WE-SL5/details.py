
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_CommonModeChoke_Wuerth_WE-SL5"
    hexID = "FZKINDUCTORSMLCOONMODECHOKEWUERTHWESL5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_CommonModeChoke_Wuerth_WE-SL5', 'description': 'WE-SL5 SMT Common Mode Line Filter, https://www.we-online.de/katalog/en/WE-SL5/, https://www.we-online.de/katalog/datasheet/744272471.pdf', 'tags': 'SMT Common Mode Line Filter', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_CommonModeChoke_Wuerth_WE-SL5.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Inductor_SMD : L_CommonModeChoke_Wuerth_WE-SL5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

