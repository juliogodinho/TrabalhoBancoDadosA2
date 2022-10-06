select h.codigo
     , h.salariobruto
     , h.fgts
     , h.irpf
     , h.salarioliquido
     , h.cpf
     , h.cnpj
     , f.nome as funcionario
  from holerite h
  inner join funcionario f
  on h.cpf = f.cpf
  inner join empresa e
  on h.cnpj = e.cnpj
  order by f.nome