
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Vertical_L41.9mm_W19.1mm_P15.80mm_Vishay_TJ7"
    hexID = "FZKINLTOROIDVERTICALL419W191P158VISHAYTJ7"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Vertical_L41.9mm_W19.1mm_P15.80mm_Vishay_TJ7', 'description': 'L_Toroid, Vertical series, Radial, pin pitch=15.80mm, , length*width=41.9*19.1mm^2, Vishay, TJ7, http://www.vishay.com/docs/34079/tj.pdf', 'tags': 'L_Toroid Vertical series Radial pin pitch 15.80mm  length 41.9mm width 19.1mm Vishay TJ7', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Vertical_L41.9mm_W19.1mm_P15.80mm_Vishay_TJ7.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Vertical_L41.9mm_W19.1mm_P15.80mm_Vishay_TJ7')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

