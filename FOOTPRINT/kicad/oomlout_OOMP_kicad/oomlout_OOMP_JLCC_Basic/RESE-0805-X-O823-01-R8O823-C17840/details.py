
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_JLCC_Basic"
    oIndex = "RESE-0805-X-O823-01-R8O823-C17840"
    hexID = "FZKICADOOMLOUTOOMPKICADOOMLOUTOOMPJLCCBASICRESE85XO8231R8O823C1784"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'RESE-0805-X-O823-01-R8O823-C17840', 'description': 'hexID: R8O823;PARTL C-JLCC;C17840;MANUF C-XXXX;0805W8F8202T5E; Resistor SMD 0805 (2012 Metric), square (rectangular) end terminal, IPC_7351 nominal, (Body size source: IPC-SM-782 page 72, https://www.pcb-3d.com/wordpress/wp-content/uploads/ipc-sm-782a_amendment_1_and_2.pdf), generated with kicad-footprint-generator', 'tags': 'resistor', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_SMD.3dshapes/R_0805_2012Metric.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('oomlout_OOMP_JLCC_Basic : RESE-0805-X-O823-01-R8O823-C17840')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

