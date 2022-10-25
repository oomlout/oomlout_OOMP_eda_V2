
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Wire"
    oIndex = "SolderWire-1sqmm_1x05_P5.4mm_D1.4mm_OD2.7mm"
    hexID = "FZKCNWIRESOLDERWIRE1SQ1X5P54D14OD27"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SolderWire-1sqmm_1x05_P5.4mm_D1.4mm_OD2.7mm', 'description': 'Soldered wire connection, for 5 times 1 mm² wires, basic insulation, conductor diameter 1.4mm, outer diameter 2.7mm, size source Multi-Contact FLEXI-E 1.0 (https://ec.staubli.com/AcroFiles/Catalogues/TM_Cab-Main-11014119_(en)_hi.pdf), bend radius 3 times outer diameter, generated with kicad-footprint-generator', 'tags': 'connector wire 1sqmm', 'attributeType': None, 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Wire.3dshapes/SolderWire-1sqmm_1x05_P5.4mm_D1.4mm_OD2.7mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Wire : SolderWire-1sqmm_1x05_P5.4mm_D1.4mm_OD2.7mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

