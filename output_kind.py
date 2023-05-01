import clang.cindex

clang.cindex.Config.set_library_path("/Library/Developer/CommandLineTools/usr/lib")

index = clang.cindex.Index.create()
translation_unit = index.parse('sample_2.cpp', args=['-std=c++17'])

for i in translation_unit.get_tokens(extent=translation_unit.cursor.extent):
    print (i.kind)
