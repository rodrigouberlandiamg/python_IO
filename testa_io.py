arquivo = open('dados/contatos-escrita.csv',encoding='latin-1',mode='a+')

print(type(arquivo.buffer))

# conteudo = arquivo.buffer.read()
# print(conteudo)

texto_bytes = bytes('Este é um texto em bytes.',encoding='latin-1')
# print(type(texto_bytes))
# print(texto_bytes)

contato = bytes('15,Verônica,veronica@veronica.com.br\n', encoding='latin-1')
arquivo.buffer.write(contato)

arquivo.close()
