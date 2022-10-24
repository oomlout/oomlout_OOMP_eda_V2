
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Radial_D16.8mm_P12.07mm_Vishay_IHB-1"
    hexID = "FZKINLRD168P127VISHAYIHB1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Radial_D16.8mm_P12.07mm_Vishay_IHB-1', 'description': 'Inductor, Radial series, Radial, pin pitch=12.07mm, , diameter=16.8mm, Vishay, IHB-1, http://www.vishay.com/docs/34015/ihb.pdf', 'tags': 'Inductor Radial series Radial pin pitch 12.07mm  diameter 16.8mm Vishay IHB-1', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Radial_D16.8mm_P12.07mm_Vishay_IHB-1.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Radial_D16.8mm_P12.07mm_Vishay_IHB-1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

