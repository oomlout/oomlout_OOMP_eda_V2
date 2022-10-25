
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_THT"
    oIndex = "R_Axial_Power_L38.0mm_W6.4mm_P40.64mm"
    hexID = "FZKRRAXIALPOWERL38W64P464"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_Axial_Power_L38.0mm_W6.4mm_P40.64mm', 'description': 'Resistor, Axial_Power series, Box, pin pitch=40.64mm, 7W, length*width*height=38*6.4*6.4mm^3, http://cdn-reichelt.de/documents/datenblatt/B400/5WAXIAL_9WAXIAL_11WAXIAL_17WAXIAL%23YAG.pdf', 'tags': 'Resistor Axial_Power series Box pin pitch 40.64mm 7W length 38mm width 6.4mm height 6.4mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Axial_Power_L38.0mm_W6.4mm_P40.64mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Resistor_THT : R_Axial_Power_L38.0mm_W6.4mm_P40.64mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

