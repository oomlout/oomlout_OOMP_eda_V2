
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock_MetzConnect"
    oIndex = "TerminalBlock_MetzConnect_360425_1x01_Horizontal_ScrewM4.0_Boxed"
    hexID = "FZKTBMETZCONNECTTBMETZCONNECT364251X1HORIZONTALSCREWM4BOXED"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TerminalBlock_MetzConnect_360425_1x01_Horizontal_ScrewM4.0_Boxed', 'description': 'single screw terminal block Metz Connect 360425, block size 9x9mm^2, drill diamater 1.6mm, 4 pads, pad diameter 3.2mm, see http://www.metz-connect.com/de/system/files/METZ_CONNECT_U_Contact_Katalog_Anschlusssysteme_fuer_Leiterplatten_DE_31_07_2017_OFF_024803.pdf?language=en page 134, script-generated using https://github.com/pointhi/kicad-footprint-generator/scripts/TerminalBlock_MetzConnect', 'tags': 'THT single screw terminal block Metz Connect 360425 size 9x9mm^2 drill 1.6mm pad 3.2mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock_MetzConnect.3dshapes/TerminalBlock_MetzConnect_360425_1x01_Horizontal_ScrewM4.0_Boxed.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('TerminalBlock_MetzConnect : TerminalBlock_MetzConnect_360425_1x01_Horizontal_ScrewM4.0_Boxed')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

