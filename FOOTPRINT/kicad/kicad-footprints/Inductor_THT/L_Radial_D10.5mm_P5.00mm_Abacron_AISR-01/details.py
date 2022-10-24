
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "L_Radial_D10.5mm_P5.00mm_Abacron_AISR-01"
    hexID = "FZKINLRD15P5ABACRONAISR1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Radial_D10.5mm_P5.00mm_Abacron_AISR-01', 'description': 'Inductor, Radial series, Radial, pin pitch=5.00mm, , diameter=10.5mm, Abacron, AISR-01, http://www.abracon.com/Magnetics/radial/AISR-01.pdf', 'tags': 'Inductor Radial series Radial pin pitch 5.00mm  diameter 10.5mm Abacron AISR-01', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Radial_D10.5mm_P5.00mm_Abacron_AISR-01.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Inductor_THT : L_Radial_D10.5mm_P5.00mm_Abacron_AISR-01')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

