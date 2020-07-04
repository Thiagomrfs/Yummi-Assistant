# coding: utf-8
def cipher(entrada, senha, modo=1, sec_number=10000):
    
    import random

    alfa = ('\\', '\n', ' ', 'f', 'ī', 'a', 'q', '#', 'Ŧ', 'ǯ', '¿', 'Ǆ', 'ƍ', '™', '®', 'Ġ', '0', 'ķ', 'L', 'Ā', 'O', 'Ə', 'ō', '&', 'ǡ', '³', 't', 'ă', 'Ǒ', '¹', 'Â', 'ď', 'Ǭ', '¶', 'ǜ', '`', 'Ǟ', 'ȁ', 'ţ', 'ƣ', 'ő', 'ǽ', 'Ț', 'ċ', 'ø', '–', 'ș', 'Ȕ', 'Ò', 'Ɖ', 'Ŭ', 'Ǯ', 'ȍ', 'ȟ', 'Ǉ', '€', 'ĩ', 'ĺ', 'Ļ', '”', 'Ɯ', 'Ī', 'ǳ', 'ę', 'ð', 'ơ', 'ƙ', 'Ű', '|', 'Ř', 'â', 'ŭ', 'ǀ', '1', 'è', '<', 'Ǔ', 'Ŋ', '‚', 'ż', 'Ă', '·', 'ã', '‡', '¾', '—', 'Ũ', 'Ĥ', 'Ȓ', 'ƻ', 'Ǻ', 'o', '7', '÷', 'Ɛ', '-', '«', 'Ô', 'Ǝ', 'Ţ', 'ƒ', 'd', 'Ƒ', 'ê', 'ƃ', 'Ʋ', 'ª', 'Ɗ', 'ˆ', 'ó', 'ĸ', '»', 'ƕ', 'ŉ', '¡', 'Ħ', 'š', 'ŕ', 'ú', 'Ɲ', '…', 'V', 'ȉ', 'Ȗ', 'J', 'Õ', 'Ņ', 'ȓ', 'Ȇ', ']', 'ŵ', 'ļ', 'Đ', '%', 'Ʒ', 'K', 'ŝ', 'ǧ', 'R', 'Ȃ', 'ǝ', 'Ǚ', 'Ï', "'", 'ǟ', 'Ś', 'ȗ', 'Ė', 'Ŀ', 'Ƶ', 'Æ', 'Ŕ', 'ņ', 'Ƕ', '¦', 'ŏ', 'ǥ', 'ǉ', 'Ǡ', 'į', 'ı', 'ý', 'ù', 'õ', 'ô', 'Û', 'B', '›', 'Á', 'ȝ', '8', 'º', 'Ñ', 'Ǿ', 'ŷ', 'Ȝ', 'Ŷ', 'ŋ', 'ä', 'Ƅ', '±', '´', 'Ķ', 'Ư', 'þ', 'ź', '’', 'ů', 'ƀ', 'æ', 'ư', 'Ǜ', 'Ƈ', 'ť', 'ň', 'Ü', 'Ƹ', 'ǐ', 'ȅ', 'i', 'È', 'ś', 'z', '?', 'œ', 'ǁ', 'ŧ', 'ğ', 'g', 'ǣ', 'á', 'Č', 'Ĵ', 'Ģ', 'Ö', '‹', 'ā', 'Ŵ', '5', 'h', 'Ō', 'ǋ', 'ģ', 'Ɣ', 'ƨ', 'Ɵ', 'Ä', 'F', 'ǭ', 'Ľ', 'ƅ', 'Ȋ', '*', 'Ǽ', 'Ǥ', 'ǆ', 'č', 'Ɔ', 'ƪ', 'N', 'Î', 'ž', ',', 'Ĳ', 'ǫ', 'ö', ';', 'Ʀ', '•', '"', 'ƹ', '2', 'Š', 'Ź', 'Ç', 'Ɩ', 'k', '_', 'Ÿ', 'ß', 'ƈ', 'ľ', 'ȋ', '=', 'Ǌ', 'ē', 'u', 'b', 'ȑ', '×', 'í', 'Ǎ', 'ƭ', 'ĭ', '½', 'E', 'ç', 'ć', 'ĵ', '¨', 'Ž', '3', 'å', 'T', 'Å', 'ĉ', 'Ș', 'ǹ', 'ȏ', 'ų', 'ì', '°', 'Ȁ', 'ï', 'Ǘ', '$', 'Ĝ', '¯', 'r', 'đ', 'ǈ', 'Ż', 'Ĕ', 'Ǵ', '9', 'l', 'm', 'ǩ', 'Ê', 'Ų', 'c', 'Ȟ', 'A', 'Ƙ', 'X', 'ħ', 'M', 'Í', 's', '²', 'à', 'ƴ', 'ȇ', 'ǻ', '‰', '4', '„', 'ǘ', 'î', 'ñ', 'Ʈ', '/', 'Ǖ', 'Ş', 'Ȑ', 'ƚ', 'Ơ', ')', 'ÿ', 'ƶ', '}', '¼', 'Ĭ', 'ƿ', 'Ď', 'p', 'ĳ', 'Ù', 'x', 'Ʊ', 'ş', 'P', 'Ǹ', 'Þ', 'Ő', '.', 'Ƿ', 'ƛ', 'S', 'Ƨ', 'Ë', '+', '!', 'Ą', 'Ã', '~', 'ą', 'é', 'Z', 'Ů', 'ſ', 'ǵ', 'Ȍ', 'ȕ', 'Ĺ', 'Ì', 'Ǐ', 'ƾ', '©', 'Ń', 'ǌ', '{', 'Ý', 'Ň', 'ǂ', 'Ƥ', 'Ȉ', 'Ŗ', 'Į', 'Ł', 'y', 'Ĩ', 'ƞ', 'U', 'Q', 'ě', 'I', 'ü', 'Y', 'ǎ', 'ĕ', '“', ':', '¢', 'Ć', 'ŗ', '¥', 'Ƭ', '˜', 'ń', 'ǅ', 'Ɨ', 'Ð', 'ũ', 'Ƴ', 'ƌ', 'ĥ', 'Ǣ', 'H', 'ű', '¬', '(', 'Ȏ', 'µ', 'e', '@', 'Ƽ', 'ƺ', '^', 'ł', 'Ǳ', 'ǿ', 'ǃ', 'û', 'Ť', '§', 'ū', 'ë', 'À', 'Ē', 'W', '[', 'ƥ', 'É', 'ŀ', 'Ø', 'Ǩ', 'ǚ', 'w', 'ĝ', '‘', 'Ƌ', 'ǰ', 'ȃ', 'ė', 'G', 'Ğ', 'C', 'Ƣ', 'D', '£', 'Œ', '>', '†', 'Ǫ', 'Ū', 'j', 'ǔ', 'İ', 'ƫ', 'Ʃ', 'Ƃ', 'Ú', 'ǒ', 'Ǧ', 'Ȅ', '¸', 'ř', 'ǖ', 'Ŏ', 'ǲ', 'Ě', 'ƽ', 'n', 'ġ', '6', 'Ę', 'Ɠ', 'Ŝ', 'Ĉ', 'ț', 'v', 'Ó', 'Ɓ', 'Ċ', '¤', 'ò')
    
    erro_modo = 0
    erro_senha = 0
    erro_entrada = 0
    total_erro = 0
    caracteres_inexistentes = []

    if type(entrada) != str or type(senha) != str or type(modo) != int:
        ValueError('Formato de entrada invalido!, a entrada e a senha devem ser uma String, e o modo deve ser um inteiro')

    for A in entrada:
        if A not in alfa:
            
            erro_entrada += 1
            caracteres_inexistentes.append(A)
            total_erro += 1

    for A in senha:
        if A not in alfa:
            
            erro_senha += 1
            caracteres_inexistentes.append(A)
            total_erro += 1

    if modo != 1 and modo != 2:

        erro_modo += 1
        total_erro += 1

    ermodo = 'SIM' if erro_modo > 0 else 'NÂO'
    if total_erro > 0:
        raise ValueError('Entradas invalidas!!!', f'Erros na entrada = {erro_entrada}, erros na senha = {erro_senha}, modo invalido = {ermodo}, erros de compatibilidade = {caracteres_inexistentes}')

    #========================================================

    senhaCon = senha + str(len(entrada))

    saidaSenCon = ''
    for A in senhaCon:
        saidaSenCon += str(alfa.index(A))

    random.seed(saidaSenCon)

    #========================================================


    saida = []
    saida2 = ''
    n1 = 0

    if modo == 1:

        for A in entrada:
            n1 += random.randint(0, sec_number)
            saida.append(alfa.index(A) + n1)
            if n1 > sec_number*2:
                n1 - sec_number
    elif modo == 2:

        for A in entrada:
            n1 += random.randint(0, sec_number)
            saida.append(alfa.index(A) - n1)
            if n1 > sec_number*2:
                n1 - sec_number
    for A in saida:
        
        B = A
        
            
        if modo == 1:
            
            B -= ((len(alfa)-1)*(B//(len(alfa)-1)))

        elif modo == 2:

            B += abs((len(alfa)-1)*(B//(len(alfa)-1)))

        
        saida2 += alfa[B]


    return saida2