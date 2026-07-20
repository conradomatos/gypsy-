# Camadas de aplicação — backend e frontend

## Backend (Django + DRF)
- Regra de negócio fora de serializers e views.
- Services para operações de negócio; selectors/consultas dedicadas para leitura
  não-trivial.
- Serializers e views finos (validar, orquestrar).
- Autenticação Django + permissions DRF. Nenhuma autorização por RLS.
- Migrations exigem revisão — uma intenção por migration.

## Frontend (React + TypeScript)
- TypeScript strict — nunca `any` nem `@ts-ignore`.
- Frontend consome apenas a API REST. Componente visual não acessa banco.
- Chamadas de dados separadas da apresentação.
- Reutilizar componentes; respeitar o design system quando formalizado (SP-02).
- Não criar biblioteca/dependência sem aprovação; não transformar ferramenta
  proposta em decisão.

Estruturas de pasta: ver `padroes_de_codigo.md` (ainda PROPOSTO — não congelar).
