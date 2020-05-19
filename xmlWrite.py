#pythonでXMLを書く
#xml書き込みはファイルを作成するが、withステートメントは不要
import xml.etree.ElementTree as ET

root = ET.Element('root')
#ElementTree:XML 文書を構築してファイルに出力する
tree = ET.ElementTree(element=root)

#SubElement:与えられた要素に新しい子要素を作成する
employee = ET.SubElement(root,'emloyee')

employ = ET.SubElement(root, 'employee')
employ_id = ET.SubElement(employ,'id')
employ_id.text = '111'
employ_id = ET.SubElement(employ, 'name')
employ_id.text = 'Mike'

employ = ET.SubElement(employee,'employ')
employ_id = ET.SubElement(employ,'id')
employ_text = '222'
employ_id = ET.SubElement(employ, 'name')
employ_id.text = 'Nancy'

tree.write('test.xml', encoding='utf-8', xml_declaration=True)

tree = ET.ElementTree(file='test.xml')
root = tree.getroot()

for employee in root:
    for employ in employee:
        for person in employ:
            print(person.tag, person.text)