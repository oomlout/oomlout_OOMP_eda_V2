
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Axial_L16.0mm_D7.5mm_P5.08mm_Vertical_Fastron_XHBCC"
    hexID = "FZKINLAXIALL16D75P58VERTICALFASTRONXHBCC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Axial_L16.0mm_D7.5mm_P5.08mm_Vertical_Fastron_XHBCC', 'description': 'Inductor, Axial series, Axial, Vertical, pin pitch=5.08mm, , length*diameter=16*7.5mm^2, Fastron, XHBCC, http://www.fastrongroup.com/image-show/26/XHBCC.pdf?type=Complete-DataSheet&productType=series', 'tags': 'Inductor Axial series Axial Vertical pin pitch 5.08mm  length 16mm diameter 7.5mm Fastron XHBCC', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Axial_L16.0mm_D7.5mm_P5.08mm_Vertical_Fastron_XHBCC.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Axial_L16.0mm_D7.5mm_P5.08mm_Vertical_Fastron_XHBCC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

