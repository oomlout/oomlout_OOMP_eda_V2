
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Wire"
    oIndex = "SolderWire-0.15sqmm_1x06_P4mm_D0.5mm_OD1.5mm"
    hexID = "FZKCNWIRESOLDERWIRE15SQ1X6P4D5OD15"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SolderWire-0.15sqmm_1x06_P4mm_D0.5mm_OD1.5mm', 'description': 'Soldered wire connection, for 6 times 0.15 mm² wires, basic insulation, conductor diameter 0.5mm, outer diameter 1.5mm, size source Multi-Contact FLEXI-E 0.15 (https://ec.staubli.com/AcroFiles/Catalogues/TM_Cab-Main-11014119_(en)_hi.pdf), bend radius 3 times outer diameter, generated with kicad-footprint-generator', 'tags': 'connector wire 0.15sqmm', 'attributeType': None, 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Wire.3dshapes/SolderWire-0.15sqmm_1x06_P4mm_D0.5mm_OD1.5mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Wire : SolderWire-0.15sqmm_1x06_P4mm_D0.5mm_OD1.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

