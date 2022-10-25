
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_JLCC_Basic"
    oIndex = "CAPC-0402-X-UF10-V63D-C4U1063D-C15525"
    hexID = "FZKICADOOMLOUTOOMPKICADOOMLOUTOOMPJLCCBASICCAPC42XUF1V63DC4U163DC15525"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'CAPC-0402-X-UF10-V63D-C4U1063D-C15525', 'description': 'hexID: C4U1063D;PARTL C-JLCC;C15525;MANUF C-XXXX;CL05A106MQ5NUNC; Capacitor SMD 0402 (1005 Metric), square (rectangular) end terminal, IPC_7351 nominal, (Body size source: IPC-SM-782 page 76, https://www.pcb-3d.com/wordpress/wp-content/uploads/ipc-sm-782a_amendment_1_and_2.pdf), generated with kicad-footprint-generator', 'tags': 'capacitor', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_SMD.3dshapes/C_0402_1005Metric.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('oomlout_OOMP_JLCC_Basic : CAPC-0402-X-UF10-V63D-C4U1063D-C15525')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

