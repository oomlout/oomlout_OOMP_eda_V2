
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_Wuerth_WE-DD-Typ-M-Typ-S"
    hexID = "FZKINDUCTORSMLWUERTHWEDDTYPMTYPS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Wuerth_WE-DD-Typ-M-Typ-S', 'description': 'Shielded Coupled Inductor, Wuerth Elektronik, WE-DD, SMD, Typ M, Typ S, https://katalog.we-online.com/pbs/datasheet/744878001.pdf, https://katalog.we-online.de/pbs/datasheet/744877001.pdf', 'tags': 'Choke Coupled Double Inductor SMD Wuerth WE-DD TypM TypS', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Wuerth_WE-DD-Typ-M-Typ-S.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Inductor_SMD : L_Wuerth_WE-DD-Typ-M-Typ-S')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

