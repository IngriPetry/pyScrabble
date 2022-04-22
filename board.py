
WORD = 'WORD'
LETTER  = 'LETTER'

displayCharacter = {
    (WORD,3) : '#',
    (LETTER,3) : '&',
    (WORD,2) : '*',
    (LETTER,2) : '!'
}

boardMultiplier = {

    (0,0) : (WORD,3),
    (0,7) : (WORD,3),
    (0,14) : (WORD,3),
    (7,0) : (WORD,3),
    (14,0) : (WORD,3),
    (14,7) : (WORD,3),
    (7,14) : (WORD,3),
    (14,14) : (WORD,3),

    (1,5) : (LETTER,3),
    (5,1) : (LETTER,3),
    (5,5) : (LETTER,3),
    (1,9) : (LETTER,3),
    (5,9) : (LETTER,3),
    (5,13) : (LETTER,3),
    (9,1) : (LETTER,3),
    (9,5) : (LETTER,3),
    (9,9) : (LETTER,3),
    (9,13) : (LETTER,3),
    (13,5) : (LETTER,3),
    (23,9) : (LETTER,3),

    (1,1) : (WORD,2),
    (2,2) : (WORD,2),
    (3,3) : (WORD,2),
    (4,4) : (WORD,2),
    (1,13) : (WORD,2),
    (2,12) : (WORD,2),
    (3,11) : (WORD,2),
    (4,10) : (WORD,2),
    (13,1) : (WORD,2),
    (12,2) : (WORD,2),
    (11,3) : (WORD,2),
    (10,4) : (WORD,2),
    (13,13) : (WORD,2),
    (12,12) : (WORD,2),
    (11,11) : (WORD,2),
    (10,10) : (WORD,2),
    (7,7) : (WORD,2),

    (3,0) : (LETTER,2),
    (11,0) : (LETTER,2),
    (11,13) : (LETTER,2),
    (3,13) : (LETTER,2),
    (6,2) : (LETTER,2),
    (6,12) : (LETTER,2),
    (8,2) : (LETTER,2),
    (8,12) : (LETTER,2),
    (7,3) : (LETTER,2),
    (7,11) : (LETTER,2),
    (2,6) : (LETTER,2),
    (2,8) : (LETTER,2),
    (3,7) : (LETTER,2),
    (12,6) : (LETTER,2),
    (12,8) : (LETTER,2),
    (11,7) : (LETTER,2),
    (6,6) : (LETTER,2),
    (8,8) : (LETTER,2),
    (6,8) : (LETTER,2),
    (8,6) : (LETTER,2),

} 
