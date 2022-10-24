
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Axial_L17.5mm_D12.0mm_P20.32mm_Horizontal_Vishay_IM-10-46"
    hexID = "FZKINLAXIALL175D12P232HORIZONTALVISHAYIM146"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Axial_L17.5mm_D12.0mm_P20.32mm_Horizontal_Vishay_IM-10-46', 'description': 'Inductor, Axial series, Axial, Horizontal, pin pitch=20.32mm, , length*diameter=17.5*12mm^2, Vishay, IM-10-46, http://www.vishay.com/docs/34030/im10.pdf', 'tags': 'Inductor Axial series Axial Horizontal pin pitch 20.32mm  length 17.5mm diameter 12mm Vishay IM-10-46', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Axial_L17.5mm_D12.0mm_P20.32mm_Horizontal_Vishay_IM-10-46.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Axial_L17.5mm_D12.0mm_P20.32mm_Horizontal_Vishay_IM-10-46')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

