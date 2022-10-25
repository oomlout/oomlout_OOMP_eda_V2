
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_THT"
    oIndex = "R_Axial_Power_L48.0mm_W12.5mm_P7.62mm_Vertical"
    hexID = "FZKRRAXIALPOWERL48W125P762VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_Axial_Power_L48.0mm_W12.5mm_P7.62mm_Vertical', 'description': 'Resistor, Axial_Power series, Axial, Vertical, pin pitch=7.62mm, 15W, length*width*height=48*12.5*12.5mm^3, http://cdn-reichelt.de/documents/datenblatt/B400/5WAXIAL_9WAXIAL_11WAXIAL_17WAXIAL%23YAG.pdf', 'tags': 'Resistor Axial_Power series Axial Vertical pin pitch 7.62mm 15W length 48mm width 12.5mm height 12.5mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Axial_Power_L48.0mm_W12.5mm_P7.62mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Resistor_THT : R_Axial_Power_L48.0mm_W12.5mm_P7.62mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

