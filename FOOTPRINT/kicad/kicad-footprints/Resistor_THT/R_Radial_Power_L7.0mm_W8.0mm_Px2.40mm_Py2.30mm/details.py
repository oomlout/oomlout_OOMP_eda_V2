
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_THT"
    oIndex = "R_Radial_Power_L7.0mm_W8.0mm_Px2.40mm_Py2.30mm"
    hexID = "FZKRRRPOWERL7W8PX24PY23"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_Radial_Power_L7.0mm_W8.0mm_Px2.40mm_Py2.30mm', 'description': 'Resistor, Radial_Power series, Radial, pin pitch=2.40*2.30mm^2, 7W, length*width=7*8mm^2, http://www.vitrohm.com/content/files/vitrohm_series_kv_-_201601.pdf', 'tags': 'Resistor Radial_Power series Radial pin pitch 2.40*2.30mm^2 7W length 7mm width 8mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Radial_Power_L7.0mm_W8.0mm_Px2.40mm_Py2.30mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Resistor_THT : R_Radial_Power_L7.0mm_W8.0mm_Px2.40mm_Py2.30mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

