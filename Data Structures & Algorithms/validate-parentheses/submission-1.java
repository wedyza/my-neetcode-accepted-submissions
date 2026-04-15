class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        HashMap<Character, Character> q = new HashMap<>();
        q.put('[', ']');
        q.put('(', ')');
        q.put('{', '}');

        for (int i = 0; i < s.length(); i++) {
            var character = s.charAt(i);
            if (q.containsKey(character))
                stack.push(character);
            else {
                if (stack.size() == 0)
                    return false;
                var closing = stack.pop();
                if (!q.get(closing).equals(character))
                    return false;
            }
        }
        return stack.isEmpty();
    }
}
