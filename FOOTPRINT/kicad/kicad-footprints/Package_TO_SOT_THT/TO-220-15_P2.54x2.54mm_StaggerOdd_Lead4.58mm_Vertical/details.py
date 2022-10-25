
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_THT"
    oIndex = "TO-220-15_P2.54x2.54mm_StaggerOdd_Lead4.58mm_Vertical"
    hexID = "FZKSOTTO2215P254X254STAGGERODDLEAD458VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TO-220-15_P2.54x2.54mm_StaggerOdd_Lead4.58mm_Vertical', 'description': 'TO-220-15, Vertical, RM 1.27mm, staggered type-1, see http://www.st.com/resource/en/datasheet/l298.pdf', 'tags': 'TO-220-15 Vertical RM 1.27mm staggered type-1', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/TO-220-15_P2.54x2.54mm_StaggerOdd_Lead4.58mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Package_TO_SOT_THT : TO-220-15_P2.54x2.54mm_StaggerOdd_Lead4.58mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

