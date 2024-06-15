Heya, here's a brief explanation for how FLHLang works on the inside.

Step 1.
    It finds its target file specified as its first argument.

Step 2.
    It then puts that file into its parser-lexer-compiler which compiles it into bytecode,
    which is then put into a file named "(filename with extension)flhbytecode.flhb".

Step 3.
    After the parser-lexer-compiler-whatever compiles it into bytecode, it interprets its
    output to run the program.
