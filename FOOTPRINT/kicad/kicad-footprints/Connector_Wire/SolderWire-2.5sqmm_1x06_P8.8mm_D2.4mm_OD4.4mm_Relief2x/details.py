
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Wire"
    oIndex = "SolderWire-2.5sqmm_1x06_P8.8mm_D2.4mm_OD4.4mm_Relief2x"
    hexID = "FZKCNWIRESOLDERWIRE25SQ1X6P88D24OD44RELIEF2X"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SolderWire-2.5sqmm_1x06_P8.8mm_D2.4mm_OD4.4mm_Relief2x', 'description': 'Soldered wire connection with double feed through strain relief, for 6 times 2.5 mm² wires, reinforced insulation, conductor diameter 2.4mm, outer diameter 4.4mm, size source Multi-Contact FLEXI-xV 2.5 (https://ec.staubli.com/AcroFiles/Catalogues/TM_Cab-Main-11014119_(en)_hi.pdf), bend radius 3 times outer diameter, generated with kicad-footprint-generator', 'tags': 'connector wire 2.5sqmm double-strain-relief', 'attributeType': None, 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Wire.3dshapes/SolderWire-2.5sqmm_1x06_P8.8mm_D2.4mm_OD4.4mm_Relief2x.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Wire : SolderWire-2.5sqmm_1x06_P8.8mm_D2.4mm_OD4.4mm_Relief2x')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

