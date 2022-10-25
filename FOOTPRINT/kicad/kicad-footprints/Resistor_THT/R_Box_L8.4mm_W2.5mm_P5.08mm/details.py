
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_THT"
    oIndex = "R_Box_L8.4mm_W2.5mm_P5.08mm"
    hexID = "FZKRRBOXL84W25P58"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_Box_L8.4mm_W2.5mm_P5.08mm', 'description': 'Resistor, Box series, Radial, pin pitch=5.08mm, 0.5W = 1/2W, length*width=8.38*2.54mm^2, http://www.vishay.com/docs/60051/cns020.pdf', 'tags': 'Resistor Box series Radial pin pitch 5.08mm 0.5W = 1/2W length 8.38mm width 2.54mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Box_L8.4mm_W2.5mm_P5.08mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Resistor_THT : R_Box_L8.4mm_W2.5mm_P5.08mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

