
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_JLCC_Basic"
    oIndex = "CAPC-1206-X-NF20-V50-C12N20-C1857"
    hexID = "FZKICADOOMLOUTOOMPKICADOOMLOUTOOMPJLCCBASICCAPC126XNF2V5C12N2C1857"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'CAPC-1206-X-NF20-V50-C12N20-C1857', 'description': 'hexID: C12N20;PARTL C-JLCC;C1857;MANUF C-XXXX;1206B224K500NT; Capacitor SMD 1206 (3216 Metric), square (rectangular) end terminal, IPC_7351 nominal, (Body size source: IPC-SM-782 page 76, https://www.pcb-3d.com/wordpress/wp-content/uploads/ipc-sm-782a_amendment_1_and_2.pdf), generated with kicad-footprint-generator', 'tags': 'capacitor', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_SMD.3dshapes/C_1206_3216Metric.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('oomlout_OOMP_JLCC_Basic : CAPC-1206-X-NF20-V50-C12N20-C1857')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

