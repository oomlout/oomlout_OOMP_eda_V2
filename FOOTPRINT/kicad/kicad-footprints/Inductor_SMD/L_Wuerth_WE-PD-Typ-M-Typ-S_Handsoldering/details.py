
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_Wuerth_WE-PD-Typ-M-Typ-S_Handsoldering"
    hexID = "FZKINDUCTORSMLWUERTHWEPDTYPMTYPSHANDSOLDERING"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Wuerth_WE-PD-Typ-M-Typ-S_Handsoldering', 'description': 'Shielded Power Inductor, Wuerth Elektronik, WE-PD, SMT, Typ M, Typ S, Handsoldering, https://katalog.we-online.com/pbs/datasheet/744778005.pdf', 'tags': 'Choke Shielded Power Inductor WE-PD TypM TypS Wuerth', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Wuerth_WE-PD-Typ-M-Typ-S.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Inductor_SMD : L_Wuerth_WE-PD-Typ-M-Typ-S_Handsoldering')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

