
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_THT"
    oIndex = "TO-220F-15_P2.54x5.08mm_StaggerEven_Lead5.08mm_Vertical"
    hexID = "FZKSOTTO22F15P254X58STAGGEREVENLEAD58VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TO-220F-15_P2.54x5.08mm_StaggerEven_Lead5.08mm_Vertical', 'description': 'TO-220F-15, Vertical, RM 1.27mm, MultiwattF-15, staggered type-2', 'tags': 'TO-220F-15 Vertical RM 1.27mm MultiwattF-15 staggered type-2', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/TO-220F-15_P2.54x5.08mm_StaggerEven_Lead5.08mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Package_TO_SOT_THT : TO-220F-15_P2.54x5.08mm_StaggerEven_Lead5.08mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

