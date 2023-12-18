%{
int count_0 = 0;
int count_255 = 0;
%}

%%
0       { count_0++; }
255     { count_255++; }
.       ;  // Ignora cualquier otro carácter
%%

int main() {
    yylex();
    printf("Número de pixeles negros: %d\n", count_0);
    printf("Número de pixeles blancos: %d\n", count_255);
    return 0;
}