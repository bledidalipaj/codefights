String decode2(String message) {
    String res = "";
    for(int i = 0; i < message.length(); i++) {
        int value = ((int)message.charAt(i) - 97 + 1) % 26;
        res += (char)((value * value + 25) % 26 + 97);
    }
    return res;
}