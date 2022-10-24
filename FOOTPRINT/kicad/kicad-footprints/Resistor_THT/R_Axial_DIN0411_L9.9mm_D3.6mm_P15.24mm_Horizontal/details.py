
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_THT"
    oIndex = "R_Axial_DIN0411_L9.9mm_D3.6mm_P15.24mm_Horizontal"
    hexID = "FZKRRAXIALDIN411L99D36P1524HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_Axial_DIN0411_L9.9mm_D3.6mm_P15.24mm_Horizontal', 'description': 'Resistor, Axial_DIN0411 series, Axial, Horizontal, pin pitch=15.24mm, 1W, length*diameter=9.9*3.6mm^2', 'tags': 'Resistor Axial_DIN0411 series Axial Horizontal pin pitch 15.24mm 1W length 9.9mm diameter 3.6mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_THT.3dshapes/R_Axial_DIN0411_L9.9mm_D3.6mm_P15.24mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Resistor_THT : R_Axial_DIN0411_L9.9mm_D3.6mm_P15.24mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

