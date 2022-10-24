
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Toroid_Horizontal_D12.7mm_P20.00mm_Diameter14-5mm_Amidon-T50"
    hexID = "FZKINLTOROIDHORIZONTALD127P2DIAMETER145AMIDONT5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Toroid_Horizontal_D12.7mm_P20.00mm_Diameter14-5mm_Amidon-T50', 'description': 'L_Toroid, Horizontal series, Radial, pin pitch=20.00mm, , diameter=12.7mm, Diameter14-5mm, Amidon-T50', 'tags': 'L_Toroid Horizontal series Radial pin pitch 20.00mm  diameter 12.7mm Diameter14-5mm Amidon-T50', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Horizontal_D12.7mm_P20.00mm_Diameter14-5mm_Amidon-T50.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Toroid_Horizontal_D12.7mm_P20.00mm_Diameter14-5mm_Amidon-T50')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

