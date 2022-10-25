
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_THT"
    oIndex = "R_Axial_Power_L20.0mm_W6.4mm_P30.48mm"
    hexID = "FZKRRAXIALPOWERL2W64P348"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_Axial_Power_L20.0mm_W6.4mm_P30.48mm', 'description': 'Resistor, Axial_Power series, Box, pin pitch=30.48mm, 4W, length*width*height=20*6.4*6.4mm^3, http://cdn-reichelt.de/documents/datenblatt/B400/5WAXIAL_9WAXIAL_11WAXIAL_17WAXIAL%23YAG.pdf', 'tags': 'Resistor Axial_Power series Box pin pitch 30.48mm 4W length 20mm width 6.4mm height 6.4mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Axial_Power_L20.0mm_W6.4mm_P30.48mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Resistor_THT : R_Axial_Power_L20.0mm_W6.4mm_P30.48mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

