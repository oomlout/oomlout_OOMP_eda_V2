
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Wire"
    oIndex = "SolderWire-1.5sqmm_1x02_P7.8mm_D1.7mm_OD3.9mm_Relief2x"
    hexID = "FZKCNWIRESOLDERWIRE15SQ1X2P78D17OD39RELIEF2X"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SolderWire-1.5sqmm_1x02_P7.8mm_D1.7mm_OD3.9mm_Relief2x', 'description': 'Soldered wire connection with double feed through strain relief, for 2 times 1.5 mm² wires, reinforced insulation, conductor diameter 1.7mm, outer diameter 3.9mm, size source Multi-Contact FLEXI-xV 1.5 (https://ec.staubli.com/AcroFiles/Catalogues/TM_Cab-Main-11014119_(en)_hi.pdf), bend radius 3 times outer diameter, generated with kicad-footprint-generator', 'tags': 'connector wire 1.5sqmm double-strain-relief', 'attributeType': None, 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Wire.3dshapes/SolderWire-1.5sqmm_1x02_P7.8mm_D1.7mm_OD3.9mm_Relief2x.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Wire : SolderWire-1.5sqmm_1x02_P7.8mm_D1.7mm_OD3.9mm_Relief2x')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

