
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Heatsink"
    oIndex = "Heatsink_Stonecold_HS-132_32x14mm_2xFixation1.5mm"
    hexID = "FZKHHSTONECOLDHS13232X142XFIXATION15"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Heatsink_Stonecold_HS-132_32x14mm_2xFixation1.5mm', 'description': 'Heatsink, StoneCold HS', 'tags': 'heatsink', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Heatsink.3dshapes/Heatsink_Stonecold_HS-132_32x14mm_2xFixation1.5mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Heatsink : Heatsink_Stonecold_HS-132_32x14mm_2xFixation1.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

