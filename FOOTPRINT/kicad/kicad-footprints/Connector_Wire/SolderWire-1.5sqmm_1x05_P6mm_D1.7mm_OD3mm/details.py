
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Wire"
    oIndex = "SolderWire-1.5sqmm_1x05_P6mm_D1.7mm_OD3mm"
    hexID = "FZKCNWIRESOLDERWIRE15SQ1X5P6D17OD3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SolderWire-1.5sqmm_1x05_P6mm_D1.7mm_OD3mm', 'description': 'Soldered wire connection, for 5 times 1.5 mm² wires, basic insulation, conductor diameter 1.7mm, outer diameter 3mm, size source Multi-Contact FLEXI-E 1.5 (https://ec.staubli.com/AcroFiles/Catalogues/TM_Cab-Main-11014119_(en)_hi.pdf), bend radius 3 times outer diameter, generated with kicad-footprint-generator', 'tags': 'connector wire 1.5sqmm', 'attributeType': None, 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Wire.3dshapes/SolderWire-1.5sqmm_1x05_P6mm_D1.7mm_OD3mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Wire : SolderWire-1.5sqmm_1x05_P6mm_D1.7mm_OD3mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

