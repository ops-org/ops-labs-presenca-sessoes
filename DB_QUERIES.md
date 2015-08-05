# OPS Labs
# Frequencia dos políticos

Lúcio fez mais um pedido para que fossem gerados alguns relatórios pra melhorar a pesquisa dele.
Fiz algumas consultas no SQLITE e compartilho aqui a fim de enriquecer mais nosso repositório.



# PESSOAS COM FALTA JUSTIFICADA ORGANIZADA POR JUSTIFICATIVA

    SELECT 
        p.name, 
        COUNT(pr.id) as quantidade,
        pr.justificativa
    FROM politician AS p 
    INNER JOIN presence AS pr 
        ON
            pr.politician_id = p.id 
    WHERE
        pr.is_presente = 0 AND
        pr.justificativa IS NOT NULL
    GROUP BY
        p.id, pr.justificativa
    ORDER BY
        quantidade DESC

# Ranking das pessoas faltosas (com ou sem justificativa)
    
    SELECT 
        p.name, 
        count(pr.id) AS soma_faltas 
    FROM politician AS p 
    INNER JOIN presence AS pr 
        ON 
            pr.politician_id = p.id 
    WHERE
        pr.is_presente = 0
    GROUP BY 
        p.id
    ORDER BY
        soma_faltas DESC
        
# Ranking das pessoas com Falta, sem Justificativa

    SELECT 
        p.name, 
        count(pr.id) AS soma_faltas 
    FROM politician AS p 
    INNER JOIN presence AS pr 
        ON 
            pr.politician_id = p.id 
    WHERE
        pr.is_presente = 0 AND pr.justificativa IS NULL
        
    GROUP BY 
        p.id
    ORDER BY
        soma_faltas DESC
