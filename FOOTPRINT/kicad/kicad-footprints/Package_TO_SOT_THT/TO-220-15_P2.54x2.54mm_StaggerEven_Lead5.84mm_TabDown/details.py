
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_THT"
    oIndex = "TO-220-15_P2.54x2.54mm_StaggerEven_Lead5.84mm_TabDown"
    hexID = "FZKSOTTO2215P254X254STAGGEREVENLEAD584TABDOWN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TO-220-15_P2.54x2.54mm_StaggerEven_Lead5.84mm_TabDown', 'description': 'TO-220-15, Horizontal, RM 1.27mm, staggered type-2, see http://www.st.com/resource/en/datasheet/l298.pdf', 'tags': 'TO-220-15 Horizontal RM 1.27mm staggered type-2', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/TO-220-15_P2.54x2.54mm_StaggerEven_Lead5.84mm_TabDown.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'oval'}})
    newPart['name'].append('Package_TO_SOT_THT : TO-220-15_P2.54x2.54mm_StaggerEven_Lead5.84mm_TabDown')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

