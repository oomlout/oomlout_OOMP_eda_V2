
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_Wuerth_WE-PD2-Typ-L"
    hexID = "FZKINDUCTORSMLWUERTHWEPD2TYPL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Wuerth_WE-PD2-Typ-L', 'description': 'Power Inductor, Wuerth Elektronik, WE-PD2, SMD, Typ L, , https://katalog.we-online.com/pbs/datasheet/74477510.pdf', 'tags': 'Choke Power Inductor WE-PD2 TypL Wuerth', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Wuerth_WE-PD2-Typ-L.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Inductor_SMD : L_Wuerth_WE-PD2-Typ-L')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

