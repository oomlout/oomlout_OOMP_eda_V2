
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Wire"
    oIndex = "SolderWire-2.5sqmm_1x02_P7.2mm_D2.4mm_OD3.6mm_Relief"
    hexID = "FZKCNWIRESOLDERWIRE25SQ1X2P72D24OD36RELIEF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SolderWire-2.5sqmm_1x02_P7.2mm_D2.4mm_OD3.6mm_Relief', 'description': 'Soldered wire connection with feed through strain relief, for 2 times 2.5 mm² wires, basic insulation, conductor diameter 2.4mm, outer diameter 3.6mm, size source Multi-Contact FLEXI-E 2.5 (https://ec.staubli.com/AcroFiles/Catalogues/TM_Cab-Main-11014119_(en)_hi.pdf), bend radius 3 times outer diameter, generated with kicad-footprint-generator', 'tags': 'connector wire 2.5sqmm strain-relief', 'attributeType': None, 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Wire.3dshapes/SolderWire-2.5sqmm_1x02_P7.2mm_D2.4mm_OD3.6mm_Relief.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Wire : SolderWire-2.5sqmm_1x02_P7.2mm_D2.4mm_OD3.6mm_Relief')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

