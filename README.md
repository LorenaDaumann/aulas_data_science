[#Processo de upload no git (vou escrever depois)
1️⃣ Veja a URL atual

Rode:

git remote -v

Deve estar aparecendo algo assim:

https://github.com/LorenaDaumann/aulas_data_science.git

Se estiver https://, é isso que está causando o erro.

2️⃣ Troque para SSH

Execute:

git remote set-url origin git@github.com:LorenaDaumann/aulas_data_science.git
3️⃣ Confirme que mudou
git remote -v

Agora deve aparecer:

git@github.com:LorenaDaumann/aulas_data_science.git

(se aparecer isso, está certo ✅)

4️⃣ Agora sim faça:
git push -u origin master

E deve funcionar 🚀

💡 O que aconteceu?

Você configurou SSH corretamente

Mas o Git ainda estava apontando para a URL HTTPS

Então ele ignorava sua chave SSH

#git commit -m "Atualiza aula5mod2.py" -   PARA ATUALIZAR ARQUIVO
](url)
