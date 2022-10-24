
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Vertical_L48.8mm_W25.4mm_P20.80mm_Vishay_TJ8"
    hexID = "FZKINLTOROIDVERTICALL488W254P28VISHAYTJ8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Vertical_L48.8mm_W25.4mm_P20.80mm_Vishay_TJ8', 'description': 'L_Toroid, Vertical series, Radial, pin pitch=20.80mm, , length*width=48.8*25.4mm^2, Vishay, TJ8, http://www.vishay.com/docs/34079/tj.pdf', 'tags': 'L_Toroid Vertical series Radial pin pitch 20.80mm  length 48.8mm width 25.4mm Vishay TJ8', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Vertical_L48.8mm_W25.4mm_P20.80mm_Vishay_TJ8.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Vertical_L48.8mm_W25.4mm_P20.80mm_Vishay_TJ8')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

