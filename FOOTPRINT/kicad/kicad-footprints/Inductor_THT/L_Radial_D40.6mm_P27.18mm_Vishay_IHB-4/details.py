
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Radial_D40.6mm_P27.18mm_Vishay_IHB-4"
    hexID = "FZKINLRD46P2718VISHAYIHB4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Radial_D40.6mm_P27.18mm_Vishay_IHB-4', 'description': 'Inductor, Radial series, Radial, pin pitch=27.18mm, , diameter=40.64mm, Vishay, IHB-4, http://www.vishay.com/docs/34015/ihb.pdf', 'tags': 'Inductor Radial series Radial pin pitch 27.18mm  diameter 40.64mm Vishay IHB-4', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Radial_D40.6mm_P27.18mm_Vishay_IHB-4.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Radial_D40.6mm_P27.18mm_Vishay_IHB-4')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

