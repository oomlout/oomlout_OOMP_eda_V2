
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Axial_L5.0mm_D3.6mm_P10.00mm_Horizontal_Murata_BL01RN1A2A2"
    hexID = "FZKINLAXIALL5D36P1HORIZONTALMBL1RN1A2A2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Axial_L5.0mm_D3.6mm_P10.00mm_Horizontal_Murata_BL01RN1A2A2', 'description': 'Inductor, Murata BL01RN1A2A2, Axial, Horizontal, pin pitch=10.00mm, length*diameter=5*3.6mm, https://www.murata.com/en-global/products/productdetail?partno=BL01RN1A2A2%23', 'tags': 'inductor axial horizontal', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Axial_L5.0mm_D3.6mm_P10.00mm_Horizontal_Murata_BL01RN1A2A2.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Axial_L5.0mm_D3.6mm_P10.00mm_Horizontal_Murata_BL01RN1A2A2')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

