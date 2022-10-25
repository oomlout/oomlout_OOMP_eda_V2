
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Wire"
    oIndex = "SolderWire-0.25sqmm_1x01_D0.65mm_OD1.7mm"
    hexID = "FZKCNWIRESOLDERWIRE25SQ1X1D65OD17"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SolderWire-0.25sqmm_1x01_D0.65mm_OD1.7mm', 'description': 'Soldered wire connection, for a single 0.25 mm² wire, basic insulation, conductor diameter 0.65mm, outer diameter 1.7mm, size source Multi-Contact FLEXI-E_0.25 (https://ec.staubli.com/AcroFiles/Catalogues/TM_Cab-Main-11014119_(en)_hi.pdf), bend radius 3 times outer diameter, generated with kicad-footprint-generator', 'tags': 'connector wire 0.25sqmm', 'attributeType': None, 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Wire.3dshapes/SolderWire-0.25sqmm_1x01_D0.65mm_OD1.7mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Wire : SolderWire-0.25sqmm_1x01_D0.65mm_OD1.7mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

