grammar antlr_expression;

// GRAMMAR

file_ : expr EOF;

expr
   : expr ( '*' | '/' ) expr
   | expr ( '+' | '-' ) expr
   | '(' expr ')'
   | NUMBER
   ;

// LEXER

NUMBER
    : DECIMALS ( '.' DECIMALS )? EXPONENT?
    | DECIMALS? '.' DECIMALS EXPONENT?
    ;

fragment DECIMALS
    : DECIMAL_DIGIT+
    ;

fragment EXPONENT
    : ( 'e' | 'E' ) ( '+' | '-' )? DECIMALS
    ;

fragment DECIMAL_DIGIT
    : [0-9]
    ;

WS
   : [ \r\n\t] + -> skip
   ;
