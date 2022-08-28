// Patrick Bomm dos Santos

public class Analisador {
    int i = 0;
    String alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    String palavra = "";

    public void mandaPalavra(String s) {

        if (isNumber(s.charAt(i)) == true) {
            System.out.println("Erro: Primeiro caracter não pode ser numero");
        } else {
            palavra = s;
            analiser();
        }
    }

    public void analiser() {
        while (i < palavra.length()) {

            // cond parada
            if (i >= palavra.length()) {
                break;
            }

            // caracter em branco
            if (characterEmBranco(palavra.charAt(i)) == true) {
                i++;
                analiser();
                break;

            }

            // caracter não alfanumerico
            if (getNonAlphanumerics(palavra.charAt(i)) == 1) {
                i++;
                analiser();
                break;

            }

            // mais de uma letra consecutiva
            if (i + 3 < palavra.length()) {
                if (isLetter(palavra.charAt(i)) == true && isLetter(palavra.charAt(i + 1)) == true
                        && isLetter(palavra.charAt(i + 2)) == true) {
                    System.out.println(
                            "(" + palavra.charAt(i) + palavra.charAt(i + 1) + palavra.charAt(i + 2) + ", VAR, 1)");
                    i += 3;
                    analiser();
                    break;
                }
            }
            if (i + 2 < palavra.length()) {
                if (isLetter(palavra.charAt(i)) == true && isLetter(palavra.charAt(i + 1)) == true) {
                    System.out.println("(" + palavra.charAt(i) + palavra.charAt(i + 1) + ", VAR, 1)");
                    i += 2;
                    analiser();
                    break;
                }
            }
            // uma só letra
            if (isLetter(palavra.charAt(i)) == true) {
                System.out.println("(" + palavra.charAt(i) + ", VAR, 1)");
                i++;
                analiser();
                break;
            }

            // equals
            if ((i + 1) < palavra.length()) {

                String equals = Character.toString(palavra.charAt(i)) + Character.toString(palavra.charAt(i + 1));
                if (equals.equals(":=")) {
                    System.out.println("(" + palavra.charAt(i) + palavra.charAt(i + 1) + ", ASSIGNOP, 12)");
                    i = i + 2;
                    analiser();
                    break;

                }
                if (equals.equals("==")) {
                    System.out.println("(" + palavra.charAt(i) + palavra.charAt(i + 1) + ", EQOP, 11)");
                    i = i + 2;
                    analiser();
                    break;

                }
            }

            // numeros
            if (isNumber(palavra.charAt(i)) == true) {
                if (i + 2 < palavra.length()) {
                    if (isNumber(palavra.charAt(i + 2)) == true && isNumber(palavra.charAt(i + 1)) == true) {
                        System.out.println(
                                "(" + palavra.charAt(i) + palavra.charAt(i + 1) + palavra.charAt(i + 2) + ", NUM, 2)");
                        if (i + 3 < palavra.length()) {
                            i = i + 3;
                            analiser();
                            break;

                        } else {
                            i = i + 2;
                            analiser();
                            break;

                        }
                    }
                }

                if (i < palavra.length()) {
                    if (isNumber(palavra.charAt(i + 1)) == true) {
                        System.out.println("(" + palavra.charAt(i) + palavra.charAt(i + 1) + ", NUM, 2)");
                        i = i + 2;
                        analiser();
                        break;

                    } else {
                        System.out.println("(" + palavra.charAt(i) + ", NUM, 2)");
                        i++;
                        analiser();
                        break;

                    }
                }
            }

        }
    }

    public boolean isNumber(char c) {
        if (c == '0' || c == '1' || c == '2' || c == '3' || c == '4' || c == '5' || c == '6' || c == '7' || c == '8'
                || c == '9') {
            return true;
        } else {
            return false;
        }
    }

    public int getNonAlphanumerics(char a) {

        if (i >= palavra.length()) {
            return 0;
        }
        if (a == ('+')) {
            System.out.println("(" + a + ", ADDOP, 5)");
            return 1;
        }

        if (a == ('-')) {
            System.out.println("(" + a + ", SUBOP, 6)");
            return 1;

        }

        if (a == ('*')) {
            System.out.println("(" + a + ", MULOP, 7)");
            return 1;

        }

        if (a == ('/')) {
            System.out.println("(" + a + ", DIVOP, 8)");
            return 1;

        }

        if (a == ('(')) {
            System.out.println("(" + a + ", LPAR, 3)");
            return 1;

        }

        if (a == (')')) {
            System.out.println("(" + a + ", RPAR, 4)");
            return 1;

        }

        if (a == ('<')) {
            System.out.println("(" + a + ", STOP, 10)");
            return 1;

        }

        if (a == ('>')) {
            System.out.println("(" + a + ", LTOP, 9)");
            return 1;

        } else {
            return 0;
        }

    }

    public String replace(char r) {
        if (r == ' ') {
            return palavra.replaceFirst(" ", "");
        }
        String aux = Character.toString(r);
        palavra = palavra.replaceFirst(aux, "");
        return palavra;
    }

    public boolean characterEmBranco(char r) {
        if (r == ' ' || r == '\r') {
            return true;
        } else {
            return false;
        }

    }

    public boolean isLetter(char r) {
        if (r == 'a' || r == 'b' || r == 'c' || r == 'd' || r == 'e' || r == 'f' || r == 'g' || r == 'h' || r == 'i'
                || r == 'j' || r == 'k' || r == 'l' || r == 'm' || r == 'n' || r == 'o' || r == 'p' || r == 'q'
                || r == 'r' || r == 's' || r == 't' || r == 'u' || r == 'v' || r == 'w' || r == 'x' || r == 'y'
                || r == 'z') {
            return true;
        } else {
            return false;
        }
    }
}
