
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Horizontal_D3.2mm_P6.40mm_Diameter3-5mm_Amidon-T12"
    hexID = "FZKINLTOROIDHORIZONTALD32P64DIAMETER35AMIDONT12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Horizontal_D3.2mm_P6.40mm_Diameter3-5mm_Amidon-T12', 'description': 'L_Toroid, Horizontal series, Radial, pin pitch=6.40mm, , diameter=3.175mm, Diameter3-5mm, Amidon-T12', 'tags': 'L_Toroid Horizontal series Radial pin pitch 6.40mm  diameter 3.175mm Diameter3-5mm Amidon-T12', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Horizontal_D3.2mm_P6.40mm_Diameter3-5mm_Amidon-T12.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Horizontal_D3.2mm_P6.40mm_Diameter3-5mm_Amidon-T12')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

