
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Resistor_SMD"
    oIndex = "R_Shunt_Vishay_WSK2512_6332Metric_T2.21mm"
    hexID = "FZKRESISTORSMRSHUNTVISHAYWSK25126332METRICT221"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'R_Shunt_Vishay_WSK2512_6332Metric_T2.21mm', 'description': 'Shunt Resistor SMD 2512 (6332 Metric), 2.6mm thick, Vishay WKS2512, Terminal length (T) 2.21mm, 1 to 4.9 milli Ohm (http://http://www.vishay.com/docs/30108/wsk.pdf)', 'tags': 'resistor shunt WSK2512', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Resistor_SMD.3dshapes/R_Shunt_Vishay_WSK2512_6332Metric_T2.21mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Resistor_SMD : R_Shunt_Vishay_WSK2512_6332Metric_T2.21mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

