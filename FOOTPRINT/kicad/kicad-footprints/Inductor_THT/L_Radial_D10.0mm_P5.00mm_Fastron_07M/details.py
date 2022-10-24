
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Radial_D10.0mm_P5.00mm_Fastron_07M"
    hexID = "FZKINLRD1P5FASTRON7M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Radial_D10.0mm_P5.00mm_Fastron_07M', 'description': 'Inductor, Radial series, Radial, pin pitch=5.00mm, , diameter=10mm, Fastron, 07M, http://www.fastrongroup.com/image-show/37/07M.pdf?type=Complete-DataSheet&productType=series', 'tags': 'Inductor Radial series Radial pin pitch 5.00mm  diameter 10mm Fastron 07M', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Radial_D10.0mm_P5.00mm_Fastron_07M.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Radial_D10.0mm_P5.00mm_Fastron_07M')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

