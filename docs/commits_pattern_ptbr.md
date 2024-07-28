# Padrões de Commits Convencionais
Ver descrição completa em: [Conventional Commits Pattern](https://github.com/BrunoTanabe/conventional-commits-pattern/).

## 1. Introdução
Commits Convencionais é uma especificação para escrever mensagens de commit consistentes. Ela define um conjunto de regras para criar um histórico de commits explícito, o que facilita a criação de ferramentas automatizadas. Esses padrões têm como objetivo melhorar a legibilidade e a estrutura das mensagens de commit, facilitando, assim, a colaboração e a gestão de projetos.

## 2. Tipos de Commits
Os Padrões de Commits Convencionais incluem vários tipos, cada um servindo a um propósito específico:

- **fix**: Corrige um bug na sua base de código.
- **feat**: Introduz uma nova funcionalidade na base de código.
- **docs**: Apenas mudanças na documentação.
- **style**: Mudanças que não afetam o significado do código (espaços em branco, formatação, falta de ponto e vírgula, etc).
- **refactor**: Uma mudança no código que nem corrige um bug nem adiciona uma funcionalidade.
- **perf**: Melhora o desempenho.
- **test**: Adiciona testes ausentes ou corrige testes existentes.
- **build**: Mudanças que afetam o sistema de build ou dependências externas (escopos de exemplo: gulp, broccoli, npm).
- **ci**: Mudanças em arquivos de configuração e scripts de CI (escopos de exemplo: Travis, Circle, BrowserStack, SauceLabs).
- **chore**: Outras mudanças que não modificam arquivos src ou de teste.
- **wip**: Trabalho em andamento; ainda não está pronto para produção.

## 3. Exemplos
Cada exemplo de mensagem de commit inclui um comando Bash para demonstrar como criar o commit usando Git.

### fix
```bash
git commit -m "fix(order): corrigir erros de digitação menores no código

ver a issue para detalhes sobre os erros de digitação corrigidos"
```
### feat
```bash
git commit -m "feat(blog): adicionar seção de comentários

Os usuários agora podem deixar comentários nos artigos. Esta era uma funcionalidade muito solicitada pelo nosso feedback de usuários."
```
### docs
```bash
git commit -m "docs(changelog): atualizar changelog para 0.3.0"
```
### style
```bash
git commit -m "style(navbar): corrigir indentação"
```
### refactor
```bash
git commit -m "refactor(auth): simplificar lógica de validação"
```
### perf
```bash
git commit -m "perf(rendering): cachear ativos SVG"
```
### test
```bash
git commit -m "test(login): adicionar testes unitários para redefinição de senha"
```
### build
```bash
git commit -m "build(packer): atualizar dependências"
```
### ci
```bash
git commit -m "ci(travis): forçar instalação de dependências"
```
### chore
```bash
git commit -m "chore(release): aumentar versão para 1.0.3"
```
### wip
```bash
git commit -m "wip(feature-x): commit temporário - to be squashed"
```