class Solution {

    public String encode(List<String> strs) {
        String res = "";
        for (String s : strs){
            res += s.length() + "#" + s;
        }
        return res;
    }

    public List<String> decode(String str) {
        int i = 0;
        List<String> res = new ArrayList(){};
        while (i < str.length() - 1){
            int j = i;
            while (!str.substring(j, j+1).equals("#")){
                j += 1;
            }
            int length = Integer.parseInt(str.substring(i, j));
            String word = str.substring(j+1, j + 1 + length);
            res.add(word);
            i = j + 1 + length;
        }
        return res;
    }
}
